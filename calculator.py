def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")  # Handle division by zero
    return x / y

from IPython.display import display, Markdown

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def calculate():
    """Enhanced calculator for Jupyter"""
    while True:
        display(Markdown("### Simple Calculator"))
        display(Markdown("**Operations:**  \n1. Addition (+)  \n2. Subtraction (-)  \n3. Multiplication (*)  \n4. Division (/)"))
        
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            op = input("Operation (1-4 or +,-,*,/): ").strip()
            
            if op in ("1", "+"):
                res = add(num1, num2)
                display(Markdown(f"**Result:** {num1} + {num2} = {res}"))
            elif op in ("2", "-"):
                res = subtract(num1, num2)
                display(Markdown(f"**Result:** {num1} - {num2} = {res}"))
            elif op in ("3", "*"):
                res = multiply(num1, num2)
                display(Markdown(f"**Result:** {num1} × {num2} = {res}"))
            elif op in ("4", "/"):
                res = divide(num1, num2)
                display(Markdown(f"**Result:** {num1} ÷ {num2} = {res}"))
            else:
                display(Markdown("⚠️ **Invalid operation**"))
                
            if input("Continue? (y/n): ").lower() != 'y':
                display(Markdown("**Calculator closed**"))
                break
                
        except ValueError:
            display(Markdown("⚠️ **Please enter valid numbers**"))
        except Exception as e:
            display(Markdown(f"⚠️ **Error:** {e}"))

# Run in Jupyter
if __name__ == "__main__":
    calculate()
