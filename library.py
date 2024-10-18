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
        print(f"{Book.get_title()} has been added to the library.")

    def borrow_book(self, book: object, user: object): # Method to borrow a book
        try:
            if book in self.library:
                Book.set_borrowed()
                User.borrow_book(book, user)
                print(f"{Book.get_title()} has been borrowed by {user.get_user_name()}.")
            else:
                print("Book not found in library.")
        except Exception as e:
            print(e)

    def return_book(self, book: object, user: object): # Method to return a book
        try:
            if book in self.library:
                User.return_book(book, user)
                Book.set_available()
                print(f"{book.get_title()} has been returned by {user}.")
            else:
                print("Book not found in library.")
        except Exception as e:
            print(e)

    # def search_book(self, book_title): # Method to search for a book by name and return its details
    #     # found = False
    #     print(f"Locating {book_title}....")
    #     # try:
    #     if book_title in self.library.keys():
    #         print(f"{book_title} found....")
    #         print(self.library[book_title][book_title])
    #     else:
    #         print("Error: Book not found in library.")        
    #     # except Exception as e:
    #     #     print(e)

    def view_books(self): # Method to print a list of book titles
        for book in self.library:
            print(book.get_title())

    def reserve_book(self, book: object, user: object): # Method to reserve a borrowed book, optional
        try:
            if book in self.library:
                User.reserve_book(book, user)
                self.set_reserved()
                self.reservations[book] = user
                print(f"{book.get_title()} has been reserved by {user.get_user_name()}.")
            else:
                print("Book not found in library.")
        except Exception as e:
            print(e)

    def add_author(self, author: object): # Method to add a new author
        try:
            if author in Library.authors:
                print(f"{author.get_author_name()} is already on file.")
            else:
                Library.authors.append(author)
                print(f"New Author Adde: {author.get_author_name()}")
        except Exception as e:
            print(e)

    def view_details(self, author: object): # Method to view details of an author
        try:
            if author in Library.authors:
                print(author)
            else:
                print(f"Author: {author.get_author_name()} not found on file.")
        except Exception as e:
            print(e)

    def view_authors(self): # Method to view a list of all authors
        for author in Library.authors.keys():
            print(author)
    
    def open_library(self):
        try:
            with open('books.txt', 'r') as file1:
                pass
            with open('books.txt', 'r') as file2:
                pass
            with open('books.txt', 'r') as file3:
                pass
            with open('books.txt', 'r') as file4:
                pass
        except Exception as e:
            print(f"Error: {e}")

    def close_library(self):
        try:
            with open('books.txt', 'w') as file1:
                for book in self.library:
                    file1.write(book)
            with open('authors.txt', 'w') as file2:
                for author in self.authors:
                    file2.write(author)
            with open('users.txt', 'w') as file3:
                for user in self.users:
                    file3.write(user)
            with open('reservations.txt', 'w') as file4:
                for book, user in self.reservations.items():
                    file4.write(book, user)
        except Exception as e:
            print(f"Error: {e}")