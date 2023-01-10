"""
Sum even or odd numbers in a range
In this coding exercise, you have to write a function named sum_eo with the following parameters:

n: a positive number
t: a str

If t has the value 'e', the function should return the sum of all even natural numbers less than n.

Else if t has the value 'o', the function should return the sum of all odd natural numbers less than n.

For any other values of t return -1. 
"""

def sum_eo(n, t):
    total = 0
    if t == 'e':
        for number in range (1, n+1):
            if(number %2 == 0):
                print ("{0}".format(number))
                # print(total)
                total = total + number
        return print("the sum of all even natural numbers less than {0} is {1}!".format(n, total))
        # if num % 2 == 0:
            # return (num, end=" ")
    elif t == 'o':
        for number in range (1, n+1):
            if(number %2 != 0):
                print ("{0}".format(number))
                total = total + number
        return print("the sum of all even natural numbers less than {0} is {1}!".format(n, total))

        # return("{0} is an odd number".format(n))
        # if num % 2 != 0:
            # return the sum of all odd natural numbers less than 'n'
    else:
        return print('-1')
        # TODO: write code...
    
n_1 = int(input("Please enter a postive number: "))
t_1 = str(input('''please enter 'e' for the sum of all even natural numbers less than {0} \nplease enter 'o' for the sum of all odd natural numbers less than {0}: '''.format(n_1)))
# total = 0

# for number in range (1, n_1+1):
#     if(number %2 == 0):
#         print("{0}".format(number))

sum_eo(n_1, t_1)
# if t='e' 