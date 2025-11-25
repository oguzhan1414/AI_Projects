import requests


API_URL = "https://api-inference.huggingface.co/models/gpt2"  # çalışır model
headers = {"Authorization": "Bearer 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"}  # Tokenini buraya yapıştır

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status Code:", response.status_code)   # <-- hata kodunu göreceğiz
    print("Raw Response:", response.text[:500])   # <-- ilk 500 karakteri yazdır
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e)}

output = query({
    "inputs": "Masa nedir konusunda SEO uyumlu bir blog girişi yaz.",
    "parameters": {"max_new_tokens": 100}
})
print(output)




