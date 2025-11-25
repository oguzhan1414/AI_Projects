"""
'w'	Write (Yazma): Dosyayı yazma amacıyla açar. Dikkat: Eğer dosya zaten mevcutsa, içeriğinin tamamını siler ve üzerine yazar.
 Dosya mevcut değilse, yeni bir dosya oluşturur.
'a'	Append (Ekleme): Dosyayı ekleme amacıyla açar. Eğer dosya mevcutsa, imleci dosyanın sonuna konumlandırır ve yeni veriyi
mevcut verinin sonuna ekler. Dosyanın eski içeriği silinmez. Dosya mevcut değilse, yeni bir dosya oluşturur.

Özellikle Türkçe karakterler (ğ, ü, ş, ı, ö, ç) içeren metinleri dosyaya yazarken open() fonksiyonuna encoding="utf-8"
"""

#with open("yeni.txt","w") as file:
    #file.write("Day1: Today I learned about writing files in Python")



#with open("yeni.txt","a") as file:
    #file.write("\n Day2: Today I built a journal logger today")

##Günlük Kaydedici App

#Step 1 : Günlük Dosyayı tanımlamak
JOURNAL_FILE = 'daily_journal.txt'

#Step 2 : Giriş isteme
def add_entry():
    entry = input("Write your journal entry")
    with open(JOURNAL_FILE,'a') as file:
        file.write(entry + "\n")
    print("Entry added succesfully!")

#step 3 : bütün girişler

def view_entries():
    try:
        with open(JOURNAL_FILE,"r") as file:
            content = file.read()
            if content:
                print("\n ----- Your Journal Entreis")
                print(content)
            else:
                print("No entries found")
    except FileNotFoundError:
        print("File Not Found Error")

#step 4 anahtar kelime ile arama yapma
def search_entries():
    keyword = input("Aradaığınız kelimeyi yazınız").lower()
    try:
        with open(JOURNAL_FILE , "r") as file:
            content = file.readlines()
            found = False
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
                if not found:
                    print("No matching entries found")
    except FileNotFoundError:
        print("File Not Found Error")

#5 menü

def show_menu():
    print("\n----Dailly Journal Logger -----")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4 Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4)").strip()
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        print("Exiting the program")
        break
    else:
        print("Adm akıllı bir şey gir dostum")


"""
split(): Metni Parçalara Ayırır
Bir metni, belirlediğiniz bir ayıraca göre parçalara ayırır ve sonuç olarak bir liste döndürür. Eğer bir ayıraç belirtmezseniz, varsayılan olarak boşluklara göre ayırır.

Ne İşe Yarar? Bir cümleyi kelimelere, virgülle ayrılmış bir veriyi elemanlara bölmek için kullanılır.

Örnek 1 (Boşluğa göre ayırma):

Python

cumle = "Python öğrenmek çok kolay"

# Cümleyi boşluklardan ayırarak kelimelerin listesini oluştur
kelimeler = cumle.split()

print(kelimeler)
Çıktı:

['Python', 'öğrenmek', 'çok', 'kolay']"""