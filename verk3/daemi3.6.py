number = 10

while number < 100:
    three_digits = number * number
    last_two = three_digits % 100
  
    if last_two == number:
        print(number)
        break
        
    number += 1