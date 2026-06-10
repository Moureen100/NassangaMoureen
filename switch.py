#exercise2:write a program that uses switch case statement to determine day 
# of the week based on a number input (1 for monday, 2 for Tuesday,etc)
#and prints the corresponding day name

day_number = int(input("Enter the number(1-7) to determine day of the week"))
match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7.")