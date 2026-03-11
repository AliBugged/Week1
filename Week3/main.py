from task_manager import TaskManager

manager = TaskManager()
manager.load_from_file()

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Save tasks")
    print("6. Exit")
    choice = input("Choose: ")

    if choice == "1":
        title = input("Task title: ")
        manager.add_task(title)
        print("Task added")

    elif choice == "2":
        manager.show_tasks()
        print("End of tasks")

    elif choice == "3":
        try:
            index = int(input("Task number: ")) - 1
            
            if index < 0 or index >= len(manager.tasks):
                print("Invalid task number")
            else:
                manager.complete_task(index)
                print("Task marked as completed")
        
        except:
            print("Invalid input")

    elif choice == "4":
        try:
            index = int(input("Task number: ")) - 1
            manager.delete_task(index)
            print("Task deleted")

        except:
            print("Invalid task number")

    elif choice == "5":
        manager.save_to_file()
        print("Tasks saved")
    
    elif choice == "6":
        manager.save_to_file()
        print("Tasks saved")
        break