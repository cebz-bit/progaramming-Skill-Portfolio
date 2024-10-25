#Exercise 5: Days of the Month
def get_days_in_month():
#Dictionary mapping month numbers to the number of days
    days_in_month = {
        1: 31,   # January
        2: 28,   # February (default)
        3: 31,   # March
        4: 30,   # April
        5: 31,   # May
        6: 30,   # June
        7: 31,   # July
        8: 31,   # August
        9: 30,   # September
        10: 31,  # October
        11: 30,  # November
        12: 31   # December
    }
#Ask the user for the month number
    month = int(input("Enter the month number (1-12): "))
#Check if the month number is valid
    if month in days_in_month:
#leap year for February
        if month == 2:
            year = int(input("Enter the year: "))
#Check for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("February has 29 days in the year", year)
            else:
                print("February has", days_in_month[month], "days in the year", year)
        else:
            print(f"The month {month} has {days_in_month[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
#Run the program
if __name__ == "__main__":
    get_days_in_month()

