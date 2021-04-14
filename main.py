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
