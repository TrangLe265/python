def print_pyramid(height: int):
    foundation = height * 2 -1
    for i in range(1,foundation + 1,2):
        print(" " * int((foundation - i)/2) + "*" * i) 
def main():
    user_input = int(input("Enter pyramid height: "))
    print_pyramid(user_input)
main()
