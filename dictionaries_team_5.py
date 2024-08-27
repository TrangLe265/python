team = {"Ann": "project manager","Jill": "lead developer","John":"software developer", "Susan": "software developer"}
positions = list(team.values())
#positions.sort()
roles = set(positions)
for item in roles: 
    print(item)