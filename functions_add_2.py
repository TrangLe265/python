def add(no1: float, no2: float):
    sum = no1 + no2 + 0.5
    return (int(sum))
def main():
    no1 = float(input("Enter a float: "))
    no2 = float(input("Enter a float: "))
    print(add(no1,no2))
if __name__ == "__main__":
    main()