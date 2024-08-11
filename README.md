# Navttc-Task-06-Random-Password-Generator
# Password Generator

## Description

This Python script generates a random password of a specified length using a combination of letters, digits, and special characters.

## Code

```python
import random
import string

def generate_password(length):
    # Define the characters to use in the password
    length = int(length)
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine all the characters
    all_chars = letters + digits + special_chars

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Set the desired password length
password_length = input("Enter the Password length you want to generate :: \n")

# Generate and print the password
print("Your strong Generated Password is as")
print("Generated Password:", generate_password(password_length))
```

## Steps

1. **Import Libraries:**
   - Import the `random` and `string` libraries to handle random selections and character sets.

2. **Define `generate_password` Function:**
   - This function takes `length` as an argument, defines the possible characters (letters, digits, and special characters), and generates a random password of the specified length.

3. **Input Password Length:**
   - Prompt the user to enter the desired length for the password.

4. **Generate and Print Password:**
   - Call the `generate_password` function with the input length and print the generated password.

## How to Run

1. **Ensure Python is Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script:**
   - Save the provided Python code into a file named `Random Password Generator.py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `Random Password Generator.py` is saved.
   - Run the script using the following command:
     ```bash
     python Random Password Generator.py
     ```

4. **Enter Password Length:**
   - When prompted, enter the desired length for the password and press Enter.

5. **View Output:**
   - The generated password will be displayed in the terminal or command prompt.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at nasirsharifqasoori786@gmail.com
