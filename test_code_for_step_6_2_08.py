# put your python code here

name1,name2,name3=input(),input(),input()

min1=min(len(name1),len(name2),len(name3))
max1=max(len(name1),len(name2),len(name3))

if min1==len(name1):
    print(name1)
elif min1==len(name2):
    print(name2)
else:
    print(name3)
    
if max1==len(name1):
    print(name1)
elif max1==len(name2):
    print(name2)
else:
    print(name3)    
'''
Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.

Тестовые данные 🟢
Sample Input 1:

Москва
Санкт-Петербург
Екатеринбург
Sample Output 1:

Москва
Санкт-Петербург
'''
