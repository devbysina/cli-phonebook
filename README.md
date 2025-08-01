# 📞 CLI Phonebook

A simple command-line phonebook application written in Python.  
It allows users to manage their contacts with basic features like adding, editing, deleting, viewing, and sorting — all stored in a JSON file.

---

## ✨ Features

- ✅ Add new contacts with name, phone number, and email  
- ✅ Validates Iranian phone numbers (supports `09`, `+98`, `0098`)  
- ✅ Validates basic email format  
- ✅ Prevents duplicate phone numbers  
- ✅ Disallows empty names  
- ✅ Edit contact partially or fully (name, phone, email)  
- ✅ Delete contact by phone number  
- ✅ List all saved contacts  
- ✅ Sort contacts by name (ascending or descending)  
- ✅ Data is automatically saved to `contacts.json` after each change  

---

## 🚀 Getting Started

### Requirements

- Python 3.10 or higher (uses `match-case` syntax)

### Run the app

```bash
python main.py
```

You will be greeted with a simple menu to manage your contacts.

---

## 📁 Project Structure

```
cli-phonebook/
├── main.py               # CLI interface
├── phonebook.py          # PhoneBook and Contact classes
├── utils.py              # Validation functions (email & phone)
├── data/
│   └── contacts.json     # Stores contacts in JSON format
├── .gitignore
└── README.md
```

---

## 🧪 Sample Output

```text
--------------------------------------------------
1. Add a new contact
2. Show all contacts
3. Delete a contact
4. Edit a contact
5. Sort contacts by name (ascending or descending)
6. Exit the phonebook
--------------------------------------------------
Choose: 1
Name: Ali
Phone: +989123456789
Email: ali@example.com
--------------------------------------------------
[SUCCESS] Contact for Ali added.
```

---

## 📝 Notes

- Phone numbers are stored in normalized 10-digit format (e.g. `9123456789`)  
- Phone number is used as the unique identifier for contacts  
- Empty names are not accepted  
- Sorting defaults to ascending unless you explicitly choose descending (`D`)  
- All data is saved in `data/contacts.json` and loaded on next run  

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
