#Мы долбанемся с этой прогой
import turtle as t


def icefrackal(n, size): #Ледяной фрактал
    if n == 0:
        t.forward(size)
    else:
        icefrackal(n-1, size/2)
        t.left(90)
        icefrackal(n-1, size/4)
        t.right(180)
        icefrackal(n-1, size/4)
        t.left(90)
        icefrackal(n-1, size/2)

        
 def icefrackal2(n, size): #Ледяной фрактал 2
    if n == 0:
        t.forward(size)
    else:
        icefrackal2(n-1, size/2)
        t.left(120)
        icefrackal2(n-1, size/4)
        t.right(180)
        icefrackal2(n-1, size/4)
        t.left(120)
        icefrackal2(n-1, size/4)
        t.right(180)
        icefrackal2(n-1,size/4)
        t.left(120)
        icefrackal2(n-1, size/2)


def branch(n, size):
    if n == 0:
        t.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)


def main():
    t.up()
    t.goto(-100, 0)
    t.down()
    n = int(input('Глубина рекурсии:'))
    size = int(input('Длина стороны:'))
    icefrackal(n, size)


main()
t.speed(100)
t.mainloop()
