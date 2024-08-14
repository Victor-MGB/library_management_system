# Library Inventory
books = {}

# Borrowed Books Record
borrowed_books = {}

def add_book():
    """Adds a new book to the library inventory."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    book_id = len(books) + 1
    books[book_id] = {"title": title, "author": author, "available": True}
    print(f"Book '{title}' by {author} has been added to the inventory.")

def search_book():
    """Search for a book by title or author."""
    search = input("Enter the book title or author to search: ").lower()
    found_books = [book for book in books.values() if search in book["title"].lower() or search in book["author"].lower()]
    
    if found_books:
        print("\n--- Search Results ---")
        for book in found_books:
            status = "Available" if book["available"] else "Not Available"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")
    else:
        print("No books found matching your search.")

def borrow_book():
    """Allows a user to borrow a book if available."""
    book_id = int(input("Enter the book ID to borrow: "))
    if book_id in books and books[book_id]["available"]:
        borrower = input("Enter your name: ")
        books[book_id]["available"] = False
        borrowed_books[borrower] = borrowed_books.get(borrower, []) + [books[book_id]["title"]]
        print(f"You have borrowed '{books[book_id]['title']}'.")
    else:
        print("Book not available for borrowing.")

def return_book():
    """Allows a user to return a borrowed book."""
    borrower = input("Enter your name: ")
    if borrower in borrowed_books:
        book_title = input("Enter the title of the book to return: ")
        if book_title in borrowed_books[borrower]:
            borrowed_books[borrower].remove(book_title)
            book_id = next((key for key, value in books.items() if value["title"] == book_title), None)
            books[book_id]["available"] = True
            print(f"Thank you for returning '{book_title}'.")
            if not borrowed_books[borrower]:
                del borrowed_books[borrower]
        else:
            print("You did not borrow this book.")
    else:
        print("No record of borrowed books found for this user.")

def view_borrowed_books():
    """Displays all borrowed books and the borrowers."""
    if borrowed_books:
        print("\n--- Borrowed Books ---")
        for borrower, books in borrowed_books.items():
            print(f"{borrower} has borrowed: {', '.join(books)}")
    else:
        print("No books are currently borrowed.")

def main_menu():
    """Displays the main menu and processes user input."""
    while True:
        print("\n--- Library Management System Menu ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Borrowed Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_borrowed_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
