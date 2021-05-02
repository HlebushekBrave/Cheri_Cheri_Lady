# Case-study 8
# Raspopova Alexandra (57%)
# Adristi Fauzi (30%)
# Belozertseva Maria (50%)
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


def icefrackal2(n, size):  # Ледяной фрактал версия 2
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


def branch(n, size):  # Ветка
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


def koch(n, size):  # Кривая Коха
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


def square(size):  # Бесконечный квадрат
    if size < 0:
        return
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.left(10)
    t.penup()
    t.forward(int(size // 10))
    t.pendown()
    square(0.9 * size)


def snowlake(size, n):  # Снежинка Коха
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


def minkovsky(n, size):  # Кривая Минковского
    if n == 0:
        t.forward(size)
    else:
        minkovsky(n - 1, size / 4)
        t.left(90)
        minkovsky(n - 1, size / 4)
        t.right(90)
        minkovsky(n - 1, size / 4)
        t.right(90)
        minkovsky(n - 1, size / 2)
        t.left(90)
        minkovsky(n - 1, size / 4)
        t.left(90)
        minkovsky(n - 1, size / 4)
        t.right(90)
        minkovsky(n - 1, size / 4)
    return


def cycle_min():
    minkovsky(n, size)
    t.right(90)


def levi(n, size):  # Кривая Леви
    if n == 0:
        t.forward(size)
    else:
        t.left(45)
        levi(n - 1, size / 2)
        t.right(90)
        levi(n - 1, size / 2)
        t.left(45)


def tree(h, a):
    if h < 30:
        return
    else:
        t.forward(h)
        t.right(a/2)
        tree(3*h/4, a)
        t.left(a)
        tree(3*h/4, a)
        t.right(a/2)
        t.backward(h)

       
def dragon_r(n, size):
    if n == 0:
        t.forward(size/2)
    else:
        dragon_sec(n - 1, size)
        t.right(90)
        dragon_r(n - 1, size)


def dragon_sec(n, size):
    if n == 0:
        t.forward(size/2)
    else:
        dragon_sec(n - 1, size)
        t.left(90)
        dragon_r(n - 1, size)

        
def choice(funct):  # Цифра - фрактал
    if funct == 1:
        return icefrackal(n, size)
    elif funct == 2:
        return icefrackal2(n, size)
    elif funct == 3:
        t.left(90)
        return branch(n, size)
    elif funct == 4:
        return koch(n, size)
    elif funct == 5:
        t.left(90)
        return square(size)
    elif funct == 6:
        return cycle()
    elif funct == 7:
        return cycle_min()
    elif funct == 8:
        return levi(n, size)
    elif funct == 9:
        def dragon_r(n, size)
    elif funct == 10:
        t.left(90)
        h = size
        a = int(input("Введите величину угла: "))
        tree(h, a)


funct = int(input('Выберите номер фрактала, который нужно нарисовать \n1) Ледяной фрактал \n2) Ледяной фрактал 2 \n3) '
                  'Ветка \n4) Кривая Коха \n5) Бесконечный квадрат \n6) Снежинка Коха \n7) Кривая Минковского '
                  '\n8) Кривая Леви \n9) Дракон Хартера-Хейтуэя \n10) Двоичное дерево \nНомер фрактала: '))
t.up()
t.goto(-100, 0)
t.down()
n = int(input('Глубина рекурсии: '))
size = int(input('Длина стороны: '))
choice(funct)
t.speed(100)
t.mainloop()
