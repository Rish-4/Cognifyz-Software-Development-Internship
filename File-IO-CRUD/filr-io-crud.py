def load_tasks():
    try:
        with open("File-IO-CRUD/tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("File-IO-CRUD/tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def create_task():
    task = input("Enter new task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def read_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Task List ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task():
    tasks = load_tasks()
    read_tasks()
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter updated task: ")
            tasks[task_num] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    read_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while 1:
        print("Type corresponding number for desired functions!")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")

menu()