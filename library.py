# Import as needed
from book import Book # set avail, set borrow, set reserve
from user import User # all

# Code for class: Library

class Library:
    def __init__(self):
        self.library = [] # List to hold book objects with: title, author, genre, pub date, availability 
        self.reservations = {}  # Dictionary to hold reserved books and user names
        self.users = [] # List to hold user objects with: name, library_id, borrowed_books, reserved_books
        self.authors = [] # List to hold author objects with: name, biograpahy

    def add_book(self, book: object): # Method to add a new book
        self.library.append(book) # add book to library
        print(f"{book.get_title()} has been added to the library.")

    def borrow_book(self, book: object, user: object): # Method to borrow a book
        try:
            book.set_borrowed()
            user.borrowed_books.append(book)
            print(f"{book.get_title()} has been borrowed by {user.get_user_name()}.")
        except Exception as e:
            print(e)

    def return_book(self, book: object, user: object): # Method to return a book
        try:
            user.borrowed_books.remove(book)
            book.set_available()
            print(f"{book.get_title()} has been returned by {user.get_user_name()}.")
        except Exception as e:
            print(e)

    def view_books(self): # Method to print a list of book titles
        for book in self.library:
            print(book)

    def add_author(self, author: object): # Method to add a new author
        try:
            self.authors.append(author)
            print(f"New Author Added: {author.get_author_name()}")
        except Exception as e:
            print(e)

    def view_authors(self): # Method to view a list of all authors
        for author in self.authors:
            print(author.get_author_name())

    def add_user(self, user: object): # Method to add a new user
        try:
            self.users.append(user)
            print(f"New User Added: {user.get_user_name()}")
        except Exception as e:
            print(e)

    def view_users(self): # Method to view a list of all authors
        print("List of Users:")
        for user in self.users:
            print(user.get_user_name())
    
