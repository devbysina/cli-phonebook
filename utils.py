import re

def validate_phone(phone):
    pattern = r'^(0|0098|\+98)?9\d{9}$'
    return re.match(pattern, phone)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)
