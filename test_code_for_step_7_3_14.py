# put your python code here

counter=0

for i in range (1,11):
    n=int(input())
    if n%2!=0:
        counter+=1
if counter>0:
    print('NO')
else:
    print('YES')

'''
Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

Тестовые данные 🟢
Sample Input 1:

2
4
6
8
10
12
14
16
18
20
Sample Output 1:

YES
'''
