menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


# for meal in menu:
#     if "spam" not in meal:
#         print(meal)

#     else:
#         while "spam" in meal:
#             meal.remove("spam")
#         print(meal)

# print()
# print()

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)

#     else:
#         for item in meal:
#             if item != "spam":
#                 print(meal[item])            

# print()
# print()

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))

# print()
# print()

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end = ", ")
#     print()
    