# put your python code here
n=int(input())
sum=0
t1=0
t2=0
for i in range (1,n+1):    
    if i==1:
        t1=1
    elif i==2:
        t1=1
        t2=0
    sum=t1+t2
    t2=t1
    t1=sum
    print(str(sum),'',end='')
    
'''
Последовательность Фибоначчи 🌶️
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Фибоначчи.

Формат входных данных
На вход программе подается одно число n\,  (n \le 100)n (n≤100) – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Фибоначчи, отделенные символом пробела.

Примечание. Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих:
1,  \, 1, \,  2, \,  3, \,  5, \,  8, \,  13, \,  21, \,  34, \,  55, \,  89, \ldots
1, 1, 2, 3, 5, 8, 13,  21, 34, 55, 89,…

Тестовые данные 🟢
Sample Input 1:

1
Sample Output 1:

1
'''