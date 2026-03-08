# Q1 - Conditional Statement
# -----------------------------------------

def check_number():
    # I ask the user to enter a number
    num = float(input("Enter a number: "))

    # Here I check if the number is positive, negative, or zero
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")

# Evidence of experimentation:
# I tested this with numbers like 5, -3, and 0 to make sure
# each condition prints the correct message.


# -----------------------------------------
# Q2 - For Loop (Star Shape)
# -----------------------------------------

def star_shape():
    # Ask user for number of rows
    rows = int(input("Enter number of rows for the star pattern: "))

    # This loop prints increasing stars
    for i in range(1, rows + 1):
        print("*" * i)

# Evidence of experimentation:
# I tested the function with 3 rows and 5 rows to see
# if the triangle pattern changes correctly.


# Q3 - While Loop (Multiples of 3)
# -----------------------------------------

def multiples_of_three():
    # Ask the user for the limit
    limit = int(input("Enter the counting limit: "))

    number = 1

    # The loop runs until number reaches the limit
    while number <= limit:

        # If the number is divisible by 3
        if number % 3 == 0:
            print("Multiple of 3")
        else:
            print(number)

        number += 1

# Evidence of experimentation:
# I tested this with limits like 10 and 15 to check
# if the program correctly replaces multiples of 3.


# Q4 - Sum of Even Numbers in a Range
# -----------------------------------------

def sum_even_numbers():
    # Ask user for start and end values
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    total = 0

    # Loop through the range
    for num in range(start, end + 1):

        # Check if number is even
        if num % 2 == 0:
            total += num

    print("The sum of even numbers is:", total)

# Evidence of experimentation:
# I tested this with ranges like 1–10 and 4–20
# to verify that only even numbers are added.


# Main Program
# -----------------------------------------

check_number()
star_shape()
multiples_of_three()
sum_even_numbers()