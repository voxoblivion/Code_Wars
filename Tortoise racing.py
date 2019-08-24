def race(v1, v2, g):
    if v1 <= v2:
        time = (g/(v2 - v1))
        hours = time
        minutes = ((hours % 1) * 60)
        seconds = ((minutes % 1) * 60)
        time = [int(hours), int(minutes), int(seconds)]
        return time
    else:
        return None


print(race(720, 850, 70))
