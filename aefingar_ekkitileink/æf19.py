low = int(input("input lower number"))
high = int(input("input higher number: "))

if low < high:
    for i in range(low,high+1):
        print(i)