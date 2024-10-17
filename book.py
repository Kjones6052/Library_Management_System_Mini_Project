
import variables
from user import User
# Code for class: Book

class Book:
    def __init__(self, title, author, genre, publish_date, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.publish_date = publish_date
        self.availability = availability
        #self.library = {}

    # def __repr__(self):
    #     return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Publishing Date: {self.publish_date}, Available: {self.availability}"

    # def get_title(self):
    #     return self.__title
    
    # def get_author(self):
    #     return self.__author
    
    # def get_genre(self):
    #     return self.__genre
    
    # def get_pub_date(self):
    #     return self.__publish_date
    
    # def get_availability(self):
    #     return self.__availability
    
    def set_available(self):
        try:
            self.__availability == "Available"
        except Exception as e:
            print(e)

    def set_borrowed(self):
        try:
            self.__availability == "Borrowed"
        except Exception as e:
            print(e)

    def set_reserved(self):
        try:
            self.__availability == "Reserved"
        except Exception as e:
            print(e)

    def add_book(self, book_title, details): # Method to add a new book
        try:
            if book_title in variables.library.keys():
                print(f"{book_title} is already in the library.")
            else:
                variables.library[book_title] = details
                print(f"{book_title} has been added to the library.")
        except Exception as e:
            print(e)

    def borrow_book(self, book_title, user): # Method to borrow a book
        try:
            if book_title in variables.library.keys():
                self.set_borrowed()
                print(f"{book_title} has been borrowed by {user}.")
            else:
                print(f"{book_title} not found in library.")
        except Exception as e:
            print(e)

    def return_book(self, book_title, user): # Method to return a book
        try:
            if book_title in variables.library.keys():
                User.return_book(user, book_title)
                self.set_available()
                print(f"{book_title} has been returned by {user}.")
            else:
                print(f"{book_title} not found in library.")
        except Exception as e:
            print(e)

    def search_book(self, book_title): # Method to search for a book by name and return its details
        #found = False
        print(f"Locating {book_title}....")
        # try:
        if book_title in variables.library.keys():
            print(f"{book_title} found....")
            print(variables.library[book_title][book_title])
        else:
            print("Error: Book not found in library.")        
        # except Exception as e:
        #     print(e)

    def view_books(self): # Method to print a list of book titles
        for book in variables.library.keys():
            print(book)

    def reserve_book(self, book_title, user): # Method to reserve a borrowed book, optional
        try:
            if book_title in variables.library.keys():
                User.return_book(user, book_title)
                self.set_reserved()
                print(f"{book_title} has been reserved by {user}.")
            else:
                print(f"{book_title} not found in library.")
        except Exception as e:
            print(e)
    