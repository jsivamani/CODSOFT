def add_contact(contacts):
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone']:
            print(f"Found Contact - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    print("Enter new details (leave blank to keep current value):")
    phone = input(f"New phone number (current: {contacts[name]['phone']}): ")
    email = input(f"New email (current: {contacts[name]['email']}): ")
    address = input(f"New address (current: {contacts[name]['address']}): ")

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    print(f"Contact {name} updated successfully.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    print("Contact Management System")
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
