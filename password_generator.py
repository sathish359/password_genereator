import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special=True):
    characters = ""
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set (uppercase, lowercase, numbers, special) should be included.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special=True):
    passwords = [generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special) for _ in range(num_passwords)]
    return passwords


password_length = int(input("Enter the password length: "))
number_of_passwords = int(input("Enter the number of passwords: "))

passwords = generate_multiple_passwords(number_of_passwords, password_length)
for i, password in enumerate(passwords, start=1):
    print(f"Password {i}: {password}")
