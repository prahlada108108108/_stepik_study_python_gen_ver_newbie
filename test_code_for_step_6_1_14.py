# put your python code here
num=int(input())
num1=num%10
num2=(num//10)%10
num3=num//100
#print (num1, num2, num3)
x1=max(num1,num2,num3)
x2=min(num1,num2,num3)
if (x1-x2)==num1+num2+num3-x1-x2:
    print('Число интересное')
else:
    print('Число неинтересное')


'''
Интересное число
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

Формат входных данных
На вход программе подается целое трехзначное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

945
Sample Output 1:

Число интересное
'''
