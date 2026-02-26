import json

FILE_NAME = "library_data.json"

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_books(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "issued": False
        }

        self.save_books()
        print("✅ Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book_id, details in self.books.items():
            status = "Issued" if details["issued"] else "Available"
            print(f"\nBook ID: {book_id}")
            print(f"Title: {details['title']}")
            print(f"Author: {details['author']}")
            print(f"Status: {status}")
            print("----------------------")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        if book_id in self.books and not self.books[book_id]["issued"]:
            self.books[book_id]["issued"] = True
            self.save_books()
            print("📕 Book issued successfully!")
        else:
            print("❌ Book not available or invalid ID")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        if book_id in self.books and self.books[book_id]["issued"]:
            self.books[book_id]["issued"] = False
            self.save_books()
            print("📗 Book returned successfully!")
        else:
            print("❌ Invalid Book ID or book was not issued")


def main():
    library = Library()

    while True:
        print("\n📚 Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()