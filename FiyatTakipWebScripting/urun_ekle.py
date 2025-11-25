import sqlite3


def yeni_urun_ekle():
    """Kullanıcıdan URL ve hedef fiyat alarak veritabanına yeni ürün ekler."""

    print("--- Yeni Ürün Ekleme ---")
    url = input("Takip etmek istediğiniz ürünün URL'ini girin: ").strip()

    while True:
        try:
            hedef_fiyat_str = input("Ürün için hedef fiyatınızı girin (örn: 1500.50): ").strip()
            hedef_fiyat = float(hedef_fiyat_str)
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin (örneğin 1500 veya 1500.50).")

    try:
        connection = sqlite3.connect('veritabani.db')
        cursor = connection.cursor()

        # Ürünü veritabanına ekliyoruz. İsim başlangıçta boş olabilir, ilk kontrolde güncelleriz.
        cursor.execute("INSERT INTO urunler (url, hedef_fiyat) VALUES (?, ?)", (url, hedef_fiyat))

        connection.commit()
        connection.close()

        print("\nBaşarılı! Ürün takip listesine eklendi.")
        print("Fiyat kontrol script'i çalıştığında bu ürün de kontrol edilecek.")

    except sqlite3.IntegrityError:
        print("\nHata: Bu URL zaten takip listesinde mevcut.")
    except sqlite3.Error as e:
        print(f"\nVeritabanı hatası: {e}")


if __name__ == "__main__":
    yeni_urun_ekle()