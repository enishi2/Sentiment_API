from transformers import pipeline

#carrega modelo PT-BR de analise de sentimento
#model_pt = pipeline(
#    "sentiment-analysis",
#    model="lipaoMai/BERT-sentiment-analysis-portuguese-with-undersampling-v2"
#)

#Carrega modelo multilinguas de analise de sentimento
model_multi = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")


def analyze_sentiment(texts: list[str]):
    results = model_multi(texts)
    return results