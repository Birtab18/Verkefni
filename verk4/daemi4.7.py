top_num = int(input("Input a number between 0 and 999: "))

for i in range(0,top_num):
    if i < 1000 and i > 99:
        fyrsta = i // 100 
        midju = i // 10 % 10
        sidasta = i % 10
        summa = fyrsta**3 + midju**3 + sidasta**3
        if summa == i:
            print(i)
    elif i < 100 and i > 9:
        fyrri = i // 10
        seinni = i % 10
        summa = fyrri**2 + seinni**2
        if summa == i:
            print (i)
    else:
        print(i)