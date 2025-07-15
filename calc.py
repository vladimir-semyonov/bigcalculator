import math
import random
import time


print("Добро пожаловать в калькулятор")
print("Вы можете использовать здесь разные функции")
v = True

while v == True:
    print("Выберите раздел:")
    print("""    1.Алгебра
    2. Геометрия
    3. Выход
            """)
    v1 = int(input("v: "))
    if v1 == 1:
        print("""Выберите функции:
        1.Сложение
        2.Вычитание
        3.Умножение
        4.Деление
              
        5.Возведение в квадрат
        6.Возведение в степень
        7.Решение квадратного уравнения
        8.Округление
        9.Факториал числа""")
        v2 = int(input("v: "))
        if v2 == 1:
            n1 = int(input("Введите первое число: "))
            n2 = int(input("Введите второе число: "))
            print(n1 + n2)
        elif v2 == 2:
            n1 = int(input("Введите первое число: "))
            n2 = int(input("Введите второе число: "))
            print(n1 - n2)
        elif v2 == 3:
            n1 = int(input("Введите первое число: "))
            n2 = int(input("Введите второе число: "))
            print(n1 * n2)
        elif v2 == 4:
            print()
            v3 = int(input(" 1. Классичексие деление \n2.С остатком\n v: "))
            if v3 == 1:
                n1 = int(input("Введите первое число: "))
                n2 = int(input("Введите второе число: "))
                print(n1/n2)
            elif v3 == 2:
                n1 = int(input("Введите первое число: "))
                n2 = int(input("Введите второе число: "))
                print(n1//n2, "", n1%n2)
        elif v2 == 5:
            n = int(input())
            print(n**2)
        elif v2 == 6:
            n = int(input())
            s = int(input())
            print(n**s)
        elif v2 == 7:
            print()
        elif v2 == 8:
            n = int(input())
            z = int(input())
            print(round(n, z))
        elif v2 == 9:
            n = int(input())
            print(math.factorial(n))


    elif v1 == 3:
        v = False
        print("goodbay")
