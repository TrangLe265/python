team = {"John":"software developer", "Ann": "project manager", "Susan": "software developer","Jill": "lead developer"}

name = input("Enter name (quit ends): ")
condition = True

while condition == True: 
    if (name != "quit"):
        if name in team: 
            print(name,"is a",team[name])
        else:
            print(name,"is not in the team")
        name = input("\nEnter name (quit ends): ")
    else: 
        condition = False
