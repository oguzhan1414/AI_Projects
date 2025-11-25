"""
Kalıtım (Inheritance) Nedir?
Kalıtım, nesne yönelimli programlamanın (OOP) temel prensiplerinden biridir. Bir sınıfın (çocuk/alt sınıf - child/subclass) başka bir sınıfın (ebeveyn/üst sınıf - parent/superclass) özelliklerini (metotlar ve nitelikler) miras almasını sağlar.

Neden kullanılır?

Kod Tekrarını Önler: Ortak özellikleri bir üst sınıfta toplayıp, alt sınıflarda tekrar tekrar yazmaktan kurtulursunuz.

Hiyerarşi Oluşturur: Sınıflar arasında mantıksal bir "bir türüdür" (is-a) ilişkisi kurar. Örneğin, "Köpek bir Hayvan'dır."

Bakımı Kolaylaştırır: Ortak bir metotta değişiklik yapmanız gerektiğinde, sadece üst sınıfta değiştirmeniz yeterli olur.


"""

###################
"""
1. Hiyerarşik Kalıtım ve Metot Ezme (Method Overriding)
Bu örnekte, birden fazla sınıf (Dog ve Cat) tek bir üst sınıftan (Animal) miras alıyor.
 Ayrıca alt sınıflar, üst sınıftaki sound metodunu kendilerine özgü şekilde yeniden tanımlıyor. 
Buna Metot Ezme (Method Overriding) denir.
"""
# Üst (Parent) Sınıf Tanımlaması
class Animal:
    # Animal sınıfına ait bir metot
    def sound(self):
        print("Animal makes a sound")

# Animal sınıfından miras alan Alt (Child) Sınıf
class Dog(Animal):
    # Üst sınıftaki 'sound' metodu burada eziliyor (override ediliyor).
    # Artık Dog nesneleri bu metodu çağıracak.
    def sound(self):
        print("Dog sound")

# Animal sınıfından miras alan başka bir Alt (Child) Sınıf
class Cat(Animal):
    # Cat sınıfı da 'sound' metodunu kendine göre eziyor.
    def sound(self):
        print("Cat sound")

# Dog sınıfından bir nesne oluşturuluyor
dog1 = Dog()
# Dog nesnesinin kendi 'sound' metodu çağrılıyor.
dog1.sound()  # Çıktı: Dog sound


############################################

"""
2. Çoklu Kalıtım (Multiple Inheritance)
Bu örnekte, bir sınıf (C) birden fazla üst sınıftan (A ve B) aynı anda miras alıyor. 
Bu sayede C sınıfından oluşturulan nesneler, hem A hem de B sınıfının metotlarına erişebilir.
"""
# Birinci Üst Sınıf
class A:
    def method_A(self):
        print("I am method A")

# İkinci Üst Sınıf
class B:
    def method_B(self):
        print("I am method B")

# 'C' sınıfı, hem 'A' hem de 'B' sınıfından miras alıyor
class C(A, B):
    pass  # C sınıfının kendine ait bir metodu yok ama miras aldığı metotları var

# C sınıfından bir nesne oluşturuluyor
nesne_C = C()
# A sınıfından miras aldığı metodu çağırabiliyor
nesne_C.method_A() # Çıktı: I am method A
# B sınıfından miras aldığı metodu çağırabiliyor
nesne_C.method_B() # Çıktı: I am method B


"""
3. Çok Seviyeli Kalıtım (Multilevel Inheritance)
Bu örnekte kalıtım bir zincir şeklinde gerçekleşir. Child sınıfı Parent sınıfından, Parent sınıfı da grandParent sınıfından miras alır
. Bu sayede en alttaki Child sınıfı, hem Parent hem de grandParent sınıfının özelliklerine erişebilir
"""
# En üstteki sınıf (Büyükbaba)
class grandParent:
    def display(self):
        print("I am a Grand Parent CLASS")

# grandParent sınıfından miras alan sınıf (Ebeveyn)
class Parent(grandParent):
    pass # Kendine ait ek bir özelliği yok, sadece miras alıyor

