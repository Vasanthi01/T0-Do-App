import json

# Task class to represent a task
class Task:
    def __init__(self, title, description, category, due_date=None, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True
    
    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f" | Due: {self.due_date}" if self.due_date else ""
        return f"[{status}] {self.title} - {self.description} ({self.category}){due_date_str}"

# Function to save tasks to a JSON file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Function to load tasks from a JSON file, with key mapping for 'status'
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            # Create Task objects from the loaded data
            return [
                Task(
                    title=d.get('title', "Untitled"),
                    description=d.get('description', ""),
                    category=d.get('category', "General"),
                    due_date=d.get('due_date'),
                    completed=d.get('completed', False)
                ) for d in data
            ]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The JSON file is not properly formatted.")
        return []

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    due_date = input("Enter task due date (optional, format YYYY-MM-DD): ")
    task = Task(title, description, category, due_date if due_date else None)
    tasks.append(task)
    print(f"Task '{title}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        print(f"Task '{tasks[task_num].title}' marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks.pop(task_num)
        print(f"Task '{task.title}' deleted.")
    else:
        print("Invalid task number.")

# Main function to run the application
def main():
    tasks = load_tasks()
    
    while True:
        print("\nPersonal To-Do List:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()