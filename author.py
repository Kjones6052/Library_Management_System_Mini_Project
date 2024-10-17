
import variables
# Code for class: Author

class Author: 
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
        #self.authors = {} # Dictionary to hold author name as keys and author names with biographies as values

    def get_author_name(self):
        return self.__name
    
    def get_author_biography(self):
        return self.__biography
    
    def add_author(self, name, biography): # Method to add a new author
        try:
            if name in variables.authors.keys():
                print(f"{name} is already on file.")
            else:
                variables.authors[name] = biography
                print(f"New Author Adde: {name}")
        except Exception as e:
            print(e)

    def view_details(self, search_name): # Method to view details of an author
        found = False
        try:
            for name, details in variables.authors.items():
                if search_name == name:
                    found = True
                    if found == True:
                        print(f"Author Name: {name}\nBiography: {details}")
                    else:
                        print(f"Author: {name} not found on file.")
        except Exception as e:
            print(e)

    def view_authors(self): # Method to view a list of all authors
        for author in variables.authors.keys():
            print(author)

