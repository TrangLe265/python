try:
    user_input = input("Enter a weekday number: ")
    user_input = int(user_input)
    if 1 <= user_input <= 7: 
        print("OK")
    else:
        print("Please enter an integer between 1 and 7")
except ValueError:
    print("Please enter an integer between 1 and 7")
