# This module contains the code for all user interactions
# Import Regex for verification of user input
import re
# Import classes: Book, Author, User
from book import Book
from author import Author
from user import User

def main(): # Print intro and main menu with input to choose action
    intro = "Welcome to the Library Management System!"
    while True:
        print(intro)
        user_input = input("Main Menu:\n1. Book Opertations\n2. Author Operations\n3. User Operations\n4. Exit Application\nPlease enter your option number (1-4): ")
        if user_input == "1": # Create Book Operations Menu
            book_op = input("Book Operations Menu:\n1. Add a New Book\n2. Borrow a Book\n3. Return a Book\n4. Search for a Book\n5. Display All Books\n6. Exit Application\nPlease enter your option number (1-7): ")
            if book_op == "1": # Get details and run add book method (book_title, details)
                book_title = input("Enter the Title of the book: ") 
                book_author = input("Enter the Author of the book: ")
                try:
                    if re.search(r"\d", book_author):
                        raise ValueError("Digits found in Author Name, no digits allowed in Author Name.")
                    else:
                        book_genre = input("Enter the Genre of the book: ")
                        if re.search(r"\d", book_genre):
                            raise ValueError("Digits found in Book Genre, no digits allowed in Book Genre.")
                        else:
                            pub_date = input("Enter the Publishing Date of the book (using numerical day-month-year xx-xx-xxxx format): ")
                            if re.search(r"\d{2}-\d{2}-\d{4}", pub_date):
                                book_availability = "Available"
                                Book.add_book(book_title, book_title, Book(book_title, book_author, book_genre, pub_date, book_availability))
                            else:
                                ValueError("Incorrect Date Format: please use numbers in the day-month-year format.")
                except ValueError as e:
                    print(e)
            elif book_op == "2": # Get details and run borrow book method (book_title, user)
                book_title = input("Enter the Title of the book: ")
                user_id = input("Enter user ID number: ")
                try:
                    if re.search(r"\d", user_id):
                        Book.borrow_book(book_title, book_title, user_id)
                        User.borrow_book(book_title, book_title, user_id)
                    else:
                        raise ValueError("Error: Please use numerical digits only for User Id Number.")
                except Exception as e:
                    print(e)
            elif book_op == "3": # Get details and run return book method (book_title, user)
                book_title = input("Enter the Title of the book: ")
                user_id = input("Enter user ID number: ")
                try:
                    if re.search(r"\d", user_id):
                        Book.return_book(book_title, book_title, user_id)
                        User.return_book(book_title, book_title, user_id)
                    else:
                        raise ValueError("Error: Please use numerical digits only for User Id Number.")
                except Exception as e:
                    print(e)
            elif book_op == "4": # Get details and run search book method (book_title)
                book_title = input("Enter the Title of the book: ")
                Book.search_book(book_title, book_title)
            elif book_op == "5": # Get run display books method
                Book.view_books(book_title)
            elif book_op == "6": # Run shut down procedure or delete
                break
            else:
                print("Invalid option, please enter a digit 1-7.")
        elif user_input == "2": # Create Author Operations Menu
            author_op = input("Author Operations Menu:\n1. Add a New Author\n2. View Author Details\n3. Display All Authors\n4. Exit Application\nPlease enter your option number (1-4): ")
            if author_op == "1": # Get details and run add author method (name, biography)
                author_name = input("Enter Author's Name: ") 
                author_bio = input("Enter Author's Biography: ")
                if re.search(r"\d", author_name):
                    print("Error: Digits found in Author Name, please try again.")
                else:
                    Author.add_author(author_name, author_name, author_bio)
            elif author_op == "2": # Get details and run view details method (name)
                author_name = input("Enter Author's Name: ")
                if re.search(r"\d", author_name):
                    print("Error: Digits found in Author Name, please try again.")
                else:
                    Author.view_details(author_name, author_name)
            elif author_op == "3": # Get view authors method
                Author.view_authors(author_name)
            elif author_op == "4": # Run shut down procedure or delete
                break
            else:
                print("Invalid option, please enter a digit 1-4.")
        elif user_input == "3": # Create User Operations Menu
            user_op = input("User Operations Menu:\n1. Add a New User\n2. View User Details\n3. Display All Users\n4. Exit Application\nPlease enter your option number (1-4): ")
            if user_op == "1": # Get details and run add user method (name, library_id)
                user_name = input("Enter name: ") 
                library_id = input("Enter Library ID Number: ")
                try:
                    if re.search(r"\d", user_name):
                        raise ValueError("Error: Digits found in User Name, please use only letters and spaces.")
                    else:    
                        if re.search(r"\d", library_id):
                            User.add_user(user_name, user_name, library_id)
                        else:
                            raise ValueError("Error: Invalid Library ID Number, please use only numerical digits.")
                except Exception as e:
                    print(e)
            elif user_op == "2": # Get details and run view details method (name)
                user_name = input("Enter name: ")
                try:
                    if re.search(r"\d", user_name):
                        raise ValueError
                    else:
                        User.view_details(user_name, user_name)
                except ValueError:
                    print("Error: Digits found in User Name, please use only letters and spaces.")
            elif user_op == "3": # Get view users method
                User.view_users(user_name)
            elif user_op == "4": # Run shut down procedure or delete
                break
            else:
                print("Invalid option, please enter a digit 1-4.")
        elif user_input == "4": # Choice: break to end program or add shut down procedure that copies all dicts to txt files
            break
        else:
            print("Invalid option, please enter a digit 1-4.")

if __name__ == "__main__":
    main()