# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    if num == 6 or num == 7:
        print("It's a weekend")
    elif 1<= num <= 5:
        print("It's a weekday")
    else:
        print("Invalid input. Please enter a number between 1 and 7")
    
# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    if num == 1:
        print("It's a Monday")
    elif num == 2:
        print("It's a Tuesday")
    elif num == 3:
        print("It's a Wednesday")
    elif num == 4:
        print("It's a Thursday")
    elif num == 5:
        print("It's a Friday")
    elif num == 6:
        print("It's a Saturday")
    elif num == 7:
        print("It's a Sunday")
    else:
        print("Invalid input. Please enter a number between 1 and 7")

if __name__ == '__main__':
    num = int(input("Check weekday or weekend (enter day number)"))
    check_weekday_or_weekend(num)
    num = int(input("Get day name"))
    get_day_name(num)
