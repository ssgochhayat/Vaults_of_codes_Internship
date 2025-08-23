import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    tasks.append(Task(title, description, category))
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "✔️" if task.completed else "❌"
        print(f"{i + 1}. [{status}] {task.title} - {task.description} (Category: {task.category})")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_completed()
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("-"*50)
        print("Personal To-Do List Application")
        print("-"*50)
        print("\t 1. Add Task")
        print("\t 2. View Tasks")
        print("\t 3. Mark Task Completed")
        print("\t 4. Delete Task")
        print("\t 5. Exit")
        print("-"*50)
        choice = input("Choose an option (1-5): ")

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
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
