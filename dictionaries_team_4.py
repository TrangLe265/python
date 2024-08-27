team = {"Ann": "project manager","Jill": "lead developer","John":"software developer", "Susan": "software developer"}

name = input("Enter name (quit ends): ")
condition = True

while condition == True: 
    if (name != "quit"):
        role = input("Enter role: ")
        if name in team: 
            team[name]= role
        else:
            team[name] = role

        name = input("\nEnter name (quit ends): ")
    else: 
        condition = False

print()
sorted_team = dict(sorted(team.items()))
for name,role in sorted_team.items():
    print(f"{name:8s}{role}")