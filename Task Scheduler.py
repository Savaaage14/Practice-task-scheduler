task = {}

def addtaskform():
    task_number = input("Input task number:")
    if task_number in task:
        print("Task number is currently existing!")
        return
    else:
        task_description = input("Input task description:")
        task[task_number] = task_description 
        print("Task successfully added in the system")

def updatetaskform():
    task_number = input("Input task number to be updated: ")
    if task_number in task:
        task_newdesc = input("Input new description: ")
        task[task_number] = task_newdesc
        print("Task successfully updated in the system")
    else:
        print("Task number doesn't exist!")
        return

def deletetaskform():
    task_number = input("Input task number to be deleted: ")
    if task_number in task:
        del task[task_number]
        print("Task number successfully deleted")
    else:
        print("Task number doesn't exist!")
        return
def showtasks():
    if not task:
        print("No tasks found")
    else:
        print("See tasks:")
        for task_number, task_description in task.items():
            print(f"{task_number}: {task_description}")
        print()

def mainform():
     while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show All Tasks")
        print("5. Exit")
        choice = input("Choose one from the option (1-5): ")

        if choice == "1":
            addtaskform()
        elif choice == "2":
            updatetaskform()
        elif choice == "3":
            deletetaskform()
        elif choice == "4":
            showtasks()
        elif choice == "5":
            print("Exiting task manager.")
            break
        else:
            print("Invalid choice. Please try again.")

mainform()

