turns = int(input("input turns: "))

if turns % 2 == 1:
    print("you picked", turns)

for i in range(1, turns+1):
    int(input("input a number: "))