x = int(input("Enter an integer: "))
sum = 0
if x <= 0:
   Output = "Nothing to be printed"
elif x > 0:
    for y in range (x,0,-1):
        sum += y 
        print(y, end=" ")
        Output = (f"\nThe sum is {sum}")

print(Output)