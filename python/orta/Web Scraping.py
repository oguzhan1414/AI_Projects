import requests

# Hedef URL
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Tarayıcı gibi davranmak için bir başlık (headers) bilgisi oluşturuyoruz.
# Bu User-Agent, yaygın bir Chrome tarayıcısını taklit eder.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# GET isteğini oluştururken 'headers' parametresini de gönderiyoruz.
response = requests.get(url, headers=headers)

# Yanıtın durum kodunu kontrol ediyoruz.
if response.status_code == 200:
    # Başarılı ise sayfa içeriğinin ilk 500 karakterini yazdır.
    print("Successfully retrieved data!")
    print(response.text[:500])
else:
    # Başarısız ise hata kodunu yazdır.
    print(f"Failed to retrieve data. Status Code: {response.status_code}")


##############----------------------------------#############

from bs4 import BeautifulSoup
html_content = "<h1 id='firstHeading' class='firstHeading mw-first-heading'><span class='mw-page-title-main'>Python (programming language)</span></h1>"
soup = BeautifulSoup(html_content,"html.parser")
print(soup.h1.text)


#Wikipedi Bilgi çekme

def get_wikipedia_page(konu):
    # Kullanıcıdan gelen konu başlığını URL formatına uygun hale getiriyoruz (boşlukları _ ile değiştiriyoruz).
    uurl = f"https://en.wikipedia.org/wiki/{konu.replace(' ', '_')}"

    # Tarayıcı gibi görünmek için User-Agent başlığı tanımlıyoruz.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # İsteği headers ile birlikte gönderiyoruz.
    # DÜZELTME 2: 'url' yerine doğru değişken olan 'uurl' kullanıldı.
    response = requests.get(uurl, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Sayfa bulunamadı veya bir hata oluştu. Durum Kodu: {response.status_code}")
        return None


def get_article_title(soup):
    # Sayfa başlığını (h1 etiketi) bulup metnini döndürür.
    return soup.find('h1', id='firstHeading').text


# DÜZELTME 3: Özet alma fonksiyonundaki mantık hatası düzeltildi.
def get_article_summary(soup):
    # Sayfadaki tüm paragraf ('p') etiketlerini bulur.
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        # Paragrafın metni boş değilse, bu ilk anlamlı paragraftır ve özettir.
        if para.text.strip():
            return para.text.strip()
    # Eğer döngü biter ve hala metin içeren bir paragraf bulunamazsa bu mesaj döner.
    return "No summary found"


def get_headings(soup):
    # h2, h3, h4 etiketlerini bularak tüm alt başlıkları bir liste olarak döndürür.
    headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings


def get_related_links(soup):
    links = []
    # href özelliğine sahip tüm link ('a') etiketlerini bulur.
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Sadece başka bir Wikipedia makalesine giden linkleri filtreler.
        # DÜZELTME 4: 'startswitch' yerine doğru metot olan 'startswith' kullanıldı.
        if href.startswith('/wiki/') and ":" not in href and not href.startswith('/wiki/Help:'):
            links.append(f"https://en.wikipedia.org{href}")
    # Tekrarlanan linkleri kaldırır (set kullanarak) ve ilk 5 tanesini döndürür.
    return list(set(links))[:5]


def main():
    topic = input("Enter a topic to search on Wikipedia: ").strip()
    if not topic:
        print("Please enter a topic.")
        return

    page_content = get_wikipedia_page(topic)

    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')

        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        related_links = get_related_links(soup)

        print("\n" + "=" * 50)
        print(f"Title: {title}")
        print("=" * 50)

        print("\n--- Summary ---")
        print(summary)

        print("\n--- Headings (Top 5) ---")
        for heading in headings[:5]:
            # İçerik tablosu gibi istenmeyen başlıkları atlayalım.
            if "Contents" not in heading:
                print(f"- {heading}")

        print("\n--- Related Links (Top 5) ---")
        for link in related_links:
            print(f"- {link}")
        print("\n" + "=" * 50)


# Bu scriptin doğrudan çalıştırıldığında main fonksiyonunu çağırmasını sağlar.
if __name__ == "__main__":
    main()