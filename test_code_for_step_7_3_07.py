# put your python code here
from math import *

n=int(input())
sum=0

for i in range (1,n+1):
    sum=sum+1/i

sum=sum-log(n)
print(sum)

'''
Асимптотическое приближение
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения
\left(1+\dfrac12 + \dfrac13 + \ldots + \dfrac{1}{n} \right) - \ln (n).
(1+ 
2
1
​
  + 
3
1
​
 +…+ 
n
1
​
 )−ln(n).

Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

Тестовые данные 🟢
Sample Input 1:

10
Sample Output 1:

0.6263831609742079
'''
