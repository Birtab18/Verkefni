a = int(input("input a: "))
b = int(input("input b: "))
choice = int(input("input choice: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
else:
    print("invalid input")