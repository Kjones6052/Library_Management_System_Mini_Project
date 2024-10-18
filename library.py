# Import as needed
from book import Book # set avail, set borrow, set reserve
from user import User # all

# Code for class: Library

class Library:
    def __init__(self):
        self.library = {}

    def add_book(self, book_title, details): # Method to add a new book
        try:
            if book_title in self.library.keys():
                print(f"{book_title} is already in the library.")
            else:
                self.library[book_title] = details# add book to library
                print(f"{book_title} has been added to the library.")
        except Exception as e:
            print(e)

    def borrow_book(self, book_title, user): # Method to borrow a book
        try:
            if book_title in self.library.keys():
                Book.set_borrowed()
                User.borrow_book(book_title, user)
                print(f"{book_title} has been borrowed by {user}.")
            else:
                print(f"{book_title} not found in library.")
        except Exception as e:
            print(e)

    def return_book(self, book_title, user): # Method to return a book
        try:
            if book_title in self.library.keys():
                User.return_book(book_title, user)
                Book.set_available()
                print(f"{book_title} has been returned by {user}.")
            else:
                print(f"{book_title} not found in library.")
        except Exception as e:
            print(e)

    def search_book(self, book_title): # Method to search for a book by name and return its details
        # found = False
        print(f"Locating {book_title}....")
        # try:
        if book_title in self.library.keys():
            print(f"{book_title} found....")
            print(self.library[book_title][book_title])
        else:
            print("Error: Book not found in library.")        
        # except Exception as e:
        #     print(e)

    def view_books(self): # Method to print a list of book titles
        for book in self.library.keys():
            print(book)

    def reserve_book(self, book_title, user): # Method to reserve a borrowed book, optional
        try:
            if book_title in self.library.keys():
                User.return_book(user, book_title)
                self.set_reserved()
                print(f"{book_title} has been reserved by {user}.")
            else:
                print(f"{book_title} not found in library.")
        except Exception as e:
            print(e)
    