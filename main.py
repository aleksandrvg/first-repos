# def ploshad(a, b):
#     return a * b
#
# a = int(input('Введите значение: '))
# b = int(input('Введите значение: '))
# print(f'Площадь: {ploshad(a, b)}')



# import math
#
# def ploshad(r):
#     return math.pi * r ** 2
#
# r = int(input('Введите радиус: '))
# print(f'Площадь круга: {ploshad(r)}')



# import math
#
# def ploshad(a, b, r):
#     result = {}
#     areaCircle = math.pi * r ** 2
#     areaSquare = a * b
#     result.update({'Площадь': areaSquare})
#     result.update({'Периметр': 2 * a + 2 * b})
#     result.update({'Площадь круга': areaCircle})
#     return result
#
# a = int(input('Введите значение: '))
# b = int(input('Введите значение: '))
# r = int(input('Введите радиус: '))
# for key, item in ploshad(a, b, r).items():
#     print(f'{key}: {item}')



import random

def getHealth():
    health = 100
    i = 0
    result = {}
    while health > 0:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        if a > b:
            health = health
        else:
            health -= 20
        i += 1
        result.update({i: health})
    print(f'Количество {i}: {health}')
    print('End')
getHealth()
