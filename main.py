# This is the main script for the Library Management System 
# Import as needed

# Main Function
def main():
    intro = "Welcome to the Library Management System!"
    while True:
        print(intro)
        prompt = input("Menu Options:\n1. Book Operations\n2. Author Operations\n3. User Operations\n4. Quit\nPlease enter your choice (1-4): ")
        try:
            if prompt == '1':
                import book_ops
                book_ops.display_book_menu()
            elif prompt == '2':
                # Go to Author Operations
                pass
            elif prompt == '3':
                # Go to User Operations
                pass
            elif prompt == '4':
                break
        except:
            print("Invalid choice, please enter a number 1-4.")
    

# Run Main Function
if __name__ == "__main__":
    main()