
# Code for class: User

class User: 
    def __init__(self, name, library_id, borrowed_books: list):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = borrowed_books

    def __repr__(self):
        return f"User Name: {self.__name}\nLibrary ID #: {self.__library_id}\nBorrowed Books: {self.borrowed_books}"

    def get_user_name(self):
        return self.__name
    
    def get_user_id(self):
        return self.__library_id
    


