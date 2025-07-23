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
        9.Факториал числа
        10.Выход """)
        r = True
        while r == True:
            v2 = int(input("v: "))
            if v2 == 1:
                r1 = True
                while r1 == True:
                    n1 = int(input("Введите первое число: "))
                    n2 = int(input("Введите второе число: "))
                    print(n1 + n2)
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 2:
                r1 = True
                while r1 == True:
                    n1 = int(input("Введите первое число: "))
                    n2 = int(input("Введите второе число: "))
                    print(n1 - n2)
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 3:
                r1 = True
                while r1 == True:
                    n1 = int(input("Введите первое число: "))
                    n2 = int(input("Введите второе число: "))
                    print(n1 * n2)
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 4:
                r1 = True
                while r1 == True:
                    v3 = int(input(" 1. Классичексие деление \n2.С остатком\n v: "))
                    if v3 == 1:
                        n1 = int(input("Введите первое число: "))
                        n2 = int(input("Введите второе число: "))
                        print(n1/n2)
                    elif v3 == 2:
                        n1 = int(input("Введите первое число: "))
                        n2 = int(input("Введите второе число: "))
                        print(n1//n2, "", n1%n2)
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 5:
                r1 = True
                while r1 == True:
                    n = int(input("Введите число: "))
                    print(n**2)
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 6:
                r1 = True
                while r1 == True:
                    n = int(input("Введите число: "))
                    s = int(input("Введите степень: "))
                    print(n**s)
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 7:
                r1 = True
                while r1 == True:
                    a = int(input("a:"))
                    b = int(input("b:"))
                    c = int(input("c:"))
                    D = (b**2) - (4*a*c)
                    if D > 0:
                        x1 = (-b + math.sqrt(D))/(2*a)
                        x2 = (-b - math.sqrt(D))/(2*a)
                        if x1 == x2:
                            print(x1)
                        else: print(x1,x2)
                    elif D == 0:
                        x1 = -b/(2*a)
                        print(x1)
                    else: print("error")
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 8:
                r1 = True
                while r1 == True:
                    n = int(input("Введите число: "))
                    z = int(input("Введите кол-во знаков после запятой: "))
                    print(round(n, z))
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 9:
                r1 = True
                while r1 == True:
                    n = int(input("Введите число: "))
                    print(math.factorial(n))
                    print("Повторить?")
                    v3 = input(":")
                    if v3.lower() == "нет":
                        r1 = False
                    else: r1 = True
            elif v2 == 10:
                r = False
        
    elif v1 == 3:
        v = False
        print("goodbay")
