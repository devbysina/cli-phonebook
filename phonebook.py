import json
import os
from utils import validate_email, validate_phone

DATA_FILE = "data/contacts.json"

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

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

    def save_contacts(self):
        with open(DATA_FILE, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
