from transformers import pipeline

#carrega modelo PT-BR de analise de sentimento
#model_pt = pipeline(
#    "sentiment-analysis",
#    model="lipaoMai/BERT-sentiment-analysis-portuguese-with-undersampling-v2"
#)

#Carrega modelo multilinguas de analise de sentimento
#model_multi = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")

# substitua por um modelo leve DistilBERT
model_sst2 = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def analyze_sentiment(texts: list[str]):
    results = model_sst2(texts)
    return results