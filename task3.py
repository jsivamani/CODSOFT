import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."

    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        # Ask if the user wants to generate another password
        next_password = input("Do you want to generate another password? (yes/no): ")
        if next_password.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

