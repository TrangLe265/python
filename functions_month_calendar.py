from datetime import date
from calendar import monthrange

def print_month_calendar(year: int, month: int):
    month_names = ["", "January", "February", "March", "April", "May","June",      "July", "August", "September", "October", "November", "December"] 
    print(f"\n> {month_names[month]} {year} <")
    print("Mon Tues Wed Thu Fri Sat Sun")

    days_in_the_month = monthrange(year,month)[1]
    my_date = date(year,month,1)

    start_of_the_week = my_date.weekday()
   
    print("    "* start_of_the_week, end ="") 

    for x in range(1,days_in_the_month+1):
        print(f"{x:4d}", end ="")
        if (x + start_of_the_week)%7 == 0:
            print("\n")
        

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print_month_calendar(year,month)
    
main()