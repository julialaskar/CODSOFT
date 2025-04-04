# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['task']}")

    def mark_completed(self, task_num):
        try:
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num-1]["completed"] = True
                print(f"Task {task_num} marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self, task_num):
        try:
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num-1)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo = TodoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            task_num = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(task_num)
        elif choice == "4":
            todo.view_tasks()
            task_num = int(input("Enter task number to delete: "))
            todo.delete_task(task_num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
