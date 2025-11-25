with open("../txt_csv_vs/sample.txt", "r") as file:   #with işlem bitince otomatik dosyayı kapatır  "r" ile okuma modu dur
    content = file.read()
    print(content)

    with open("../txt_csv_vs/sample.txt", "r") as file:
        for line in file:
            print(line.strip())


with open("../txt_csv_vs/sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

try:
    with open("asdsadsad.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
except FileNotFoundError: ##DOSYA BULUNAMADI HATASI
    print("File Not Found ERROR")



##yemek tarif projesi

def load_recipes(file_path):
    """
    Verilen dosya yolundan tarifleri okur ve bir sözlük olarak döndürür.
    Her tarifin çift satır boşluğuyla ayrıldığı varsayılır.
    Her tarifin ilk satırı başlıktır.
    """
    try:
        # Dosyayı okuma modunda ve Türkçe karakter desteğiyle aç
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Tüm içeriği çift satır boşluğuna göre ayırarak tarif listesi oluştur
            recipes = content.split("\n\n")
            recipe_dict = {}

            # Her bir tarif metni üzerinde döngü başlat
            for recipe in recipes:
                # Satır başı ve sonundaki boşlukları temizle ve satırlara ayır
                lines = recipe.strip().split("\n")

                # Bir tarifin en az başlık ve bir içerik satırından oluştuğunu kontrol et
                if len(lines) >= 2:
                    # İlk satırı tarifin adı olarak al
                    recipe_name = lines[0].strip()
                    # Geri kalan satırları içerik olarak al (malzemeler ve talimatlar)
                    recipe_content = [line.strip() for line in lines[1:]]

                    # Ana sözlüğe tarifi ekle
                    # Anahtar: tarifin adı, Değer: tarifin içeriği (liste)
                    recipe_dict[recipe_name] = recipe_content

            return recipe_dict

    except FileNotFoundError:
        print(f"Hata: '{file_path}' adında bir dosya bulunamadı.")
        return None  # Hata durumunda None döndür

load_recipes("../txt_csv_vs/sample.txt")