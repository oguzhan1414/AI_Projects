#statick yöntem ve class yöntem
class Calculator:
    base_value = 100

    @staticmethod
    def add(value1,value2):
        return value1 + value2

    @classmethod
    def multiply_base(cls,multiplier):
        return cls.base_value * multiplier
#Using statick method
print(Calculator.add(4,5))

#using class method
print(Calculator.multiply_base(2))

class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 10
Counter.increment()
print(Counter.count)

###ınverntory managmemetn system

# Envanterdeki ürünleri yönetmek için bir sınıf tanımlıyoruz.
class Inventory:
    # Bu bir "sınıf değişkeni" (class variable).
    # Oluşturulan TÜM Inventory nesneleri bu tek değişkeni paylaşır.
    # Mağazadaki toplam ürün sayısını takip eder.
    total_items = 0

    # __init__ metodu, bir nesne oluşturulduğunda otomatik olarak çalışan kurucu metottur.
    def __init__(self, product_name, price, quantity):
        # --- DÜZELTME: 'produc_name' -> 'product_name' olarak düzeltildi. ---
        # Bunlar "örnek değişkenleri" (instance variables).
        # Her bir ürün nesnesinin kendine ait adı, fiyatı ve miktarı olur.
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

        # Yeni bir ürün eklendiğinde, miktar kadar toplam ürün sayısını artır.
        Inventory.total_items += quantity

    # Ürünün detaylarını ekrana yazdıran metot.
    def show_product_details(self):
        print("--- Product Details -----")
        # --- DÜZELTME: 'produc_name' -> 'product_name' olarak düzeltildi. ---
        print(f"Product Name : {self.product_name}")
        print(f"Price: ${self.price}")  # Para birimi simgesi eklendi
        print(f"Quantity: {self.quantity}")

    # Belirtilen miktarda ürün satan metot.
    def sell_product(self, amount):
        # Eğer satılmak istenen miktar, stoktaki miktardan az veya eşitse satışı yap.
        if amount <= self.quantity:
            self.quantity -= amount  # Ürünün kendi stoğunu azalt.
            Inventory.total_items -= amount  # Mağazadaki toplam ürün sayısını da azalt.
            # --- DÜZELTME: 'produc_name' -> 'product_name' olarak düzeltildi. ---
            print(f"{amount} {self.product_name}(s) sold successfully.")
        else:
            # Yeterli stok yoksa uyarı ver.
            print("Insufficient quantity in stock.")

    # @staticmethod, sınıfa veya nesneye bağlı olmayan, bağımsız bir yardımcı fonksiyondur.
    # 'self' veya 'cls' parametresi almaz.
    # Sadece verilen parametrelerle bir işlem yapar.
    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price * (1 - discount_percentage / 100)

    # @classmethod, nesneye değil, doğrudan sınıfın kendisine bağlı bir metottur.
    # 'cls' parametresi ile sınıfın kendisine erişir (örneğin sınıf değişkenlerine).
    @classmethod
    def total_items_report(cls):
        print(f"\nTotal items in inventory: {cls.total_items}")


# Tüm ürün nesnelerini saklayacağımız boş bir liste.
products = []


def add_product():
    print("\n--- Add New Product ---")
    product_name = input("Enter product name: ")
    # --- DÜZELTME: Fiyat, string yerine float (ondalıklı sayı) olarak alınıyor. ---
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    # Yeni ürün için bir Inventory nesnesi oluştur.
    product = Inventory(product_name, price, quantity)
    products.append(product)
    print(f"'{product_name}' added to inventory.")


# --- DÜZELTME: Fonksiyon adı 'view_products' olarak düzeltildi. ---
def view_products():
    print("\n----- Current Inventory -----")
    if not products:
        print("No products in inventory.")
    else:
        for product in products:
            product.show_product_details()


# --- DÜZELTME: Fonksiyon adı 'sell_product_cli' olarak değiştirildi (sınıf metoduyla karışmasın diye). ---
def sell_product_cli():
    print("\n--- Sell Product ---")
    product_name = input("Enter product name to sell: ")
    product_found = False  # Ürünün bulunup bulunmadığını kontrol etmek için bir bayrak

    for product in products:
        # --- DÜZELTME: 'product.product_name' doğru yazımla kullanıldı. ---
        # --- DÜZELTME: if satırının sonuna ':' eklendi. ---
        if product.product_name.lower() == product_name.lower():  # Büyük/küçük harf duyarsız arama
            product_found = True
            try:
                amount = int(input(f"Enter amount of '{product_name}' to sell: "))
                product.sell_product(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
            break  # Ürün bulunduktan sonra döngüyü kır.

    # --- DÜZELTME: "Bulunamadı" mesajı döngü bittikten sonra kontrol ediliyor. ---
    if not product_found:
        print("Product not found in inventory.")


# --- DÜZELTME: Fonksiyon tamamen yeniden yazılarak mantık hatası giderildi. ---
def discount_price():
    print("\n--- Calculate Discount ---")
    try:
        # Fonksiyon artık hem orijinal fiyatı hem de indirim oranını istiyor.
        original_price = float(input("Enter original price: "))
        discount_percentage = float(input("Enter discount percentage (e.g., 15): "))

        # Static metot doğru şekilde iki parametre ile çağrılıyor.
        discounted_price = Inventory.calculate_discount(original_price, discount_percentage)
        print(f"Discounted Price: ${discounted_price:.2f}")  # Sonuç formatlandı.
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Ana program döngüsü
while True:
    print("\n===== Inventory Menu =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Sell Product")
    print("4. Calculate Discount")
    print("5. Total Items Report")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_product()
    elif choice == "2":
        # --- DÜZELTME: Fonksiyon adı düzeltildi. ---
        view_products()
    elif choice == "3":
        # --- DÜZELTME: Fonksiyon adı düzeltildi. ---
        sell_product_cli()
    elif choice == "4":
        discount_price()
    elif choice == "5":
        Inventory.total_items_report()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please Try Again.")