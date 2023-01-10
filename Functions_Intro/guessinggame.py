import random


def get_integer(prompt):
    """Get an integer from Standard Input (stdin).

    The function will conitnue looping, and prompting
    ther user, until a valid `int` is entered.

    Args:
        prompt (_String_): The String that the user will see, when
        they're prompted to enter the value.

    Returns:
        _Integer_: The integer that the user enters.
    """    
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0} is not a valid number".format(temp))

help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0 # initialize to any number that doesn't equal the answer
#chosen_exit = ""

print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())


while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
        # print("You got it first time")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")

        # while guess != answer:
            # print("type '0' to quit")
            # if chosen_exit.casefold() == 0:
            #     print("Game Over")
            #     break