import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
