def get_item_name(item):
    return item['name']
def sort_items(items):
    return sorted(items, key=get_item_name)
def display_items(items):
    for item in items:
        print(f"{item['name'].capitalize()}: {item['quantity']}")
def main():
    items = [
        {"name": "apple", "quantity": 25},
        {"name": "carrot", "quantity": 20},
        {"name": "eggplant", "quantity": 5},
         {"name": "dates", "quantity": 10},
        {"name": "fig", "quantity": 15},
        {"name": "grape", "quantity": 50},
        {"name": "honeydew", "quantity": 12},
        {"name": "kiwi", "quantity": 22},
        {"name": "banana", "quantity": 30},
        {"name": "lemon", "quantity": 18}
    ]
    print("Original List:")
    display_items(items)
    # Sort and display sorted items
    items = sort_items(items)
    print("\nSorted List:")
    display_items(items)
    while True:
        add_item = input("\nAdd a new item? (yes/no): ").strip().lower()
        if add_item == 'no':
            break
        elif add_item == 'yes':
            name = input("Enter the item name: ").strip().lower()
            quantity = int(input("Enter the quantity: ").strip())
            items.append({"name": name, "quantity": quantity})
            # Sort and display updated list
            items = sort_items(items)
            print("\nUpdated Sorted List:")
            display_items(items)
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
if _name_ == "_main_":
    main()









