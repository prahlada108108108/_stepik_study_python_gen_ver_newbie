# put your python code here
n=int(input())
counter=0

while n>=1:
    while n>=5:
        while n>=10:
            while n>=25:
                counter+=n//25
                n=n%25
                #print(counter, n)
            counter+=n//10
            n=n%10
            #print(counter, n)
        counter+=n//5
        n=n%5
        #print(counter, n)
    counter+=n//1
    n=n%1
print(counter)



'''
Ведьмаку заплатите чеканной монетой
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, \, 5, \, 10, \, 251,5,10,25.

Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.

Формат входных данных 
На вход программе подается одно натуральное число, цена за услугу ведьмака.

Формат выходных данных
Программа должна вывести минимально возможное количество чеканных монет для оплаты.

Тестовые данные 🟢
Sample Input 1:

49
Sample Output 1:

7
'''
