# put your python code here

n=int(input())
mult=1
sum=0

while n>0:
    for i in range (1,n+1):
        mult*=i
    sum+=mult
    mult=1
    n-=1
print(sum)

'''
Сумма факториалов
Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.

Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до nn, то есть
n!=1\cdot2\cdot3\cdot…\cdot n
n!=1⋅2⋅3⋅…⋅n

Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)

Тестовые данные 🟢
Sample Input 1:

3
Sample Output 1:

9
'''
