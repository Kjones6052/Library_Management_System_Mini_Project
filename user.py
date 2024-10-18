
from library import Library
# Code for class: User

class User: 
    def __init__(self, name, library_id, borrowed_books: list, reserved_books: list):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = borrowed_books
        self.reserved_books = reserved_books

    def __repr__(self):
        return f"User Name: {self.get_user_name()}\nLibrary ID #: {self.get_user_id}\nBorrowed Books: {self.borrowed_books}\nReserved Books: {self.reserved_books}"

    def get_user_name(self):
        return self.__name
    
    def get_user_id(self):
        return self.__library_id
    
    def add_user(self, user: object): # Method to add a new user
        try:
            if user in Library.users:
                print(f"{self.get_user_name()} is already on file.")
            else:
                Library.users.append(user)
                print(f"New User Added: {self.get_user_name()}")
        except Exception as e:
            print(e)

    def view_details(self, user: object): # Method to view details of an user
        try: 
            if user in Library.users:
                print(user)
            else:
                print(f"User not found on file.")
        except Exception as e:
            print(e)

    def view_users(self): # Method to view a list of all authors
        print("List of Users:")
        for user in Library.users:
            print(user.get_user_name())

    def borrow_book(self, book: object, user: object):
        try:
            if user in Library.users:
                self.borrowed_books.append(book)
            else:
                print("User not found.")
        except Exception as e:
            print(e)

    def return_book(self, book: object, user: object):
        try:
            if user in Library.users:
                self.borrowed_books.remove(book)
            else:
                print("User not found.")
        except Exception as e:
            print(e)

    def reserve_book(self, book: object, user: object):
        try:
            if user in Library.users.keys():
                self.reserved_books.append(book)
            else:
                print("User not found.")
        except Exception as e:
            print(e)
