class task:
    def __init__(self,t_id,t_name):
        self.t_id = t_id
        self.t_name = t_name

    def __str__(self):
        return "ID: " + self.t_id + ", Title: " + self.t_name

task_array = []

def createT():
    t_id = input("Enter task id: ")
    t_name = input("Enter task name: ")
    new_task = task(t_id,t_name)
    task_array.append(new_task)
    print("Task is created successfully!")

def readT():
    print("TASK LIST: ")
    for i in task_array:
        print(i)

def updateT():
    t_id = input("Enter task id: ")
    for i in task_array:
        if i.t_id == t_id:
            t_name = input("Enter new task name to update: ")
            i.t_name = t_name
            print("Task details successfully updated")
            print(i)
            return
    print("Task not found")

def deleteT():
    t_id = input("Enter task id: ")
    for i in task_array:
        if i.t_id == t_id:
            task_array.remove(i)
            print("Task successfully deleted")
            return
    print("Task not found")

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
            createT()
        elif choice == '2':
            readT()
        elif choice == '3':
            updateT()
        elif choice == '4':
            deleteT()
        elif choice == '5':
            print("Exiting menu")
            break
        else:
            print("Invalid choice")

menu()