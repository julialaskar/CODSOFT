import tkinter as tk
from tkinter import messagebox

class KawaiiToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("(っ◕‿◕)っ To-Do List")
        self.root.geometry("300x400")
        self.root.configure(bg="#FFE6EE")  # Pink background
        
        # Cute font (change to any kawaii font you have installed)
        self.font = ("Comic Sans MS", 12)
        
        # Header
        self.header = tk.Label(root, 
                             text="★彡 Your Kawaii Tasks 彡★", 
                             font=("Comic Sans MS", 14, "bold"), 
                             bg="#FFB6C1", fg="white")
        self.header.pack(fill=tk.X, pady=10)
        
        # Task entry
        self.task_entry = tk.Entry(root, 
                                 font=self.font, 
                                 bg="white", 
                                 relief=tk.FLAT)
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)
        
        # Add button
        self.add_btn = tk.Button(root, 
                               text="(◕‿◕) Add", 
                               command=self.add_task,
                               bg="#FFB6C1", 
                               fg="white",
                               relief=tk.FLAT,
                               font=self.font)
        self.add_btn.pack(pady=5)
        
        # Task list
        self.task_list = tk.Listbox(root, 
                                  font=self.font, 
                                  bg="white",
                                  selectbackground="#FFB6C1",
                                  relief=tk.FLAT)
        self.task_list.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Complete and Delete buttons
        btn_frame = tk.Frame(root, bg="#FFE6EE")
        btn_frame.pack(pady=10)
        
        self.complete_btn = tk.Button(btn_frame, 
                                    text="(✓) Done", 
                                    command=self.complete_task,
                                    bg="#98FB98",  # Pastel green
                                    font=self.font)
        self.complete_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_btn = tk.Button(btn_frame, 
                                  text="(×) Delete", 
                                  command=self.delete_task,
                                  bg="#FF9999",  # Pastel red
                                  font=self.font)
        self.delete_btn.pack(side=tk.LEFT, padx=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, f"○ {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("(｡•́︿•̀｡)", "Please enter a task!")
    
    def complete_task(self):
        try:
            index = self.task_list.curselection()[0]
            task = self.task_list.get(index)
            if task.startswith("○"):
                self.task_list.delete(index)
                self.task_list.insert(index, f"✓ {task[2:]}")
            else:
                self.task_list.delete(index)
                self.task_list.insert(index, f"○ {task[2:]}")
        except:
            messagebox.showwarning("(ﾉ◕ヮ◕)ﾉ", "Please select a task first!")
    
    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
        except:
            messagebox.showwarning("(╥﹏╥)", "Please select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KawaiiToDo(root)
    root.mainloop()
