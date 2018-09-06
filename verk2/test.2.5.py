year = int(input("Input a year: ")) # Do not change this line

step4 = True
step5 = False

#step1
if year % 4 == 0:
      # step2
    if year % 100 == 0:
           # step3
        if year % 400 == 0:
            print(step4)
        else:
            print(step5)
    else:
        print(step4)
else:
    print(step5)


