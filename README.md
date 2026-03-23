# Yapay Zeka ve Veri Bilimi Projeleri Koleksiyonu

<p align="center">
  <i>Derin öğrenme, makine öğrenmesi, veri analizi ve bilgisayarlı görü alanlarındaki keşiflerimi barındıran kapsamlı proje laboratuvarım.</i>
</p>

<p align="center">
  <img src="https://img.icons8.com/color/48/000000/python--v1.png" alt="Python" title="Python" />
  <img src="https://img.icons8.com/color/48/000000/pandas.png" alt="Pandas" title="Pandas" />
  <img src="https://img.icons8.com/color/48/000000/numpy.png" alt="NumPy" title="NumPy" />
  <img src="https://img.icons8.com/color/48/000000/tensorflow.png" alt="TensorFlow" title="TensorFlow" />
  <img src="https://img.icons8.com/nolan/48/machine-learning.png" alt="Scikit-Learn" title="Scikit-Learn / ML" />
</p>

---

## 🚀 Proje Özeti

Bu depo, yapay zeka, veri bilimi ve otomasyon alanında geliştirilmiş çeşitli algoritmaları ve pratik uygulamaları barındıran bir çalışma laboratuvarıdır. Temel seviye Python pratiklerinden başlayarak; duygu analizi, araç fiyatı tahmini, kalp krizi risk analizi, spam e-posta sınıflandırması ve web üzerinden dinamik veri çekimi (scraping) gibi gerçek dünya problemlerine makine öğrenmesi modelleriyle çözümler üretmeye odaklanmaktadır. 

Dağınık ve düzensiz verilerin temizlenerek anlamlı tahminlere dönüştürülmesi sürecinde, farklı algoritma tipleri (Karar Ağaçları, Sinir Ağları vb.) ve modern veri bilimi kütüphaneleri aktif olarak kullanılmıştır.

## ✨ Özellikler (Key Features)

*   **Kapsamlı Veri Ön İşleme (Data Preprocessing):** Eksik verilerin doldurulması, kategorik değişkenlerin dönüştürülmesi (One-Hot Encoding) ve verilerin standartlaştırılması süreçleri.
*   **Makine Öğrenmesi Modelleri:** Karar Ağaçları (Decision Trees) ve regresyon teknikleri ile Araba Fiyat Tahmini ve sağlık analizleri.
*   **Doğal Dil İşleme (NLP):** Metin madenciliği kullanarak Duygu Analizi (Sentiment Analysis) ve Spam E-posta tespiti algoritmaları.
*   **Bilgisayarlı Görü (Computer Vision):** OpenCV kullanarak kamera üzerinden hareket algılama sistemleri.
*   **Derin Öğrenme:** TensorFlow alt yapısı ile geliştirilen yapay sinir ağı taslakları.
*   **Veri Kazıma (Web Scraping):** E-ticaret siteleri üzerinden fiyat takibi ve otomatik web veri analizi otomasyonları.

## 📸 Screenshots

| Duygu Analizi Çıktısı | Veri Ön İşleme Aşaması |
| :---: | :---: |
| ![Placeholder 1](https://via.placeholder.com/400x250.png?text=Duygu+Analizi+Gorseli) | ![Placeholder 2](https://via.placeholder.com/400x250.png?text=Veri+Tablosu+Gorseli) |

> *Not: Projeleri çalıştırdıkça ilgili çıktı ekran görüntülerini yukarıdaki alana ekleyebilirsiniz.*

## ⚙️ Kurulum ve Çalıştırma

Projeleri yerel ortamınızda sorunsuz bir şekilde incelemek ve test etmek için aşağıdaki adımları takip edebilirsiniz.

1. **Depoyu Klonlayın**
```bash
git clone https://github.com/oguzhan1414/AI_Projects.git
cd AI_Projects
```

2. **Sanal Ortam Oluşturun (Opsiyonel ama Önerilir)**
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
```

3. **Gerekli Kütüphaneleri Kurun**
Her klasör farklı teknolojiler barındırdığı için, genel olarak ihtiyaç duyacağınız temel kütüphaneleri tek seferde kurabilirsiniz:
```bash
pip install pandas numpy scikit-learn tensorflow opencv-python beautifulsoup4 requests
```

4. **Projeleri Çalıştırın**
İncelemek istediğiniz projenin bulunduğu klasöre giderek terminal üzerinden scripti çalıştırın. Örneğin Veri Ön İşleme dosyası için:
```bash
cd YapayZekaPro
python VeriOnisleme.py
```