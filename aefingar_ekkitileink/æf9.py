num1 = int(input("input first number: "))
num2 = int(input("input second number: "))
num3 = int(input("input third number: "))

if num3 > num1 < num2:
    print(num1)
elif num1 > num2 < num3:
    print(num2)
elif num1 > num3 < num2:
    print(num3)
else:
    print()