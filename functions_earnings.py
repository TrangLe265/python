def compute_earnings(wage: float,hours: int):
    return wage*hours
def main():
    wage = float(input("Enter wage: "))
    hours = int(input("Enter hours: "))

    if 0 < hours <= 40:
        total_earning = compute_earnings(wage,hours)
    elif hours > 40:
        over_time_hours = hours - 40
        over_time_wage = wage * 1.5
        total_earning = compute_earnings(wage,40) + compute_earnings(over_time_wage,over_time_hours)
    else:
        total_earning = 0
    
    print(f"The earnings are {total_earning:.2f}")

main()

