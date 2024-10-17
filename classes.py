# These are the defined classes with private attributes that are used in the main script

class Author: # Class for Authors
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
        #self.authors = {}

    def get_author_name(self):
        return self.__name
    
    def get_author_biography(self):
        return self.__biography
    
class Book: # Class for Books
    def __init__(self, title, author, genre, publish_date, availability):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publish_date = publish_date
        self.__availability = availability
        #self.library = {}
    
    def get_book_title(self):
        return self.__title
    
    def get_book_author(self):
        return self.__author
    
    def get_book_genre(self):
        return self.__genre
    
    def get_publish_date(self):
        return self.__publish_date
    
    def get_availability(self):
        return self.__availability
    
class User: # Class for Users
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        #self.users = {}

    def get_user_name(self):
        return self.__name

    def get_user_id(self):
        return self.__library_id
