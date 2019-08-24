class Mammal:
    def __init__(self, gender):
        self.gender = gender
    blood_temp = 'warm'


class Carnivour:
    food = 'Meat'


class Lion(Mammal, Carnivour):
    food_chain = 'alpha'


a = Lion('Male')
print(a.blood_temp)
print(a.gender)
print(a.food + '\n' + a.food_chain)

