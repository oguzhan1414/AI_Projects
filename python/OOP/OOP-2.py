## KÜTÜPHANE YÖNETİM SİSTEMİ

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                book.display_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Book '{title}' has been borrowed. Enjoy reading!")
                return
        print(f"Book '{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' is not in the library or wasn't borrowed.")


# Ana Menü
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ").strip()
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ").strip()
        library.return_book(title)
    elif choice == "5":
        print("Exiting the library management system.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
