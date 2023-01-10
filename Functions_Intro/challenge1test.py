import string

def palindrone_sentence(sentence):
    # for punc in string.punctuation:
    #     psent = sentence.replace(punc, '')
        # if not punc.ascii_lowercase()
    # values = sentence.strip([])
    # values =  sent.translate(str.maketrans('', '', string.punctuation))
    # "".join(char if char not in seperators else " " for char in sent).split()
    return sentence[::-1] == sentence


sent = input("Please enter a sentence to check: ")
if palindrone_sentence(sent.lower()):
    print("'{}' is a palindrome".format(sent))
else:
    print("'{}' is not a palindrome".format(sent))
