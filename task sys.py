import sys

# A class to represent a single to-do item
class ToDoItem:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description}"


# A class to manage the to-do list
class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, description):
        item = ToDoItem(description)
        self.items.append(item)

    def list_items(self):
        if not self.items:
            print("No to-do items yet.")
        else:
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item}")

    def mark_item_complete(self, index):
        try:
            self.items[index].mark_complete()
        except IndexError:
            print(f"Item {index + 1} does not exist in the list.")

    def remove_item(self, index):
        try:
            self.items.pop(index)
        except IndexError:
            print(f"Item {index + 1} does not exist in the list.")


def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Options:")
        print("1. wake up by 6.30am")
        print("2. List all tasks")
        print("3. Mark a task as complete")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            description = input("Enter the task description: ")
            to_do_list.add_item(description)
        elif choice == "2":
            to_do_list.list_items()
        elif choice == "3":
            to_do_list.list_items()
            index = int(input("Enter the task number to mark complete: ")) - 1
            to_do_list.mark_item_complete(index)
        elif choice == "4":
            to_do_list.list_items()
            index = int(input("Enter the task number to remove: ")) - 1
            to_do_list.remove_item(index)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
