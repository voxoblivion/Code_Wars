# https://www.codewars.com/kata/52f78966747862fc9a0009ae/train/python
import operator


def calc(expr):
    # TODO: Your awesome code here
    operations = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
    operator_found = False
    expr_list = expr.split(' ')
    for i in operations:
        if i[0] in expr_list:
            a = int(expr_list[expr_list.index(i[0]) - 1])
            b = int(expr_list[expr_list.index(i[0]) - 2])
            operator_found = True
            c = i[1](b, a)
    if not operator_found:
        len_expr = len(expr_list)
        if len(expr) != 0 and not expr.isspace():
            if '.' in expr:
                return float(expr_list[len_expr - 1])
            else:
                return int(expr_list[len_expr - 1])
        else:
            return 0


print(calc('1 3 - 2 4 +'))
