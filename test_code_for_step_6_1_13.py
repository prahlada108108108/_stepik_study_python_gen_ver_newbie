# put your python code here
a,b,c=int(input()),int(input()),int(input())

if a>b:
    if a>c:
        if b>c:
            print(a)
            print(b)
            print(c)
        else:
            print(a)
            print(c)
            print(b)
    else:        
        print(c)
        print(a)
        print(b)
else:        
    if a>c:
        print(b)
        print(a)
        print(c)
    else:        
        if b>c:
            print(b)
            print(c)
            print(a)
        else:
            print(c)
            print(b)
            print(a)


'''
Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

Тестовые данные 🟢
Sample Input 1:

132
129
135
Sample Output 1:

135
132
129
'''
