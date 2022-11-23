# put your python code here
from math import *

n,a=int(input()),float(input())

s=(n*pow(a,2))/(4*tan(pi/n))
print(s)



'''
Правильный многоугольник
Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны aa и количеством сторон nn вычисляется по формуле: 
S = \dfrac{n \cdot a^2}{4\tg \left(\dfrac{\pi}{n}\right)}
S= 
4tg( 
n
π
​
 )
n⋅a 
2
 
​
 
Даны два числа: натуральное число nn и вещественное число aa. Напишите программу, которая находит площадь указанного правильного многоугольника.

Формат входных данных
На вход программе подается два числа nn и aa, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественное число – площадь многоугольника.

Тестовые данные 🟢
Sample Input:

3
2.0
Sample Output:

1.7320508075688779
'''
