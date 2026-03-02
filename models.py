from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class CommentAnalysis(Base):
    __tablename__ = "comment_analysis"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
