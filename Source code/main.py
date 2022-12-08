from IgFunc import *
from tkinter import *
import turtle as t
#Окно и фрейм
window = Tk() #Создаём окно
window.config(bg = "gray16") #Увет фона окна
window.title("IT Geometry") #Название окна
window.geometry("720x440") #Указываем размеры
window.resizable(width=False, height=False) #Отключаем возможность изменения размеров окна
mainw = Frame(window, bg = "gray64") #Создаём фрейм для вывода элементов
mainw.place(relx = 0.04 / 1.4, rely = 0.12, relwidth= 1-2*(0.04 / 1.4), relheight = 1 - 2 * 0.04 - 0.08) #Выводим фрейм в окно

#Функция создания графика
def Grafik():
    triangle_button.config(state='disabled') #Отключаем возможность повтрного нажатия на клавишу
    fresult.configure(text="") #Убираем поле ответ

    #Получаем длины сторон
    a1 = import_a.get()
    b1 = import_b.get()
    c1 = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a1)
    teststr(b1)
    teststr(c1)
    #Пероводим из строкового типа в числовой
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    #Проверяем треугольник на существование
    test(a1, b1, c1)
    #Вычисляем углы треугольника
    a_a = angle_a(a1, b1, c1)
    a_b = angle_b(a1, b1, c1)
    a_c = angle_c(a1, b1, c1)
    #Увеличиваем/уменьшаем размеры треугольника, так, чтобы треугольник был хорошо виден
    a = 180
    b = 180 * b1 / a1
    c = 180 * c1 / a1
    h = height(a, b, c) #Считаем высоту

    t.bgcolor("Gray16") #Цвет фона
    t.color("White") #Цвет линиЙ
    t.hideturtle() #Убирает черепашку
    t.speed(0) #Убираем анимацию рисования

    #Центровка треугольника
    t.penup()
    t.left(90)
    t.backward(h / 3)
    t.left(90)
    t.pendown()

    #Отрисовка трегольника
    t.forward(c / 2)
    t.right(180 - a_b)
    t.forward(a)
    t.right(180 - a_c)
    t.forward(b)
    t.right(180 - a_a)
    t.forward (c / 2)
    t.done()

def Mediana_a():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем трегольник на существование
    test(a, b, c)
    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(mediana(c, b, a), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Mediana_b():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, c, b)
    
     #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(mediana(a, c, b), 2)}"
    fresult.configure(text=text)

