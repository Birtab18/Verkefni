# To find the maximum positive integer input by a user and the user repeatedly inputs numbers until a negative value is entered I will:

# First I will ask the user to input a number

# Then I will use a while loop, the loop will run as long as the input number is positive

# Than I will use a if loop to find out which of the input numbers is the maximum number

# Last I will print the maximum number the user input

num_int = int(input("Input a number: "))
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)

