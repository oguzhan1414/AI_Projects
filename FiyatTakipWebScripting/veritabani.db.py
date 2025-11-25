import sqlite3

try:
    # veritabani.db adında bir dosya oluşturur veya var olana bağlanır
    connection = sqlite3.connect('veritabani.db')
    cursor = connection.cursor()

    # urunler tablosunu oluştur
    # Kullanıcının girdiği ürünleri ve hedeflerini burada saklayacağız
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS urunler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL UNIQUE,
        isim TEXT,
        hedef_fiyat REAL NOT NULL
    )
    ''')

    # fiyat_gecmisi tablosunu oluştur
    # Her kontrolün sonucunu buraya tarihle birlikte kaydedeceğiz
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fiyat_gecmisi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        urun_id INTEGER NOT NULL,
        fiyat REAL NOT NULL,
        tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (urun_id) REFERENCES urunler (id)
    )
    ''')

    print("Veritabanı ve tablolar başarıyla oluşturuldu veya zaten mevcuttu.")

    # Değişiklikleri kaydet ve bağlantıyı kapat
    connection.commit()
    connection.close()

except sqlite3.Error as e:
    print(f"SQLite hatası: {e}")