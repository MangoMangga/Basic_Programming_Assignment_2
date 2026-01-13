tasks = []

def add_task(description, priority):
    tasks.append({"description" : description, "priority" : priority, "done": False})

def view_tasks():
    if not tasks:
        print("No Task!")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task ["done"] else "Pending"
        print(f"{i+1}: {task['description']}, Priority: {task['priority']} - {status}")

def mark_done(index):
    try:
        tasks[index - 1]["done"] = True
    except IndexError:
        print("Invalid Index.")

def main_menu():
    while True:
        print("\nTask Manager:\n1. Add Task\n2. View Task\n3. Mark Done\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            desc = input("Description: ")
            priority = input("Priority (High, Medium, Low): ")
            if priority not in ["High", "Medium", "Low"]:
                print("Invalid Priority.")
            else:
                add_task(desc, priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                idx = int(input("Index: "))
                mark_done(idx)
            except ValueError:
                print("Invalid Input.")
        elif choice == "4":
            break
        else:
            print("Invalid Choice.")
main_menu() 