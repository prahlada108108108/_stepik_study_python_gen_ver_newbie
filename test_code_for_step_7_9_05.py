# put your python code here
n=int(input())
sum1=0

while n>0:        
    while n>0:
        sum1+=n%10
        n//=10
    n=sum1
    sum1=0
    if n<10:
        break
print(n)
'''
Цифровой корень
На вход программе подается натуральное число nn. Напишите программу, которая находит цифровой корень данного числа. Цифровой корень числа nn получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести цифровой корень введенного числа.

Примечание. Используйте вложенные циклы while.

Тестовые данные 🟢
Sample Input:

192
Sample Output:

3
'''