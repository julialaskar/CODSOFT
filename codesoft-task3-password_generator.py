import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")  # Slightly taller for status messages
        self.root.resizable(False, False)
        self.root.configure(bg='white')
        
        # Check for pyperclip availability
        self.pyperclip_available = True
        try:
            import pyperclip
            self.pyperclip = pyperclip
        except ImportError:
            self.pyperclip_available = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="PASSWORD GENERATOR", font=('Helvetica', 14, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Length control
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
        self.length_var = tk.IntVar(value=12)
        self.length_slider = ttk.Scale(length_frame, from_=8, to=64, variable=self.length_var, 
                                      command=lambda e: self.update_length_label())
        self.length_slider.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        self.length_display = ttk.Label(length_frame, text="12", width=3)
        self.length_display.pack(side=tk.LEFT)
        
        # Complexity options
        options_frame = ttk.Frame(main_frame)
        options_frame.pack(fill=tk.X, pady=10)
        
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.upper_var).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.lower_var).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.digits_var).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Symbols (!@#...)", variable=self.symbols_var).pack(anchor=tk.W)
        
        # Generate button
        ttk.Button(main_frame, text="Generate Password", command=self.generate_password).pack(pady=15)
        
        # Password display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, font=('Courier', 12), 
                                  state='readonly', justify=tk.CENTER)
        password_entry.pack(fill=tk.X, pady=5)
        
        # Copy button with availability indicator
        copy_frame = ttk.Frame(main_frame)
        copy_frame.pack()
        
        self.copy_button = ttk.Button(copy_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()
        
        # Status label
        self.status_var = tk.StringVar()
        status_label = ttk.Label(main_frame, textvariable=self.status_var, foreground='gray')
        status_label.pack(pady=5)
        
        if not self.pyperclip_available:
            self.status_var.set("Clipboard feature not available - install pyperclip")
            self.copy_button.config(state=tk.DISABLED)
        
    def update_length_label(self):
        self.length_display.config(text=str(int(self.length_var.get())))
        
    def generate_password(self):
        # Check at least one character set is selected
        if not any([self.upper_var.get(), self.lower_var.get(), 
                   self.digits_var.get(), self.symbols_var.get()]):
            messagebox.showwarning("Warning", "Please select at least one character type")
            return
            
        length = int(self.length_var.get())
        char_sets = []
        
        if self.upper_var.get():
            char_sets.append(string.ascii_uppercase)
        if self.lower_var.get():
            char_sets.append(string.ascii_lowercase)
        if self.digits_var.get():
            char_sets.append(string.digits)
        if self.symbols_var.get():
            char_sets.append(string.punctuation)
            
        # Ensure we include at least one character from each selected set
        password = []
        for char_set in char_sets:
            password.append(random.choice(char_set))
            
        # Fill the rest of the password
        all_chars = ''.join(char_sets)
        password.extend(random.choice(all_chars) for _ in range(length - len(password)))
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password)
        self.password_var.set(''.join(password))
        self.status_var.set("Password generated!")
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Warning", "No password generated yet")
            return
            
        if self.pyperclip_available:
            self.pyperclip.copy(password)
            self.status_var.set("Password copied to clipboard!")
        else:
            # Fallback method - select the text in the entry widget
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.status_var.set("Password copied (basic clipboard support)")
            messagebox.showinfo("Password Copied", 
                               "Password copied using basic clipboard support.\n"
                               "For better clipboard handling, install pyperclip:\n"
                               "pip install pyperclip")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
