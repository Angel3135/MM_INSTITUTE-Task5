contacts= {}

while True:
    print("\n contact book app")
    print("1.create contact")
    print("2.view contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.search contact")
    print("6.count contact")
    print("7.exit")

    choice= input("enter your choice=")

    if choice=="1":
        name= input("enter your name=")
        if name in contacts:
            print(f"contactname {name} already exist!")
        else:
            age= input("enter age=")
            email= input("enter email=")
            mobile= input("enter mobilenumber=")
            contacts[name]= {"age": int(age), "email": email, "mobile": mobile}    
            print(f"contactname {name} has been created successfully!")

    elif choice== "2":
        name= input("enter contact name to view=")
        if name in contacts:
            contact= contacts[name]
            print(f"name:{name}, age: {age}, mobile number: {mobile}")
        else:
            print("contact not found")

    elif choice== "3":
        name= input("enter name to update contact=")
        if name in contacts:
            age= input("enter updated age=")
            email= input("enter updated email=")
            mobile= input("enter updated mobile number=")
            contacts[name]= {"age": int(age), "email": email, "mobile": mobile}
        else:
            print("contact not found!")

    elif choice== "4":
        name= input("enter contact name to delete=")
        if name in contacts:
            del contacts[name]
            print(f"contactname {name} has been deleted successfully!")
        else:
            print("contact not found")

    elif choice== "5":
        search_name= input("enter contact name to search=")
        found=False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"found name{name}, age: {age}, mobile number: {mobile}")
                found=True
        if not found:
            print(" no contact found with that name")

    elif choice== "6":
        print(f"total contacts in your book: {len(contacts)}")

    elif choice== "7":
        print("good bye...closing the program")
    else:
        print("invalid input")                                                              
          