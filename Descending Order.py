# https://www.codewars.com/kata/descending-order/train/python

def Descending_Order(num):
    a = [i for i in str(num)]
    a.sort(reverse=True)
    a = int("".join(a))
    return a


def Descending_Order_V2(num):
    return int("".join(sorted(str(num), reverse=True)))


print(Descending_Order_V2(21445))

