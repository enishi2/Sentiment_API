import os
import requests



HF_TOKEN = os.getenv("HF_TOKEN")
print("HF_TOKEN:", HF_TOKEN)


#carrega modelo PT-BR de analise de sentimento
#model_pt = pipeline(
#    "sentiment-analysis",
#    model="lipaoMai/BERT-sentiment-analysis-portuguese-with-undersampling-v2"
#)

#Carrega modelo multilinguas de analise de sentimento
#model_multi = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")

# substitua por um modelo leve DistilBERT
API_URL = "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-xlm-roberta-base-sentiment"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def analyze_sentiment(texts: list[str]):
    results = []

    for text in texts:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text}
        )

        print("Status code:", response.status_code)
        print("Resposta bruta:", response.text)

        data = response.json()

        # Verifica se veio lista dentro de lista
        if isinstance(data, list) and isinstance(data[0], list):
            best = max(data[0], key=lambda x: x["score"])
            results.append({
                "label": best["label"],
                "score": best["score"]
            })
        else:
            print("Formato inesperado:", data)
            results.append({
                "label": "ERROR",
                "score": 0
            })

    return results