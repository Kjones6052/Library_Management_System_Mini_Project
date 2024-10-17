import re

user_op = input("User Operations Menu:\n1. Add a New User\n2. View User Details\n3. Display All Users\n4. Exit Application\nPlease enter your option number (1-4): ")
if user_op == "1": # Get details and run add user method (name, library_id)
    user_name = input("Enter name: ") 
    library_id = input("Enter Library ID Number: ")
    try:
        if re.search(r"\d", user_name):
            raise Exception("bad user name")
        else:
            if re.search(r"\d", library_id):
                print("It worked")
            else:
                print("Bad ID")
    except Exception as e:
        print(e)