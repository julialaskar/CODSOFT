# password_generator.py
import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        chars = string.ascii_letters
    elif complexity == 2:
        chars = string.ascii_letters + string.digits
    elif complexity == 3:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Using default (letters + numbers + symbols).")
        chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be positive.")
            return
            
        print("\nComplexity Levels:")
        print("1. Letters only")
        print("2. Letters and numbers")
        print("3. Letters, numbers, and special characters")
        
        complexity = int(input("Choose complexity level (1-3): "))
        
        password = generate_password(length, complexity)
        print(f"\nGenerated Password: {password}")
        
        strength = "Weak" if complexity == 1 else "Medium" if complexity == 2 else "Strong"
        print(f"Password Strength: {strength}")
        
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
