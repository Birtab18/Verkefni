low = int(input("input lower number: "))
high = int(input("input higher number: "))

for i in range(low,high+1):
     if i % 2 == 1:
        print(i+i)