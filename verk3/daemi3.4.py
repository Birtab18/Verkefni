n = int(input("Input an int: ")) # Do not change this line

num = 1

while num > 0:
    if n % num == 0:
        print (num)
    num += 1
    if num > n:
        break