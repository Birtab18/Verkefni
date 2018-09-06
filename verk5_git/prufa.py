n = int(input("input a number: "))

first = 1
second = 2
third = 3
for i in range(1,n+1):
    if i < 4:
        print(i)
    else: 
        summa = first + second + third
        first = second
        second = third
        third = summa
        print(summa)