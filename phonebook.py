phonebook = {}

while True:
    ask = input("Enter command ('add', 'search', 'delete', 'update', or 'exit'): ").lower()

    if ask == "exit":
        break

    elif ask == "add":
        name = input("Enter a contact name: ").lower()
        number = input("Enter the contact number: ")


        if name in phonebook:
            phonebook[name].append(number)  # add number to existing list
        else:
            phonebook[name] = [number] # start a new list for the contact
            print(f"Number added for {name}.")

    elif ask == "search":
        name = input("Enter a contact name: ").lower()
        if name in phonebook:
            print(f"{name}: {', '.join(phonebook[name])}")
        else:
            print("Not found")

    elif ask == "delete":
        name = input("Enter a contact name: ").lower()
        if name in phonebook:
            phonebook.pop(name)
        else:
            print("Not found")

    elif ask == "update":
        name = input("Enter a contact name: ").lower()
        if name in phonebook:
            print(f"Current numbers for {name}: {', '.join(phonebook[name])}")
            new_number = input("Enter the new number to replace: ")
            phonebook[name] = [new_number] # replace with  single new number
            print(f"{name}`s number updated.")
        else:
            print("Not found")

    else:
        print("Invalid command")

for key, value in phonebook.items():
    print(f"{key}: {''.join(value)}")
