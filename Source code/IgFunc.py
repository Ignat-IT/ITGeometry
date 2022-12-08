import math as m
import sys
from tkinter import messagebox as mb

# Функция проверки неравенства треугольника
def test (a, b, c):
    local = (a + b) > c and (a + c) > b and (b + c) > a
    if not local:
        mb.showerror("Неверный ввод", "Треугольник не существует")
        sys.exit()

# Функция вычисления длины медианы
def mediana(a, b, c):
    M = 1/2 * m.sqrt(2 * a ** 2 + 2 * b ** 2 - c**2)
    return M

# Функция вычисления длины биссектрисы
def biss(a, b, c):
    B = m.sqrt(a * b * (a + b + c) * (a + b -c)) / (a + b)
    return B

# Функция вычисления длины высоты
def height(a, b, c):
    p = (a + b + c) / 2
    H = 2 / a * m.sqrt(p * (p - a) * (p - b) * (p - c))
    return H

# Функция вычисления размера угла a
def angle_a(a, b, c):
    angle_a = m.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    angle_a = angle_a / m.pi * 180
    angle_a = round(angle_a, 4)
    return angle_a

# Функция вычисления размера угла b
def angle_b(a, b, c):
    angle_b = m.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    angle_b = angle_b / m.pi * 180
    angle_b = round(angle_b, 4)
    return angle_b

# Функция вычисления размера угла c
def angle_c(a, b, c):
    angle_c = m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    angle_c = angle_c / m.pi * 180
    angle_c = round(angle_c, 4)
    return angle_c

# Функция вычисления периметра
def perimetr(a, b, c):
    return a + b + c

# Функция вычисления плошади
def square(a, b, c):
    p = (a + b + c) / 2
    sq = m.sqrt(p * (p - a) * (p - b) * (p - c))
    return sq

# Функция проверки строки на соответсвие требования
def teststr(str):
    if str == '':
        mb.showerror("Неверный ввод", "Недостаточно данных")
        sys.exit()
    else:
        truestr = "1234567890" # Разрешённые символы
        firsttrue = "123456789" # Разрешённые первые символы
        local_first = str[0]
        if  local_first not in firsttrue:
            mb.showerror("Неверный ввод","Программа принимает на вход только натуральные числа, меньшие 10000")
            sys.exit()
        local_list = list(str)[1 : len(str) : 1]
        for i in local_list:
            if i not in truestr:
                mb.showerror("Неверный ввод","Программа принимает на вход только натуральные числа, меньшие 10000")
                sys.exit()
        if len(str) >= 5:
            mb.showerror("Неверный ввод", "Число должно быть натуральным и меньшим 10000")
            sys.exit()
