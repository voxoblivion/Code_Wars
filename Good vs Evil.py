# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python
def goodVsEvil(good, evil):
    good = good.split(' ')
    evil = evil.split(' ')
    good_values = [1, 2, 3, 3, 4, 10]
    evil_values = [1, 2, 2, 2, 3, 5, 10]
    total_good = sum(map(lambda x, y: int(x) * y, good, good_values))
    total_evil = sum(map(lambda x, y: int(x) * y, evil, evil_values))
    if total_good == total_evil:
        return 'Battle Result: No victor on this battle field'
    elif total_good > total_evil:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: Evil eradicates all trace of Good"


goodVsEvil('1 2 3 4 5 6','1 2 3 4 5 6 7')
