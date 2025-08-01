from phonebook import PhoneBook

def main():
    phonebook = PhoneBook()
    phonebook.load_contacts()
    print('Welcome to CLI Phonebook!')
    while True:
        print('1. Add a new contact')
        print('2. Show all contacts')
        print('3. Delete a contact')
        print('4. Edit a contact')
        print('5. Sort contacts by name (ascending or descending)')
        print('6. Exit the phonebook')
        choice = input('Choose: ').strip()
        match choice:
            case '1':
                name = input('Name: ').strip()
                phone = input('Phone: ').strip()
                email = input('Email: ').strip()
                status, message = phonebook.add_contact(name, phone, email)
                print(f'[{status.upper()}] {message}')
            case '2':
                print(phonebook.list_contacts())
            case '3':
                phone = input('Enter phone number to delete: ').strip()
                status, message = phonebook.delete_contact(phone)
                print(f'[{status.upper()}] {message}')
            case "4":
                phone = input('Enter phone number of contact to edit: ').strip()
                print("Leave a field empty if you don't want to change it.")
                new_name = input('New name: ').strip()
                new_phone = input('New phone: ').strip()
                new_email = input('New email: ').strip()
                status, message = phonebook.edit_contact(phone, new_name, new_phone, new_email)
                print(f'[{status.upper()}] {message}')
            case '5':
                order = input('Sort order (A)scending / (D)escending: ').strip().lower()
                reverse = True if order == 'd' else False
                status, message = phonebook.sort_contacts(reverse=reverse)
                print(f'[{status.upper()}] {message}')
            case '6':
                break
            case _:
                print('Sorry, we could not recognize your input. Please try again.')

if __name__ == "__main__":
    main()
