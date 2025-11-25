#tuple(demetler) : değişmez veri yapısıdır bir şey eklenemez vs vs vs 1 kez oluşturulur ve öylece kalır
#set : tekrar oluşturulur değiştirilir ama 1 şetden tek 1 tane olur
my_tuple = (1,2,3)
fruits = ("apple","banana","cherry")
print(fruits[1])

my_Set = {1,2,3}
set_a = {"a","b","c"}
set_b = {"a","b"}
print(set_a | set_b) #birleşim
print(set_a & set_b)  # kesişim
print(set_a - set_b) #çıkarma


# Malzeme Kontrol Uygulaması

# Adım 1: Tarifteki malzemeleri tanımla
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

# Adım 2: Kullanıcıdan mevcut malzemeleri al
user_input = input("Sahip olduğunuz malzemeleri girin (virgülle ayırarak): ")
user_ingredients = set(user_input.split(", "))

# Adım 3: Malzemeleri Karşılaştır
# Eksik malzemeleri bul (tarifte olup kullanıcıda olmayanlar)
missing_ingredients = recipe_ingredients - user_ingredients
# Fazla malzemeleri bul (kullanıcıda olup tarifte olmayanlar)
extra_ingredients = user_ingredients - recipe_ingredients

# Adım 4: Sonuçları Göster
print("\n--- Malzeme Kontrol Sonuçları ---")

# Eksik malzemeleri kontrol et ve göster
if missing_ingredients:
    print(f"Eksik malzemeleriniz: {', '.join(missing_ingredients)}")
else:
    print("Tüm gerekli malzemelere sahipsiniz.")

# Fazla malzemeleri kontrol et ve göster
if extra_ingredients:
    print(f"Fazla malzemeleriniz: {', '.join(extra_ingredients)}")
else:
    print("Fazla malzemeniz bulunmuyor.")