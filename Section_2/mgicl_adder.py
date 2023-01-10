# numbers = "9,223,372,036,854,775,807"
# print(numbers.split(","))


# a = input("Please enter an number ")
# b = input("Please enter an number ")
# c = input("Please enter an number ")

# print(type(a))
# print(type(b))
# print(type(c))

# integer = [a, b, c]

# print(integer)

# a = int(a)
# b = int(b)
# c = int(c)

# print(type(a))
# print(type(b))
# print(type(c))

# integer = [a, b, c]

# print(integer)

# adder = a + b - c

# print(adder)

###############################################3

# # take multiple inputs in array
# input_str_array = input().split(", ")

# print("array:", input_str_array)

# # take multiple inputs in array
# input_int_array = [int(x) for x in input().split(", ")]

# print("array:", input_int_array)

# # Python program to take integer input in Python

# # input size of the list
# # n = int(input("Enter the size of list : "))
# n = 3

# # store integers in a list using map, split and strip functions
# lst = list(map(int, input(
# 	"Please enter three numbers (Comma-Separated): ").strip().split(",")))[:n]

# print('The list is:', lst) # printing the list comma seperated

# # seperator = ", "
# # output = seperator.join(lst)
# # print(output)

# adder = lst[0] + lst[1] - lst[2]

# print("The calculated answer is: ", adder)

##########################################################################Solution.py
# Take input from the user
user_input = input("Please enter three numbers, comma-seperated with no spaces in between: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)


