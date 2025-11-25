"""
print("Welcome to the tip calculator")
hesap = int(input("Total Hesabı Girin"))
bahsis_orani = int(input("How much tip would you like to give 10 ,12 ,15"))
kisi_sayisi = int(input("Kaç kişi bu hesabı paylaşıcak"))

totel_hesap = hesap+(hesap * (bahsis_orani / 100))
kisi_basi_hesap = totel_hesap / kisi_sayisi
print(kisi_basi_hesap)
"""

"""
import random
list = ["taş","kağıt","makas"]
rastgele = random.choice(list)
#s1=random.randint(0,2)  pc = list[s1] şeklinde de üstteki choice gibi de olur
pc = rastgele
print(pc)
kullanici = input("Taş Kağıt Makas tercih yapın").lower()
if(pc == "taş"):
    if(kullanici == "taş"):
        print("Berabere")
    elif(kullanici == "makas"):
        print("PC Kazandı")
    else:
        print("Kullanici kazandı")

elif(pc == "makas"):
    if(kullanici=="taş"):
        print("Kullanici kazandi")
    elif(kullanici == "makas"):
        print("BERABERE")
    else:
        print("PC KAZANDI")
else:
    if(kullanici == "taş"):
        print("PC KAZANDI")
    elif(kullanici=="makas"):
        print("Kullanıcı kazandı")
    else:
        print("BERABERE")
"""
import random

print("Welcome to the PyPassword Generator")

uzunluk = int(input("How many letters would you like in your password? "))
symbol_uzunluk = int(input("How many symbols would you like? "))
number_tane = int(input("How many numbers would you like? "))

numbers = ["1","2","3","4","5","6","7","8","9","0"]
harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sembol = ["#","%","$","_","£"]

password_list = []

# Harf ekleme
for i in range(uzunluk):
    password_list.append(random.choice(harfler))

# Sembol ekleme
for i in range(symbol_uzunluk):
    password_list.append(random.choice(sembol))

# Sayı ekleme
for i in range(number_tane):
    password_list.append(random.choice(numbers))

# Karıştır
random.shuffle(password_list)

# Listeyi stringe çevir
password = "".join(password_list)

print(f"Your password is: {password}")



#maxı bulma örneği for
score = [1,2,3,4,5,6,7]
max_score = 0
for i in score:
    if i > max_score:
        max_score = i

print(max_score)