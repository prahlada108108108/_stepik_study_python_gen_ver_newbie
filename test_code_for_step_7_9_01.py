# put your python code here
n=int(input())
counter=0
for i in range (1,n+1):
    for j in range(1,i+1):
        counter+=1
        print(counter,end=' ')
    print()
    
'''
Численный треугольник 3
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.

Тестовые данные 🟢
Sample Input:

3
Sample Output:

1
2 3
4 5 6
Напишите программу. Тестируе
'''