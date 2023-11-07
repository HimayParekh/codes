# Define an empty list to store the to-do items
todo_list = []

# Function to add a to-do item to the list
def add_todo():
    item = input("Enter a to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

# Function to display the to-do list
def show_todo_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, item in enumerate(todo_list, 1):
            print(f"{index}. {item}")

# Function to remove a to-do item
def remove_todo():
    show_todo_list()
    if not todo_list:
        return
    try:
        item_number = int(input("Enter the number of the item to remove: ")) - 1
        if 0 <= item_number < len(todo_list):
            removed_item = todo_list.pop(item_number)
            print(f"'{removed_item}' has been removed from your to-do list.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid item number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a to-do item")
    print("2. Show to-do list")
    print("3. Remove a to-do item")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_todo()
    elif choice == '2':
        show_todo_list()
    elif choice == '3':
        remove_todo()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
