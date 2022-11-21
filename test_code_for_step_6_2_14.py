# put your python code here

s=input() 
if '@' in s and '.' in s:
    print('YES') 
else:
    print('NO') 
    
'''
Корректный email
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

Формат входных данных
На вход программе подаётся одна строка – email адрес.

Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.

Примечание. Наличие символов @ и . недостаточно для корректности email адреса, однако их отсутствие гарантировано влечёт за собой неверный email.

Тестовые данные 🟢
Sample Input 1:

aaaa@bbb.com
Sample Output 1:

YES
'''
