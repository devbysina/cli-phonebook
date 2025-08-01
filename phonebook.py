import json
import os
from utils import validate_email, validate_phone

DATA_FILE = "data/contacts.json"

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.phone == other.phone
        return False

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'])


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            self.contacts = [Contact.from_dict(contact) for contact in data]

    def add_contact(self, name, phone, email):
        if not validate_phone(phone):
            return 'error', 'Invalid phone number format.'

        if not validate_email(email):
            return 'error', 'Invalid email format.'

        phone = phone[-10:]  # normalization
        contact = Contact(name, phone, email)

        if contact in self.contacts:
            return 'error', 'Contact with this phone number already exists.'

        self.contacts.append(contact)
        self.save_contacts()
        return 'success', f'Contact for {contact.name} added.'

    def list_contacts(self):
        if not self.contacts:
            return "No contacts found."

        lines = [f"{index}. {contact}" for index, contact in enumerate(self.contacts, start=1)]
        return "\n".join(lines)

    def delete_contact(self, phone):
        if not validate_phone(phone):
            return 'error', 'Invalid phone number format.'

        phone = phone[-10:]  # normalization

        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                self.save_contacts()
                return 'success', f"Contact '{contact.name}' deleted."

        return 'error', 'No contact found with this phone number.'

    def save_contacts(self):
        with open(DATA_FILE, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
