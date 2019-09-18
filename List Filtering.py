# https://www.codewars.com/kata/list-filtering/train/javascript


def filter_list(l):
    e = []
    for i in l:
        if isinstance(i, str):
            e.append(i)
    [l.pop(l.index(i)) for i in e]
    return l


def filter_list_V2(l):
    return [i for i in l if not isinstance(i, str)]

print(filter_list([1,2,'a','b']))



