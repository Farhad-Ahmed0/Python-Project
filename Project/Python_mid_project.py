class PC:
    def __init__(self, number, os, status):
        self.number = number
        self.os = os
        self.status = status
pc_list = []

def add_pc():
    number = input("Enter PC number: ")
    os = input("Enter operating system installed: ")
    status = input("Enter status of the PC: ")
    for pc in pc_list:
        if pc.number == number:
            choice = input("This PC number already exists. Do you want to modify it or remove it? (m/r/n): ")
            if choice == "m":
                pc.os = os
                pc.status = status
            elif choice == "r":
                pc_list.remove(pc)
            return
    pc = PC(number, os, status)
    pc_list.append(pc)

def update_pc():
    number = input("Enter PC number to update: ")
    for pc in pc_list:
        if pc.number == number:
            os = input("Enter new operating system installed: ")
            status = input("Enter new status of the PC: ")
            pc.os = os
            pc.status = status
            return
    print("PC not found")

def remove_pc():
    number = input("Enter PC number to remove: ")
    for pc in pc_list:
        if pc.number == number:
            pc_list.remove(pc)
            return
    print("PC not found")

def display_all():
    print("PC Number\tOS\tStatus")
    for pc in pc_list:
        print(f"{pc.number}\t\t{pc.os}\t{pc.status}")

def display_pc():
    number = input("Enter PC number to display: ")
    for pc in pc_list:
        if pc.number == number:
            print(f"PC Number: {pc.number}")
            print(f"Operating System: {pc.os}")
            print(f"Status: {pc.status}")
            return
    print("PC not found")

def search_pc():
    number = input("Enter PC number to search: ")
    for pc in pc_list:
        if pc.number == number:
            print(f"PC Number: {pc.number}")
            print(f"Operating System: {pc.os}")
            print(f"Status: {pc.status}")
            return
    choice = input("PC not found. Do you want to add it? (y/n): ")
    if choice == "y":
        add_pc()

def store():
    with open("pc_list.txt", "w") as file:
        file.write("PC Number\tOS\tStatus\n")
        for pc in pc_list:
            file.write(f"{pc.number}\t\t{pc.os}\t{pc.status}\n")

while True:
    print("\nPC Lab Management System")
    print("1. Add a new PC")
    print("2. Update PC information")
    print("3. Remove a PC")
    print("4. Display all PCs")
    print("5. Display a PC")
    print("6. Search for a PC")
    print("7. Store all PCs to file")
    print("8. Quit")
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        add_pc()
    elif choice == "2":
        update_pc()
    elif choice == "3":
        remove_pc()
    elif choice == "4":
        display_all()
    elif choice == "5":
        display_pc()
    elif choice == "6":
        search_pc()
    elif choice == "7":
        store()
    elif choice == "8":
        break
    else:
        print("Invalid Number choosen.Enter your choice (1-8)")