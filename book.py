

# Code for class: Book

class Book:
    def __init__(self, title, author, genre, publish_date, availability):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publish_date = publish_date
        self.__availability = availability

    def __repr__(self):
        return f"Title: {self.get_title()}, Author: {self.get_author()}, Genre: {self.get_genre()}, Publishing Date: {self.get_publish_date()}, Available: {self.get_availability()}"

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_publish_date(self):
        return self.__publish_date
    
    def get_availability(self):
        return self.__availability
    
    def set_available(self):
        self.__availability = "Available"
        
    def set_borrowed(self):
        self.__availability = "Borrowed"

