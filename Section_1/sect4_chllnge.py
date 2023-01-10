opt1 = "1. Learn Python" 
opt2 = "2. Learn Java"
opt3 = "3. Go Swimming"
opt4 = "4. Have dinner"
opt5 = "5. Go to bed"
opt6 = "6. Exit"
List = ["1. Learn Python", "2. Learn Java", "3. Go Swimming", "4. Have dinner", "5. Go to bed", "6. Exit"]

# directions = input("Please choose your option from the list below: \n {} \n {} \n {} \n {} \n {} \n {} \n".format(opt1, opt2, opt3, opt4, opt5, opt6))
selection = 7
while True:
    selection = input("Please choose your option from the list below: \n {} \n {} \n {} \n {} \n {} \n {} \n".format(opt1, opt2, opt3, opt4, opt5, opt6))
    print("select '0' to exit")
    if selection == "0":
        print("You have input '0' which means we are going to exit the program. Bye!")
        break
    elif selection == "1":
        print("You have input '1' which means we are going to Learn Python! Yay!")
    elif selection == "2":
        print("You have input '2' which means we are going to learn Java!")
    elif selection == "3":
        print("You have input '3' which means we are going to Go swimming!")
    elif selection == "4":
        print("You have input '4' which means we are going to have dinner!")
    elif selection == "5":
        print("You have input '5' which means we are going to go to bed :)")
else:
    print("Please enter a number between 0 and 6")

# print(directions)

# while 