# put your python code here
num=int(input())

if num%2!=0:
    print('YES')
else:
    if 2<=num<=5:
        print('NO')
    elif 6<=num<=20:
        print('YES')
    elif 20<num:
        print('NO')   

'''
YES or NO вот в чем вопрос
Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».

Условия:

если число нечётное, то вывести «YES»;
если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
если число чётное и больше 20, то вывести «NO».
Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

1
Sample Output 1:

YES
'''