# Parent sınıfından miras alan sınıf (Çocuk)
class Child(Parent):
    pass # Kendine ait ek bir özelliği yok, sadece miras alıyor

# Child sınıfından bir nesne oluşturuluyor
child = Child()
# Child nesnesi, kendisinde veya Parent sınıfında olmamasına rağmen,
# en üstteki grandParent sınıfındaki 'display' metoduna erişebilir.
child.display() # Çıktı: I am a Grand Parent CLASS


#############################

"""
. Kurucu Metot (__init__) ve super() Kullanımı
Alt sınıfın kendi kurucu metodu (__init__) varsa, üst sınıfın kurucu metodunu otomatik olarak çağırmaz. 
Üst sınıfın kurucu metodunu da çalıştırmak için super().__init__() fonksiyonunu kullanırız. 
Bu, üst sınıfın başlatılması gereken özelliklerinin doğru bir şekilde ayarlanmasını sağlar.
"""

# Üst Sınıf
class Animal:
    # Animal sınıfının kurucu metodu
    def __init__(self):
        print("Animal Created")

# Animal sınıfından miras alan Alt Sınıf
class Dogs(Animal):
    # Dogs sınıfının kendi kurucu metodu
    def __init__(self):
        # super() fonksiyonu ile üst sınıfın (Animal) __init__ metodu çağrılıyor.
        # Bu sayede önce "Animal Created" yazısı ekrana basılır.
        super().__init__()
        # Ardından Dogs sınıfının kendi kodu çalışır.
        print("Dog Created")

# Dogs sınıfından bir nesne oluşturulduğunda, her iki __init__ metodu da çalışır.
dog = Dogs()
# Çıktı:
# Animal Created
# Dog Created


#############EMPLOYE MANAGEMENT SYSTEM

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n--- EMPLOYEE DETAILS ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary:,.2f}")  # Maaşı daha okunaklı formatta yazdıralım

    def calculate_bonus(self):
        return self.salary * 0.1


# Derived class: Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.2


# Derived class: Developer
class Developer(Employee):
    # Değişken adındaki yazım hatası düzeltildi
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        # Değişken adındaki yazım hatası düzeltildi
        self.programming_language = programming_language

    def display_info(self):
        # Hatalı 'return' ifadesi kaldırıldı
        super().display_info()
        # Değişken adındaki yazım hatası düzeltildi
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.15  # Bonus oranı daha mantıklı bir değere çekildi (0.5 -> 0.15)


employees = []


# Fonksiyon adındaki yazım hatası düzeltildi
def add_employee():
    print("\nChoose Employee Type:")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")

    try:
        choice = int(input("Enter your choice: ").strip())

        name = input("Enter Name: ").strip()
        emp_id = input("Enter Employee ID: ").strip()
        salary = float(input("Enter Employee Salary: ").strip())

        if choice == 1:
            employees.append(Employee(name, emp_id, salary))
        elif choice == 2:
            department = input("Enter Department: ").strip()
            employees.append(Manager(name, emp_id, salary, department))
        # EKSİK OLAN DEVELOPER EKLEME KISMI EKLENDİ
        elif choice == 3:
            programming_language = input("Enter Programming Language: ").strip()
            employees.append(Developer(name, emp_id, salary, programming_language))
        else:
            print("Invalid Choice. Please try again.")

        print("Employee added successfully!")

    except ValueError:
        print("Invalid input. Please enter numeric values for choice and salary.")


# Fonksiyon adındaki yazım hatası düzeltildi
def display_all_employees():
    if not employees:
        print("\nNo employees to display.")
        return

    for employee in employees:
        employee.display_info()
        # METOT ADINDAKİ YAZIM HATASI DÜZELTİLDİ
        bonus = employee.calculate_bonus()
        print(f"Bonus: ${bonus:,.2f}")  # Bonus da daha okunaklı formatta
        print("-" * 25)


# Ana Program Döngüsü
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): ").strip())

        if choice == 1:
            # Fonksiyon adındaki yazım hatası düzeltildi
            add_employee()
        elif choice == 2:
            # Fonksiyon adındaki yazım hatası düzeltildi
            display_all_employees()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")
