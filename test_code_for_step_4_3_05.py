# put your python code here
a,b,c=int(input()),int(input()),int(input())

if a>b>c or c>b>a:
    print(b)
elif b>a>c or c>a>b:
    print(a)
else:
    print(c)

'''
Среднее число
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

Формат входных данных
На вход программе подаётся три различных целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести среднее число.

Примечание. Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.

Тестовые данные 🟢
Sample Input 1:

1
2
3
Sample Output 1:

2
'''