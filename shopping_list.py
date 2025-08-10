# Shopping List Maker
# 1. Start with an empty list
shopping_list = []

print("Welcome to the Shopping List Maker!")
print("Type 'done' when you finish.\n")


# 2. Loop to keep asking for items

while True:
    item = input("Add an item: ")

    if item.lower() == "done": # stop when user says 'done'
        break

    shopping_list.append(item) # add to list

# 3. Show final list

print("\nYour shopping list:")

for i, product in enumerate(shopping_list, start = 1):
    print(f"{i}. {product}")


