gig = int(input("Number of gigs:"))
one_set_usage = int(input("Gigs to be played with the same set of strings: "))
price_one_set = float(input("Price of a set of guitar strings: "))

if gig == 0:
    set_needed = 0
    total_cost = 0
elif (gig <= one_set_usage):
    set_needed = 1 
    total_cost = price_one_set
else:
    if (gig % one_set_usage) > 0:
        set_needed = 1+ gig//one_set_usage
        total_cost = float(price_one_set*set_needed)
    elif (gig % one_set_usage) == 0:
        set_needed = gig//one_set_usage
        total_cost = float(price_one_set*set_needed)

print(f"\nThe guitarist needs {set_needed} new sets of guitar strings")
print(f"The total cost is {total_cost:.2f} euros")