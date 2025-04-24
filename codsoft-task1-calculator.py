import tkinter as tk
from tkinter import font as tkfont

class GirlyCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌸 Cute Calculator 🌸")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#FFE6F2")  # Light pink background
        
        # Custom cute font
        try:
            self.cute_font = ("Comic Sans MS", 18)  # Playful font
            self.display_font = ("Comic Sans MS", 24, "bold")
        except:
            self.cute_font = ("Arial", 18)  # Fallback font
            self.display_font = ("Arial", 24, "bold")
        
        self.current_input = ""
        self.create_widgets()
    
    def create_widgets(self):
        # Cute display with rounded corners (simulated)
        display_frame = tk.Frame(self.root, bg="#FFB6D9", bd=5, relief=tk.RIDGE)
        display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        self.display_var = tk.StringVar()
        display = tk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            font=self.display_font,
            bg="#FFF0F7",  # Very light pink
            fg="#D63384",  # Dark pink text
            bd=0,
            insertwidth=2,
            width=14,
            justify="right",
            relief=tk.FLAT
        )
        display.pack(ipady=10, fill=tk.BOTH, expand=True)
        
        # Button layout with cute symbols
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('.', 5, 0), ('💖', 5, 3)
        ]
        
        # Create cute buttons
        for (text, row, col) in buttons:
            button = tk.Button(
                self.root, 
                text=text, 
                padx=20, 
                pady=15, 
                font=self.cute_font,
                bg="#FFB6D9",  # Pink button color
                fg="#FFFFFF",  # White text
                activebackground="#FF85C2",  # Darker pink when pressed
                activeforeground="#FFFFFF",
                relief=tk.RAISED,
                bd=3,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            
            # Make C and = buttons special
            if text == 'C':
                button.config(bg="#FF6B9D", fg="#FFFFFF")  # Darker pink
            elif text == '=':
                button.config(bg="#FF4081", fg="#FFFFFF")  # Even darker pink
            elif text == '💖':
                button.config(command=self.show_love)
        
        # Add some decorative elements
        tk.Label(self.root, text="✿ ✿ ✿", bg="#FFE6F2", fg="#FF85C2", 
                font=("Arial", 12)).grid(row=5, column=1, columnspan=2)
        
        # Configure row/column weights
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.current_input = ""
            self.display_var.set("")
        elif char == '=':
            try:
                # Replace cute symbols with actual operators
                expression = self.current_input.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.display_var.set(result)
                self.current_input = result
            except:
                self.display_var.set("Oops! 💔")
                self.current_input = ""
        else:
            self.current_input += str(char)
            self.display_var.set(self.current_input)
    
    def show_love(self):
        self.display_var.set("Love You! 💖")
        self.current_input = ""

def main():
    root = tk.Tk()
    app = GirlyCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
