#import math
from math import sqrt

print('Программа для решения квадратных уравнений!')
bad_data = True
# badData
while bad_data == True:
    try:
        a = int(input('Введите число а: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
        bad_data = False
    except ValueError:
        print('Данные не привести к числу')

# N = a + b
# print(N)
D = (b * b) - (4 * a * c)
print(D)

if D > 0:
    d = sqrt(D)
    x1 = ((-b) + d) / (2 * a)
    x2 = ((-b) - d) / (2 * a)
    print(f'уровнение имеет 2 корня \n x1 ={x1} x2={x2}')
elif D == 0:
    x1 = (-b) / (2 * a)
    print('уравнение имеет 1 корень. x1={}'. format(x1))
else:
    print('Корней нет')
