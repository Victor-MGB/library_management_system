# 
Project: Library Management System
Objective: Create a Python-based library management system that allows users to manage a library's book inventory. The system should include features such as:

Adding new books
Searching for books by title or author
Borrowing and returning books
Keeping track of borrowed books
Components of the Library Management System
Books Inventory: A dictionary will store the books available in the library, where each book will have details like title, author, and availability status.
Borrowed Books: A dictionary to track borrowed books, with user details and the borrowed book details.
Functions:
Add Book: Add new books to the library inventory.
Search Book: Search for books by title or author.
Borrow Book: Borrow a book if it is available.
Return Book: Return a borrowed book and update its availability status.
View Borrowed Books: Display the list of books currently borrowed and by whom.
Main Menu: Provide options for the user to interact with the library system.


Explanation of the Code
Books Dictionary: Stores the books available in the library. Each book is assigned a unique ID and contains information like title, author, and availability status.
Borrowed Books Dictionary: Tracks the books that have been borrowed, along with the borrower's name.
Functions:
add_book(): Adds new books to the library inventory.
search_book(): Allows searching for books by title or author, displaying the results with availability status.
borrow_book(): Lets a user borrow a book if it is available.
return_book(): Allows a user to return a borrowed book, updating the inventory.
view_borrowed_books(): Displays a list of all borrowed books and the corresponding borrowers.
main_menu(): Provides an interface for the user to navigate through the library management system.
Key Concepts and Techniques
Dictionaries: Used for storing and managing the book inventory and tracking borrowed books.
Lists: Employed within the borrowed books dictionary to handle multiple borrowed books per user.
Basic I/O: Using input() and print() for user interaction and control flow.
Control Flow: Using loops and conditionals to manage the library system's operations.