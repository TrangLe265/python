def print_rectangle(height: int,width: int):
    output = ""
    for x in range(width):    
        output += "*" 
    for y in range(height):
        print(output)

def main():
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))
    print_rectangle(height,width)
main()