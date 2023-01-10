import random

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0 # initialize to any number that doesn't equal the answer
#chosen_exit = ""

print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())


while guess != answer:
    guess = int(input())

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