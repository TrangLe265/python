def print_player(tuple):
    team ,name ,goal = tuple
    print (f"{name} ({team}), {goal} goals" ) 

def main(): 
    p = ("Hawks", "Jennifer", 10) 
    print_player(p) 

main() 