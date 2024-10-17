
import variables
# Code for class: User

class User: 
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = []
        #self.users = {}

    def get_user_name(self):
        return self.__name

    def get_user_id(self):
        return self.__library_id
    
    def add_user(self, name, library_id): # Method to add a new user
        try:
            if name in variables.current_users.keys():
                print(f"{name} is already on file.")
            else:
                variables.current_users[name] = library_id
                print(f"New User Added: {name}")
        except Exception as e:
            print(e)

    def view_details(self, search_name): # Method to view details of an user
        found = False
        try: 
            for name, details in variables.current_users.items():
                if search_name == name:
                    found = True
                    if found == True:
                        print(f"User Name: {name}\nLibrary ID: {details}")
                    else:
                        print(f"User: {name} not found on file.")
        except Exception as e:
            print(e)

    def view_users(self): # Method to view a list of all authors
        for user in variables.current_users.keys():
            print(user)

    def borrow_book(self, title, user):
        try:
            if user in variables.current_users.keys():
                self.borrowed_books.append(title)
            else:
                print("User not found.")
        except Exception as e:
            print(e)

    def return_book(self, title, user):
        try:
            if user in variables.current_users.keys():
                self.borrowed_books.remove(title)
            else:
                print("User not found.")
        except Exception as e:
            print(e)