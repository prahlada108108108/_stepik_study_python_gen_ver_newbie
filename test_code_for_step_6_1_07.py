# put your python code here
age_d=int(input())

if age_d<=2:
    age_h= age_d*10.5
else:
    age_h=(age_d-2)*4+10.5*2
print(age_h)    

'''
Dog age
На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.

Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.

Формат выходных данных
Программа должна вывести возраст собаки в человеческих годах.

Примечание. В течение первых двух лет собачий год равен 10.510.5 человеческим годам. После этого каждый год собаки равен 4 человеческим годам.

Тестовые данные 🟢
Sample Input 1:

1
Sample Output 1:

10.5
'''
