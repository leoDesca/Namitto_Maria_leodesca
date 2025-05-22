#assignment create an inventory management  use loops to display or update a list of stock items

#Inventory management programm
print("Welcome to Inventory Management!!")
item_names = []
item_quantities = []

while True:
    print("\n--- MENU ---")
    print("1. Add item")
    print("2. Remove item") 
    print("3. Show all items")
    print("4. Exit")

    choice = input("Enter 1, 2, 3, or 4: ")
    if choice == "1":
        print("\n--- ADD ITEM ---")
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity for the item: "))
        found = False
        i = 0
        while i < len(item_names):
            if item_names[i] == name:
                item_quantities[i] = item_quantities[i] + quantity
                print("Added more " + name)
                found = True
            i = i + 1
        
        if found == False:
            item_names.append(name)
            item_quantities.append(quantity)
            print("Added " + name + " to inventory")
    
    elif choice == "2":
        print("\n--- REMOVE ITEM ---")
        
        if len(item_names) == 0:
            print("Nothing to remove!")
        else:
            print("Current items:")
            i = 0
            while i < len(item_names):
                print(item_names[i] + ": " + str(item_quantities[i]))
                i = i + 1
            
            name = input("Enter item to remove: ")
            found = False
            i = 0
            while i < len(item_names):
                if item_names[i] == name:
                    print("Current amount: " + str(item_quantities[i]))
                    remove_amount = int(input("How many to remove? "))
                    if remove_amount >= item_quantities[i]:
                        item_names.pop(i)
                        item_quantities.pop(i)
                        print("Removed all " + name)
                    else:
                        item_quantities[i] = item_quantities[i] - remove_amount
                        print("Removed " + str(remove_amount) + " " + name)
                    found = True
                i = i + 1
            if found == False:
                print("Item not found!")
    elif choice == "3":
        print("\n--- ALL ITEMS ---")
        
        if len(item_names) == 0:
            print("No items in inventory")
        else:
            print("Your stock items:")
            for i in range(len(item_names)):
                print(item_names[i] + ": " + str(item_quantities[i]))
            total = 0
            for i in range(len(item_quantities)):
                total = total + item_quantities[i]
            
            print("Total items: " + str(total))
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please pick 1, 2, 3, or 4 only!")
