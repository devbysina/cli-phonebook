from phonebook import PhoneBook

def main():
    phonebook = PhoneBook()
    print('Welcome to CLI Phonebook!')
    phonebook.load_contacts()

if __name__ == "__main__":
    main()
