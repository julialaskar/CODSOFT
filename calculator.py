# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (1-4 or +,-,*,/): ")
            
            if operation in ("1", "+"):
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif operation in ("2", "-"):
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif operation in ("3", "*"):
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif operation in ("4", "/"):
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operation. Please try again.")
                
            another = input("Perform another calculation? (y/n): ").lower()
            if another != 'y':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
