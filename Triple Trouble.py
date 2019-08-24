# https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python

def triple_double(num1, num2):
    if check_number(num1, 3) == True:
        if check_number(num2, 2) == True:
            return 1
    return 0


def check_number(num, amount):
    num1_list = []
    no_found = 0
    for x in str(num):
        num1_list.append(x)
    for y in range(len(num1_list)):
        if y == 0:
            continue
        else:
            if num1_list[y] == num1_list[y - 1]:
                no_found += 1
                if no_found == (amount - 1):
                    return True
                    continue


a = '1'
print(a * 3)
