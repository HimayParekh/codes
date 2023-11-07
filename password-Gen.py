import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        print("Cannot generate a password with no character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")

    while True:
        length = input("Enter the desired password length (default is 12): ")
        include_digits = input("Include digits? (yes/no, default is yes): ").lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no, default is yes): ").lower() == "yes"

        try:
            length = int(length) if length else 12
        except ValueError:
            print("Invalid length. Using the default length of 12.")

        password = generate_password(length, include_digits, include_special_chars)
        print(f"Generated password: {password}")

        another = input("Generate another password? (yes/no): ").lower()
        if another != "yes":
            break

    print("Thank you for using the Password Generator!")
