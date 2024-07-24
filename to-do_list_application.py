task_list = []

def display_menu():
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task complete\n4. Delete a task\n5. Quit")

def add_task():
    task = input("Enter the task you want to add: ")
    task_list.append({"title": task, "status": "Incomplete"})
    print(f"Task '{task}' added.")

def view_tasks():
    if not task_list:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task['title']} - {task['status']}")

def mark_task_complete():
    if not task_list:
        print("No tasks to mark as complete.")
    else:
        try:
            task_num = int(input("Enter the number of the task to mark as complete: "))
            if 1 <= task_num <= len(task_list):
                task_list[task_num - 1]["status"] = "Complete"
                print(f"Task '{task_list[task_num - 1]['title']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    if not task_list:
        print("No tasks to delete.")
    else:
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(task_list):
                deleted_task = task_list.pop(task_num - 1)
                print(f"Task '{deleted_task['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Thank you for using the To-Do List App! Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
