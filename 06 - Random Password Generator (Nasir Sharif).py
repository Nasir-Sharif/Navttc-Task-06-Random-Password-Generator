import random
import string

def generate_password(length):
    # Define the characters to use in the password
    length=int (length)
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine all the characters
    all_chars = letters + digits + special_chars

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Set the desired password length

password_length=  input("Enter the Password length you want to generate :: \n" )

# Generate and print the password
print("Your strong Generated Password is as")
print("Generated Password:", generate_password(password_length))
