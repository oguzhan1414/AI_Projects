from transformers import pipeline
import os

def load_model():
    try:
        # Küçük İngilizce model, Türkçe zayıf ama test için
        generator = pipeline("text-generation", model="gpt2")
        return generator
    except Exception as e:
        print("Model yüklenemedi, dummy metin kullanılacak.", e)
        return None

generator = load_model()

def generate_blog_intro(topic: str) -> str:
    # Eğer model yüklüyse, Hugging Face ile üret
    if generator:
        try:
            prompt = f"SEO uyumlu bir blog yazısı için giriş paragrafı: {topic}"
            result = generator(prompt, max_new_tokens=100, num_return_sequences=1)
            text = result[0]['generated_text']
            # Eğer çıktı anlamsızsa dummy fallback
            if len(text.strip()) < 10:
                raise ValueError("Üretilen metin çok kısa veya anlamsız")
            return text
        except Exception as e:
            print("AI üretim hatası, dummy metin kullanılacak.", e)

    # Dummy fallback (Türkçe, güvenilir)
    return f"'{topic}' hakkında SEO uyumlu bir blog giriş paragrafı: Bu konuda detaylı bilgiler sunacağız ve okuyucuya faydalı ipuçları vereceğiz."
