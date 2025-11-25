import requests
from bs4 import BeautifulSoup
import sqlite3
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    # Bazen siteler dil ayarı için bu başlığı da kontrol eder
    'Accept-Language': 'en-US,en;q=0.9,tr;q=0.8',
}


def get_product_info(url):
    """
    Verilen URL'deki ürünün başlığını ve fiyatını çeker.
    """
    try:
        # timeout eklemek, sayfanın çok uzun süre yanıt vermemesi durumunda takılıp kalmayı önler
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        title_element = soup.find("h1", class_="product-title")
        price_element = soup.find("span", class_="price-container")

        if not title_element or not price_element:
            # Bu artık bir hata değil, bir uyarı. None döndürerek ana döngüde yönetilecek.
            return None, None

        product_title = title_element.text.strip()
        price_text = price_element.text.strip()

        cleaned_price = price_text.replace('TL', '').replace('.', '').replace(',', '.').strip()
        price_float = float(cleaned_price)

        return product_title, price_float

    # Hata mesajlarını daha spesifik hale getirelim ki sorunu daha iyi anlayalım
    except requests.exceptions.Timeout:
        print(f"Hata: Sayfa zaman aşımına uğradı ({url})")
        return None, None
    except requests.exceptions.HTTPError as e:
        print(f"Hata: Geçersiz HTTP yanıtı ({e.response.status_code}) - ({url})")
        return None, None
    except requests.exceptions.RequestException as e:
        print(f"Hata: Sayfa çekilemedi ({url}). Hata: {e}")
        return None, None
    except ValueError:
        print(f"Hata: Fiyat dönüştürülemedi. Fiyat formatı beklenmedik olabilir. ({url})")
        return None, None
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu ({url}): {e}")
        return None, None


def veritabani_guncelle(urun_id, guncel_isim, guncel_fiyat):
    """Hem fiyat geçmişine yeni kayıt ekler hem de ürünün ismini günceller."""
    conn = sqlite3.connect('veritabani.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fiyat_gecmisi (urun_id, fiyat) VALUES (?, ?)", (urun_id, guncel_fiyat))
    cursor.execute("UPDATE urunler SET isim = ? WHERE id = ?", (guncel_isim, urun_id))
    conn.commit()
    conn.close()


def main():
    """Veritabanındaki tüm ürünleri kontrol eden ana fonksiyon."""
    while True:
        try:
            conn = sqlite3.connect('veritabani.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, url, hedef_fiyat, isim FROM urunler")
            urunler = cursor.fetchall()
            conn.close()

            if not urunler:
                print("Takip edilecek ürün bulunamadı. Lütfen 'urun_ekle.py' script'i ile ürün ekleyin.")
                time.sleep(60)
                continue

            print(f"--- {time.ctime()} ---")
            print(f"{len(urunler)} adet ürün kontrol ediliyor...")

            for urun in urunler:
                # ========================================================== #
                # <<< YENİ VE ÖNEMLİ KISIM BAŞLANGICI >>>
                # Her bir ürünü kendi try-except bloğu içine alıyoruz
                try:
                    urun_id, url, hedef_fiyat, eski_isim = urun

                    guncel_isim, guncel_fiyat = get_product_info(url)

                    # Eğer get_product_info bir sorun yaşayıp None döndürürse,
                    # bu ürünü atlayıp bir sonrakine geçiyoruz.
                    if guncel_isim is None or guncel_fiyat is None:
                        print(f"-> BİLGİ: '{eski_isim or url}' ürünü için veri alınamadı, bir sonraki ürüne geçiliyor.")
                        continue  # <<< BU KOMUT ÇOK ÖNEMLİ

                    print(f"-> Başarılı: {guncel_isim} | Güncel Fiyat: {guncel_fiyat} TL | Hedef: {hedef_fiyat} TL")
                    veritabani_guncelle(urun_id, guncel_isim, guncel_fiyat)

                    if guncel_fiyat <= hedef_fiyat:
                        print(f"\n🎉🎉🎉 MÜJDE! FİYAT DÜŞTÜ! 🎉🎉🎉")
                        print(f"'{guncel_isim}' ürününün fiyatı belirlediğin {hedef_fiyat} TL hedefinin altına indi!")
                        # BURAYA E-POSTA GÖNDERME KODU GELEBİLİR

                except Exception as e:
                    # Bu blok, get_product_info dışında (örn: veritabani_guncelle'de)
                    # beklenmedik bir hata olursa devreye girer.
                    print(f"'{eski_isim or url}' ürünü işlenirken döngü içinde bir hata oluştu: {e}")
                    print("Bir sonraki ürüne devam ediliyor...")
                    continue  # Hataya rağmen bir sonraki ürüne devam et

                # <<< YENİ VE ÖNEMLİ KISIM BİTİŞİ >>>
                # ======================================================== #

                time.sleep(5)

            print("\nTüm ürünler kontrol edildi. Bir sonraki kontrol 1 saat sonra.")
            time.sleep(3600)

        except Exception as e:
            print(f"Ana döngüde kritik bir hata oluştu: {e}")
            print("60 saniye sonra yeniden denenecek.")
            time.sleep(60)


if __name__ == "__main__":
    main()