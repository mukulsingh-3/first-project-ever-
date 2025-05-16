#building a personal mini contact book which has features as shown below
#this will have features to Add a new contact (name, number, email), view all contacts, search contact by names, delete contacts, editing contacts



contacts = {}

while True:
    action = input("Do you want to add, delete, search a contact or exit? (add/delete/search/edit/exit): ").lower()

    #adding contact
    if action == "add":
        name = input("Enter the name of the person: ")
        phone = (input("Enter the phone number of the person: "))
        email = input("Enter the email of the person: ")

        contacts[name] = {
            "phone" : phone,
            "email" : email
        }
    #deleting contact 
    elif action == "delete":
        name = input("Enter the name of the person to delete: ")
        if name in contacts:
            del contacts[name]
            print(name, "'s contact deleted")
        else:
            print(name, "not found in the contact book")
    #searching contact 
    elif action == "search":
        name = input("Enter the name of the person you want to search the contact of: ")
        if name in contacts:
            print(name, " => Phone: ", contacts[name]["phone"], ",Email: ", contacts[name]["email"])
        else:
            print(name,"'s contact not found in the contact book")
    #exiting
    elif action == "exit":
        break
    #editing contact
    elif action == "edit":
        name = input("Enter the name of the person you want to edit the contact of: ")
        if name in contacts:
            print("What do you want to edit?")
            print("1. Phone number")
            print("2. Email")
            choice = input("Enter 1 or 2: ")

            if choice == "1":
                new_phone = int(input("enter the new phone number: "))
                contacts[name]["phone"] = new_phone
                print("Phone number updated successfully!!")
            elif choice == "2":
                new_email = input("Enter the new email: ")
                contacts[name]["email"] = new_email
                print("Email updated successfully!!")
            else:
                print("Invalid choice!!")
    
    #invalid command 
    else:
        print("Invalid option. Please type 'add', 'delete', 'search' or 'exit'")


#final viewing of contact book
if len(contacts) != 0:
    print("\nContact Book: ")
    for name, info in contacts.items():
        print(name,"=> Phone:", info["phone"], ",Email:", info["email"])

else:
    print("\nContact Book\nthe Book is empty")

