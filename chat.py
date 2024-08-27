from datetime import date
from calendar import monthrange

def print_month_calendar(year: int, month: int):
    month_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Get the total number of days in the month
    days_in_the_month = monthrange(year, month)[1]

    # Print the month and year
    print(f"\n> {month_names[month]} {year} <")

    # Print the header for the days of the week
    print("Mo Tu We Th Fr Sa Su")

    # Initialize the date for the first day of the month
    my_date = date(year, month, 1)

    # Determine the day of the week for the first day
    start_day_of_week = my_date.weekday()

    # Print leading spaces for the first week
    print("   " * start_day_of_week, end="")

    # Loop through the days of the month
    for i in range(1, days_in_the_month + 1):
        # Print each day, adjusting the format for single-digit days
        print(f"{i:2d} ", end="")

        # Move to the next line after Saturday
        if (i + start_day_of_week) % 7 == 0:
            print()

    print()  # Add a newline at the end for better formatting

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print_month_calendar(year, month)

main()
