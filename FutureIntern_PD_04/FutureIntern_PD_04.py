import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Create a pool of characters based on the user's choices
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Ensure the user has selected at least one character type
    if not characters:
        print("Error: You must select at least one character type!")
        return None

    # Generate the random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password
while True:
    # Ask the user for input
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'


    # Generate the password based on user input
    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)

    # Display the password if it was successfully generated
    if password:
        print("Generated password:", password)
    x=input("Are you satisfied with the password[Y/N]: ").lower()
    if x== "y":
        print("Thank you for using the generator!")
        break
    elif x=="n":
        print("Restarting the program...")
        continue
    else:
        print("Invalid choice!!!!")
        break
