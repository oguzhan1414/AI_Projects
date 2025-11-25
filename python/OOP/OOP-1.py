class Car:
    def __init__(self,brand,model):  ##init olarak otomatik oluşturur
        self.brand = brand,
        self.model = model

    def display_info(self):
        print(f"This is a {self.brand}: {self.model}.")


#obje oluşturma
my_Car = Car("Tesla","Model 3")
my_Car.display_info()


class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barkin!")

dog1 = Dog("Maviş")
dog1.bark()
dog2= Dog("Gromp")


# Bank Account Simulator

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    # Withdraw Money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Show account details
    def show_details(self):
        print("---- Account Details ----")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")


accounts = {}


def create_account():
    name = input("Enter account holder's name: ").strip()
    initial_deposit = float(input("Enter initial deposit amount: "))
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    print("ACCOUNT CREATED SUCCESSFULLY!")


def access_account():
    name = input("Enter your name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n---- ACCOUNT MENU ----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_details()
            elif choice == '4':
                print("Exiting account menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Account not found. Please create an account first.")

#Main Menu

while True:
    print("----Bank Account Simulator")
    print("1.Create account")
    print("2 acces account")
    print("3 Exit")

    choice = input("ENter your choice (1-3)")
    if choice == '1':
        create_account()
    elif choice == '2':
        access_account()
    elif choice == '3':
        print("Exiting the program Goodbye")
        break
    else:
        print("Invald choice Please seled a valid option")


"""
OOP Nedir? Neden İhtiyacımız Var?
OOP'den önce genellikle Prosedürel Programlama kullanılırdı. Bu yaklaşım, bilgisayara "şunu yap, sonra bunu yap,
 
sonra şunu hesapla" gibi ardışık komutlar vermeye odaklanır. Küçük programlar için harikadır.

Ancak programlar büyüdükçe, yüzlerce hatta binlerce satır kod, birbiriyle ilişkili ama dağınık duran veriler (değişkenler) ve 
bu verileri işleyen fonksiyonlar arasında kaybolmak çok kolaylaşır. Kodun bakımı, geliştirilmesi ve hataların ayıklanması bir kabusa dönüşür.

OOP ise bu kaosa bir çözüm getirir. Programı, birbiriyle etkileşimde olan "nesneler" topluluğu olarak düşünmemizi sağlar. Tıpkı gerçek dünyadaki gibi.

Benzetme: Bir araba düşünelim.

Verileri (Özellikleri): Rengi, markası, modeli, mevcut hızı, benzin seviyesi...

İşlevleri (Metotları): Hızlanması, yavaşlaması, durması, sinyal vermesi...

OOP'de biz bu arabayı bir "nesne" olarak modelleriz. Arabanın rengi ve hızı gibi verileri ile hızlanması ve durması gibi işlevleri birbirinden ayrı düşünmek yerine, hepsini "Araba" adını verdiğimiz tek bir paketin içine koyarız. Bu, kodun daha düzenli, anlaşılır ve yönetilebilir olmasını sağlar.

OOP'nin Temel Kavramları: Sınıf (Class) ve Nesne (Object)
Bu iki kavram, OOP'nin temelidir.

1. Sınıf (Class)
Bir nesnenin nasıl olacağını tanımlayan bir taslak, kalıp veya plandır. Sınıf, o nesnenin hangi özelliklere (attributes) 
ve hangi davranışlara (methods) sahip olacağını belirler.

Araba sınıfı, "Her arabanın bir rengi, markası ve modeli olmalıdır. Her araba hızlanabilir ve yavaşlayabilir." diyen bir teknik çizim gibidir.

2. Nesne (Object)
Sınıf kalıbından üretilmiş somut bir örnektir. Teknik çizimden (sınıftan) üretilmiş gerçek araba (nesne) gibidir.

Kırmızı renkli, BMW marka, X5 model araba bir nesnedir.

Mavi renkli, Mercedes marka, C180 model araba başka bir nesnedir.

İkisi de aynı Araba sınıfından (kalıbından) üretilmiştir ama farklı özelliklere sahiptirler.

Python'da Görelim:

Python

# 1. Sınıfı (kalıbı) tanımlayalım
class Araba:
    # Bu __init__ metodu, bir nesne oluşturulduğunda otomatik olarak çalışan özel bir metottur.
    # Nesnenin başlangıç özelliklerini belirler. "self" kelimesi, nesnenin kendisini temsil eder.
    def __init__(self, renk, marka, model):
        self.renk = renk
        self.marka = marka
        self.model = model
        self.hiz = 0  # Her araba başlangıçta 0 hızla başlasın

    # Sınıfın metotları (davranışları)
    def hizlan(self, miktar):
        self.hiz += miktar
        print(f"{self.marka} hızlandı. Yeni hız: {self.hiz} km/s")

    def yavasla(self, miktar):
        self.hiz -= miktar
        print(f"{self.marka} yavaşladı. Yeni hız: {self.hiz} km/s")

    def bilgi_ver(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Renk: {self.renk}")

# 2. Bu sınıftan (kalıptan) nesneler (somut arabalar) üretelim
araba1 = Araba(renk="Kırmızı", marka="BMW", model="X5")
araba2 = Araba(renk="Mavi", marka="Mercedes", model="C180")

# 3. Nesneleri kullanalım
araba1.bilgi_ver()  # Çıktı: Marka: BMW, Model: X5, Renk: Kırmızı
araba2.bilgi_ver()  # Çıktı: Marka: Mercedes, Model: C180, Renk: Mavi

araba1.hizlan(50)   # Çıktı: BMW hızlandı. Yeni hız: 50 km/s
araba2.hizlan(30)   # Çıktı: Mercedes hızlandı. Yeni hız: 30 km/s
araba1.yavasla(10)  # Çıktı: BMW yavaşladı. Yeni hız: 40 km/s
OOP'nin Dört Temel Prensibi (Sütunu)
OOP'yi güçlü kılan dört ana prensip vardır.

1. Kapsülleme (Encapsulation)
Verileri (özellikleri) ve o veriler üzerinde çalışan metotları (işlevleri) tek bir birim (sınıf) içinde birleştirmek ve
 verilerin dışarıdan doğrudan erişilmesini kısıtlamaktır.

Benzetme: Yine araba örneği. Siz gaz pedalına basarsınız (hizlan metodu), ama motorun içinde pistonların nasıl hareket ettiği, 
yakıtın nasıl püskürtüldüğü gibi karmaşık detayları bilmek zorunda değilsiniz. 
Araba, bu karmaşıklığı kendi içinde "kapsüller" ve size sadece basit bir arayüz (gaz pedalı, direksiyon) sunar.

Neden Önemli? Verinin yanlışlıkla veya kasıtlı olarak bozulmasını engeller. Kodun daha güvenli ve yönetilebilir olmasını sağlar.

Python

class BankaHesabi:
    def __init__(self, sahip, bakiye=0):
        self.sahip = sahip
        # "__" ile başlayan değişkenler "private" (gizli) kabul edilir.
        # Dışarıdan doğrudan erişilmesi istenmez.
        self.__bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.__bakiye} TL")
        else:
            print("Geçersiz miktar.")

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.__bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")

    def bakiye_goster(self):
        return self.__bakiye

hesabim = BankaHesabi("Oğuzhan", 1000)

# Kapsülleme sayesinde bakiyeyi koruyoruz.
hesabim.para_yatir(500)  # Doğru yöntem
hesabim.para_cek(200)    # Doğru yöntem

# Bakiyeyi doğrudan değiştirmeye çalışmak zordur ve istenmez.
# hesabim.__bakiye = 5000 # Bu şekilde doğrudan değiştiremezsiniz! Python buna izin vermez.
print(f"Güncel Bakiye: {hesabim.bakiye_goster()}")
2. Kalıtım (Inheritance)
Bir sınıfın özelliklerini ve metotlarını başka bir sınıfa devretmesidir. Bu, "bir şey, başka bir şeydir" ilişkisini kurar (IS-A relationship).

Benzetme: Kamyon bir Araç'tır. Otomobil de bir Araç'tır. Hem kamyonun hem de otomobilin tekerlekleri, motoru 
ve direksiyonu vardır. Bu ortak özellikleri Araç adında bir temel (parent) sınıfta toplayabiliriz. 
Kamyon ve Otomobil sınıfları bu temel sınıftan kalıtım alarak bu ortak özellikleri miras alır ve kendilerine özgü yeni özellikler 
(örneğin kamyon için dorse_kapasitesi) ekleyebilirler.

Neden Önemli? Kod tekrarını önler ve hiyerarşik bir yapı kurmayı sağlar.

Python

# Temel (Parent) Sınıf
class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def yemek_ye(self):
        print(f"{self.isim} yemek yiyor.")

# Kalıtım alan (Child) Sınıflar
class Kopek(Hayvan): # Parantez içine parent sınıfın adını yazarız
    def havla(self):
        print("Hav hav!")

class Kedi(Hayvan):
    def miyavla(self):
        print("Miyav!")

# Nesneler oluşturalım
rex = Kopek("Rex")
pamuk = Kedi("Pamuk")

rex.yemek_ye() # Bu metot Hayvan sınıfından miras alındı!
rex.havla()    # Bu metot Kopek sınıfının kendi metodu.

pamuk.yemek_ye() # Bu metot da Hayvan sınıfından miras alındı!
pamuk.miyavla()  # Bu metot Kedi sınıfının kendi metodu.
3. Çok Biçimlilik (Polymorphism)
Farklı nesnelerin aynı isimdeki bir metoda farklı şekillerde cevap verebilmesidir. "Çok biçimlilik" kelimesi de buradan gelir.

Benzetme: konus() diye bir komut düşünün. Bu komutu bir insana verdiğinizde "Merhaba" der, bir köpeğe verdiğinizde 
"Hav" der, bir kediye verdiğinizde "Miyav" der. Komut aynı (konus()), ama her nesne kendi doğasına göre farklı bir davranış sergiliyor.

Neden Önemli? Esneklik sağlar. Tek bir arayüz kullanarak farklı tiplerdeki nesnelerle çalışmamıza olanak tanır.

Python

# Bir önceki örnekteki sınıfları kullanalım ama küçük bir ekleme yapalım.
class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        print("Bu hayvanın genel bir sesi var.")

class Kopek(Hayvan):
    def ses_cikar(self): # Parent sınıftaki metodu eziyoruz (Method Overriding)
        print("Hav hav!")

class Kedi(Hayvan):
    def ses_cikar(self): # Parent sınıftaki metodu eziyoruz
        print("Miyav!")

def hayvan_konustur(hayvan_nesnesi):
    hayvan_nesnesi.ses_cikar()

rex = Kopek("Rex")
pamuk = Kedi("Pamuk")
garip_hayvan = Hayvan("Garip")

hayvan_konustur(rex)         # Çıktı: Hav hav!
hayvan_konustur(pamuk)       # Çıktı: Miyav!
hayvan_konustur(garip_hayvan) # Çıktı: Bu hayvanın genel bir sesi var.

# Bakın, `hayvan_konustur` fonksiyonu içine ne tür bir hayvan nesnesi geldiğini bilmiyor.
# Sadece gelen nesnenin `ses_cikar` diye bir metodu olduğunu varsayıyor ve çağırıyor.
# Python, o anda nesnenin tipine göre doğru metodu çalıştırıyor. İşte bu polimorfizmdir!
4. Soyutlama (Abstraction)
Karmaşık iç yapıyı gizleyip kullanıcıya sadece gerekli olan işlevleri sunmaktır.

Benzetme: TV kumandası mükemmel bir soyutlama örneğidir. Siz sadece "ses aç", "kanal değiştir" gibi düğmelere basarsınız. 
Düğmeye bastığınızda arka planda hangi sinyallerin gittiğini, televizyonun içindeki devrelerin bu sinyalleri nasıl işlediğini bilmenize gerek yoktur. 
Kumanda, bu karmaşıklığı soyutlayarak size basit bir arayüz sunar.

Neden Önemli? Programın karmaşıklığını azaltır. Kullanıcının (veya başka bir programcının) sadece bilmesi gereken şeylere odaklanmasını sağlar.

Soyutlama genellikle "soyut sınıflar" (abstract classes) ile uygulanır. Soyut bir sınıf, "bu türdeki her nesnenin mutlaka şu metotlara sahip olması gerekir"
 diyen bir sözleşme gibidir.

Python

from abc import ABC, abstractmethod

# Bu bir sözleşme gibidir. "Her Taşıt'ın bir hareket_et metodu olmalı" der.
class Tasit(ABC):
    @abstractmethod
    def hareket_et(self):
        pass # İçini doldurmuyoruz, çünkü her taşıt farklı hareket eder.

class Araba(Tasit):
    def hareket_et(self): # Sözleşmeye uymak zorunda!
        print("Araba yolda gidiyor.")

class Ucak(Tasit):
    def hareket_et(self): # Sözleşmeye uymak zorunda!
        print("Uçak havada süzülüyor.")

# tasit = Tasit() # HATA! Soyut sınıftan doğrudan nesne üretemezsiniz.
# Bu sizi o sözleşmeyi uygulayan somut sınıflar (Araba, Ucak) üretmeye zorlar.

bmw = Araba()
boeing = Ucak()

bmw.hareket_et()
boeing.hareket_et()
Özetle
Sınıf (Class): Nesnenin planı, taslağı.

Nesne (Object): Plandan üretilmiş somut örnek.

Kapsülleme (Encapsulation): Veri ve metotları bir pakete koyup, veriyi korumak.

Kalıtım (Inheritance): Kod tekrarını önlemek için özellikleri miras almak.

Çok Biçimlilik (Polymorphism): Aynı komuta farklı nesnelerin farklı cevap vermesi.

Soyutlama (Abstraction): Karmaşık detayları gizleyip basit bir arayüz sunmak.

OOP'yi anlamanın en iyi yolu pratik yapmaktır. Gerçek hayattan bir nesne seç (öğrenci, kitap, bilgisayar, banka hesabı vb.) ve 
onu bir sınıf olarak modellemeye çalış. Özellikleri ne olurdu? Metotları ne olurdu? Sonra ondan nesneler üret ve kullan
"""