from phonebook import PhoneBook

def main():
    phonebook = PhoneBook()
    phonebook.load_contacts()
    print('Welcome to CLI Phonebook!')
    while True:
        print('1. Add a new contact')
        print('2. Show all contacts')
        print('3. Delete a contact')
        print('4. Exit the phonebook')
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
            case '4':
                break

if __name__ == "__main__":
    main()
