# import string
def multiply(x: float, y: float) -> float:
    """Pass two integer values and return the result of the equation.

    Args:
        x (_Integer_): The integer value to be multiplied by y
        y (_Integer_): The integer value to be multiplied by x

    Returns:
        _Integer_: The result of multipying param. x and param. y
    
    (Tim's (instructor) docstring)
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """    
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """Pass a word and return the result of checking if it is a palindrome

    Args:
        string (_String_): The String (word) that the user will input when
        prompted with "Please enter a word to check: "

    Returns:
        _String_: Passed argument (word) is a palindrome or 
        Passed argument (word) is not a palindrome

    (Tim's (instructor) docstring)
    Check if a string is a palindrome.
 
    A palindrome is a string that reads the same forwards as backwards.
 
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """    
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1] == string #Tim added return string[::-1].casefold() == string.casefold() as his solution to case insensitivity


def palindrone_sentence(sentence: str) -> bool:
    """Pass a sentence argument and return the result of checking if it is a palindrome

    Args:
        sentence (_String_): The String (sentence) that the user will input when
        prompted with "Please enter a sentence to check: "

    Returns:
        _String_: Passed argument (sentence) is a palindrome or 
        Passed argument (sentence) is not a palindrome
    
    (Tim's (instructor) docstring)
    Check if a sentence is a palindrome.
 
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """    
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # print(string)
    # return string[::-1] == string #Tim added return string[::-1].casefold() == string.casefold() as his solution to case insensitivity
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

    # sentence =  sent.translate(str.maketrans('', '', string.punctuation))
    # sentence2 = sentence.lower().replace(' ', '')
    # sentence = sentence2
    # # "".join(char if char not in seperators else " " for char in sent).split()
    # return sentence[::-1] == sentence


# word = input("Please enter a word to check: ")
# if is_palindrome(word.lower()):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# sent = input("Please enter a sentence to check: ")
# if palindrone_sentence(sent.lower()):
#     print("'{}' is a palindrome".format(sent))
# else:
#     print("'{}' is not a palindrome".format(sent))


# answer = multiply(10.5, 4)
# print(answer)

# forty_two = multiply(6, 7)
# print(forty_two)

# print()

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

p = palindrone_sentence()

