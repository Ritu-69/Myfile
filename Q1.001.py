import random
import string

def generate_password(length):
    # Combine lowercase, uppercase letters, and numbers
    characters = string.ascii_letters + string.digits
    
    # Randomly pick characters and join them together
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program execution
try:
    user_length = int(input("Enter desired password length (e.g., 12): "))
    if user_length < 4:
        print("For security, please choose a length of 4 or more.")
    else:
        new_password = generate_password(user_length)
        print(f"Your generated password is: {new_password}")
except ValueError:
    print("Please enter a valid whole number.")
