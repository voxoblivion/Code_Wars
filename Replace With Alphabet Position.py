# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
def alphabet_position(text):
    alphabet_positions = ''
    j = 0
# Create dic with every alphabet assigned to number
# Get the first letter and print out its number value
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    for i in text.lower():
        j += 1
        if i in alphabet:
            if j != len(text):
                alphabet_positions += str(alphabet[i]) + ' '
            else:
                alphabet_positions += str(alphabet[i])

        else:
            continue

    return alphabet_positions

print(alphabet_position("The sunset sets at twelve o' clock."))
