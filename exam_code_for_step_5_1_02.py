# put your python code here
col1,row1,col2,row2=int(input()),int(input()),int(input()),int(input())

if col1%2 !=0:
    if row1%2!=0:
        paint1='white'
    else:
        paint1='black'
elif col1%2 ==0:
    if row1%2!=0:
        paint1='black'
    else:
        paint1='white'
        
if col2%2 !=0:
    if row2%2!=0:
        paint2='white'
    else:
        paint2='black'
elif col2%2 ==0:
    if row2%2!=0:
        paint2='black'
    else:
        paint2='white'        

if paint1==paint2:
    print('YES')
else:
    print('NO')

    
'''
Шахматная доска
Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.



Тестовые данные 🟢
Sample Input 1:

1
1
2
6
Sample Output 1:

YES
'''
