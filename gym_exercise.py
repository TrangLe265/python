visit_per_year = int(input("Enter the number of days of gym visits per year: "))
day_pass_price = float(input("Enter price for a day pass: "))
membership_fee = float(input("Enter yearly membership fee: "))

buying_day_pass = visit_per_year * day_pass_price
difference = membership_fee - buying_day_pass

if difference == 0: 
    print("\nThere is no price difference")
elif difference > 0:
    print(f"\nBuying day passes is {difference:.2f} euros cheaper")
else:
    difference = - (difference)
    print(f"\nPaying the yearly membership fee is {difference:.2f} euros cheaper")