def Mediana_c():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)

    
    #Проверяем треугольник на существование
    test(a, b, c)
    
     #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(mediana(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Bissectr_a():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)

    #Проверяем треугольник на существование
    test(a, b, c)
    
    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(biss(b, c, a), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Bissectr_b():
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, b, c)
    
    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(biss(a, c, b), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Bissectr_c():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)

    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом`
    answer = "Ответ: "
    text = f"{answer} {round(biss(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Height_a():
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(height(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Height_b():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(height(b, a, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Height_c():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(height(c, a, b), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Square():
    #Получаем длины сторон
    a = import_a.get()
    b = import_a.get()
    c = import_a.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(square(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Perimetr():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)
    
    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {a+b+c}"
    fresult.configure(text=text)
    perimetr(a, b, c)

def Angle_a():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)

    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(angle_a(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

def Angle_b():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)

    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(angle_b(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)
    
def Angle_c():
    #Получаем длины сторон
    a = import_a.get()
    b = import_b.get()
    c = import_c.get()

    #Проверяем на отсутствие символов
    teststr(a)
    teststr(b)
    teststr(c)
    #Пероводим из строкового типа в числовой
    a = int(a)
    b = int(b)
    c = int(c)

    #Проверяем треугольник на существование
    test(a, b, c)

    #Создаём строку с ответом
    answer = "Ответ: "
    text = f"{answer} {round(angle_c(a, b, c), 2)}"
    #Выводим её в поле для вывода
    fresult.configure(text=text)

#Создаём поля для ввода
import_a = Entry(mainw, width = 16)
import_a.insert(0, "BC") #Подписываем сторону треугольника
import_b = Entry(mainw, width = 16)
import_b.insert(0, "AC") #Подписываем сторону треугольника
import_c = Entry(mainw, width = 16)
import_c.insert(0, "AB") #Подписываем сторону треугольника
#Выводим поля для ввода в фрейм
import_a.place (relx = 0.5, rely = 0.08, anchor = CENTER)
import_b.place (relx = 0.5, rely = 0.16, anchor = CENTER)
import_c.place (relx = 0.5, rely = 0.24, anchor = CENTER)

#Создаём кнопки
Programm_name = Label(window, text = "IT Geometry", font = ("Harrington", 18), bg="Gray16", fg = "White") #Поле с названием программы
mediana_a_button = Button(mainw, text = "Медиана из A", command=Mediana_a, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
mediana_b_button = Button(mainw, text = "Медиана из B", command=Mediana_b, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
mediana_c_button = Button(mainw, text = "Медиана из C", command=Mediana_c, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
bissectr_a_button = Button(mainw, text = "Биссектрисса из A", command=Bissectr_a, width = 15, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
bissectr_b_button = Button(mainw, text = "Биссектрисса из B", command=Bissectr_b, width = 15, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
bissectr_c_button = Button(mainw, text = "Биссектрисса из C", command=Bissectr_c, width = 15, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
height_a_button = Button(mainw, text = "Высота из A", command=Height_a, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
height_b_button = Button(mainw, text = "Высота из B", command=Height_b, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
height_c_button = Button(mainw, text = "Высота из C", command=Height_c, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
angle_a_button = Button(mainw, text = "Угол A", command=Angle_a, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
angle_b_button = Button(mainw, text = "Угол B", command=Angle_b, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
angle_c_button = Button(mainw, text = "Угол C", command=Angle_c, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
perimetr_button = Button(mainw, text = "Периметр", command=Perimetr, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
square_button = Button(mainw, text = "Площадь", command=Square, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
triangle_button = Button(mainw, text = "График", command = Grafik, width = 14, height = 1, font=("Segoe UI", 7), bg = "Gray16", fg = "White")
fresult = Label(mainw, text = "Ответ: ", bg = "Gray64", font = ("Monotype Corsiva", 18)) #Поле для вывода ответа
#Выводим кнопки, поле с названием программы и поля для вывода ответа в фрейм
mediana_a_button.place(relx = 0.5 - 0.19 * 2, rely = 2/5, anchor = CENTER)
mediana_b_button.place(relx = 0.5 - 0.19 * 2, rely = 2/5 + 0.1, anchor = CENTER)
mediana_c_button.place(relx = 0.5 - 0.19 * 2, rely = 2/5 + 0.2, anchor = CENTER)
bissectr_a_button.place(relx= 0.5 - 0.19, rely = 2/5, anchor = CENTER)
bissectr_b_button.place(relx = 0.5 - 0.19, rely = 2/5 + 0.1, anchor = CENTER)
bissectr_c_button.place(relx = 0.5 - 0.19, rely = 2/5 + 0.2, anchor = CENTER)
height_a_button.place(relx = 0.5, rely = 2/5, anchor = CENTER)
height_b_button.place(relx = 0.5, rely = 2/5 + 0.1, anchor = CENTER) 
height_c_button.place(relx = 0.5, rely = 2/5 + 0.2, anchor = CENTER)
angle_a_button.place(relx = 0.5 + 0.19, rely = 2/5, anchor = CENTER)
angle_b_button.place(relx = 0.5 + 0.19, rely = 2/5 + 0.1, anchor = CENTER)
angle_c_button.place(relx = 0.5 + 0.19,  rely = 2/5 + 0.2, anchor = CENTER)
perimetr_button.place(relx = 0.5 + 0.19 * 2,  rely = 2/5, anchor = CENTER)
square_button.place(relx = 0.5 + 0.19 * 2,  rely = 2/5 + 0.1, anchor = CENTER)
triangle_button.place(relx = 0.5 + 0.19 * 2,  rely = 2/5 + 0.2, anchor = CENTER)
fresult.place(relx = 0.5,  rely = 0.85, anchor = CENTER)
Programm_name.place(relx = 0.5, rely = 0.06, anchor = CENTER)

window.mainloop() #Запускаем отрисовку окна