# https://www.codewars.com/kata/growth-of-a-population/train/python
import math
def nb_year(p0, percent, aug, p):
    cp = p0
    years = 0
    while p >= cp:
        years += 1
        cp += math.floor(((cp * (percent/100)) + aug))
    return years


print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))
