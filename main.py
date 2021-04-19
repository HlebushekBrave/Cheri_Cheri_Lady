# Мы долбанемся с этой прогой
import turtle as t


def icefrackal(n, size):  # Ледяной фрактал
    if n == 0:
        t.forward(size)
    else:
        icefrackal(n - 1, size / 2)
        t.left(90)
        icefrackal(n - 1, size / 4)
        t.right(180)
        icefrackal(n - 1, size / 4)
        t.left(90)
        icefrackal(n - 1, size / 2)


def icefrackal2(n, size):  # Ледяной фрактал 2
    if n == 0:
        t.forward(size)
    else:
        icefrackal2(n - 1, size / 2)
        t.left(120)
        icefrackal2(n - 1, size / 4)
        t.right(180)
        icefrackal2(n - 1, size / 4)
        t.left(120)
        icefrackal2(n - 1, size / 4)
        t.right(180)
        icefrackal2(n - 1, size / 4)
        t.left(120)
        icefrackal2(n - 1, size / 2)


def branch(n, size):  # Грибанная ветка, не забудь повернуть
    if n == 0:
        t.left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        t.left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)


def koch(n, size): #Кривая Коха
    if n == 0:
        t.forward(size)
    else:
        koch(n - 1, size / 3)
        t.left(60)
        koch(n - 1, size / 3)
        t.right(120)
        koch(n - 1, size / 3)
        t.left(60)
        koch(n - 1, size / 3)


def square(size): #бесконечный квадрат
    if size<0:
        return
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.left(10)
    t.penup()
    t.forward(int(size//10))
    t.pendown()
    square(0.9*size)

def snowlake(size, n): #Снежинка Коха
    if n == 0:
        t.forward(size)
    else:
        snowlake(size / 3, n - 1)
        t.left(60)
        snowlake(size / 3, n - 1)
        t.right(120)
        snowlake(size / 3, n - 1)
        t.left(60)
        snowlake(size / 3, n - 1)
def cycle():
    for i in range(3):
        snowlake(size, n)
        t.right(120)


def choice(funct): #цифра - фрактал
    if funct==1:
        return icefrackal(n, size)
    elif funct==2:
        return icefrackal2(n, size)
    elif funct == 3:
        return branch(n, size)
    elif funct == 4:
        return koch(n, size)
    elif funct == 5:
        return square(size)
    elif funct == 6:
        cycle()
    #elif funct == 7:
    #elif funct == 8:
    #elif funct == 9:


funct=input('Выберите номер фрактала, который нужно нарисовать: \n 1) ледяной фрактал \n 2) ледяной фрактал 2 \n 3) ветка \n 4) кривая Коха \n 5) бесконечный квадрат \n 6) снежинка Коха \n 7) кривая Минковского \n 8) кривая Леви \n 9) фрактал Дракон Хартера-Хейтуэя   ')
t.up()
t.goto(-100, 0)
t.down()
n = int(input('Глубина рекурсии:'))
size = int(input('Длина стороны:'))
choice(funct)
t.speed(100)
t.mainloop()
