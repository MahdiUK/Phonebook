phonebook = {}

# Add a contact
def add_contact(name, number):
    phonebook[name] = number
    print("Contact added successfully!")

# Search for a contact
def search_contact(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook.")

# Display all contacts
def display_contacts():
    for name, number in phonebook.items():
        print(f"{name}: {number}")

# Delete a contact
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted from phonebook.")
    else:
        print(f"{name} not found in phonebook.")

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Enter contact name: ")
        search_contact(name)
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        name = input("Enter contact name: ")
        delete_contact(name)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")