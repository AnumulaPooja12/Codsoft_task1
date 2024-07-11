# Function to display the main menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark Task as Done")
    print("4. Exit")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print("Task added successfully!")

# Function to mark a task as done
def mark_task_as_done(todo_list):
    print("Select the task to mark as done:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")
    try:
        task_index = int(input("Enter the task number: ")) - 1
        if 0 <= task_index < len(todo_list):
            completed_task = todo_list.pop(task_index)
            print(f"Task '{completed_task}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view the to-do list
def view_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Main function to run the application
def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_task_as_done(todo_list)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
		