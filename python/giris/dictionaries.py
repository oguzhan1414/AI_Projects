"""
contact = {
    "name" : "John Doe",
    "phone" : "123-456"
}
#print(contact["name"])
#print(contact.get("phone"))
contact["phone"] = "567-891"
#print(contact["phone"])
contact["adress"] = "Bolu Merkez"
#print(contact.get("adress"))
del contact["adress"]
#print(contact.get("adress"))

for key,value in contact.items():# items() => sözlükteki hem anahtarları hem değerleri döndürür (key, value)
    print(key,value)
if "email" in contact: # in => bir anahtarın sözlükte olup olmadığını kontrol eder
    print("E-mail var")
else:
    print("hayır yok")

"""

# Kitap Ödevi: Basit bir Contact Book (Kişi Defteri) uygulaması

# Boş bir sözlük oluşturuyoruz, burada tüm kişiler saklanacak
contacts = {}

# Menü fonksiyonu: kullanıcıya yapılabilecek işlemleri gösterir
def show_menu():
    print("1. Add Contact")     # Kişi ekleme
    print("2. View Contacts")   # Kişileri görüntüleme
    print("3. Search Contact")  # Kişi arama
    print("4. Edit Contact")    # Kişi düzenleme
    print("5. Delete Contact")  # Kişi silme
    print("6. Exit")            # Çıkış

# Kişi ekleme fonksiyonu
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    # contacts sözlüğüne isim anahtar olarak eklenir ve phone & email değer olarak saklanır
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} has been added to your contact book successfully")

# Kişileri görüntüleme
def view_contacts():
    if contacts:  # Sözlük boş değilse
        print("--------Contact List --------")
        # items() => hem anahtar hem değer üzerinde döngü kurmamızı sağlar
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("Your contact book is empty")

# Kişi arama
def search_contact():
    name = input("Enter the name of the contact you want to search: ")
    # in => anahtarın sözlükte olup olmadığını kontrol eder
    if name in contacts:
        print("-----Contact Details------")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found in your contact book")

# Kişi düzenleme
def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:  # Eğer kişi varsa düzenleme yapılır
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} has been updated successfully")
    else:
        print(f"Contact {name} not found in your contact book")

# Kişi silme
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:  # Eğer kişi varsa silinir
        del contacts[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} not found in your contact book")

# Main program loop: kullanıcı çıkana kadar çalışır
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using the Contact Book")
        break
    else:
        print("Invalid choice! Please select a valid option 1-6")
