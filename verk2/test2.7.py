age = int(input("Input age: ")) # Do not change this line

ticket_price = 30.0

if age >= 65:
    print(ticket_price * 0.5)
elif age <= 5:
    print(ticket_price * 0.0)
else:
    print(ticket_price)
    
