choice = "-"
while choice != "0":
    1if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1. Learn Python")
        print("2. Learn Java")
        print("3. Go Swimming")
        print("4. Have dinner")
        print("5. Go to bed")
        print("0. Exit")

    choice = input()
