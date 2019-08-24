# https://www.codewars.com/kata/binary-addition/train/python


def addBinary(a,b):
    total = a+b
    binary_string = ""
    a = 1
    binary_numbers = []
    for i in range(100):
        if a > total:
            break
        binary_numbers.append(a)
        a = a * 2
    binary_numbers.reverse()
    number_found = False
    for i in binary_numbers:
        if total / i >= 1 and total != 0:
            total = total-i
            binary_string += "1"
            number_found = True
        elif number_found is True:
            binary_string += "0"

    return binary_string


print(addBinary(0, 63))
