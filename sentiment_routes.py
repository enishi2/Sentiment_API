from fastapi import APIRouter, Depends, Query
from schemas import CommentsInput
from services import analyze_sentiment
from database import SessionLocal
from models import CommentAnalysis
from schemas import CommentsInput
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime


router = APIRouter(prefix="/sentiment", tags=["sentiment"])





# Dependency profissional para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/analyze-batch")
def analyze_comments(data: CommentsInput, db: Session = Depends(get_db)):
    results = analyze_sentiment(data.comments)

    analyzed = []
    positive = 0
    neutral = 0
    negative = 0

    for comment, result in zip(data.comments, results):
        label = result['label']
        score = result['score']

        stars = int(label.split()[0])  # pega o número da estrela

        if stars <= 2:
            sentiment = "NEGATIVE"
            negative += 1
        elif stars == 3:
            sentiment = "NEUTRAL"
            neutral += 1
        else:
            sentiment = "POSITIVE"
            positive += 1

        #savla no banco de dados

        new_analysis = CommentAnalysis(
            comment=comment,
            sentiment=sentiment,
            confidence=score
        )

        db.add(new_analysis)

        analyzed.append({
            "comment": comment,
            "sentiment": sentiment,
            "confidence": score
        })

    db.commit()

    total = len(data.comments)



    return {
        "Summary": {
            "total_comments": total,
            "positive": positive,
            "neutral": neutral,
            "negative": negative,
            "positive_percentage": round((positive/total) * 100, 2) if total > 0 else 0,
            "negative_percentage": round((negative/total) * 100, 2) if total > 0 else 0,
        },
        "details": analyzed
    }



@router.get("/history")
def get_history(
    db: Session = Depends(get_db),
    sentiment: Optional[str] = Query(None, description="Filtra por sentimento"),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    limit: int = 50,
    offset: int = 0
):
    query = db.query(CommentAnalysis)
    
    if sentiment:
        query = query.filter(CommentAnalysis.sentiment == sentiment.upper())
    if start_date:
        query = query.filter(CommentAnalysis.created_at >= start_date)
    if end_date:
        query = query.filter(CommentAnalysis.created_at <= end_date)

    results = query.order_by(CommentAnalysis.created_at.desc()).offset(offset).limit(limit).all()

    return [
        {
            "comment": r.comment,
            "sentiment": r.sentiment,
            "confidence": r.confidence,
            "created_at": r.created_at
        }
        for r in results
    ]