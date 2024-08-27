"""def roll_forward(time,hour_to_add,minute_to_add):
    hour, minute = time
    hour = hour + hour_to_add
    minute = minute + minute_to_add 
    if minute >= 60:
        hour += minute // 60
        minute = minute%60
    if hour >= 24: 
        hour = hour%24
    return hour, minute"""

def roll_forward(time,hour_to_add,minute_to_add):
    current_hour, current_min = time
    current_hour += hour_to_add
    current_min += minute_to_add
    if(current_min >= 60):
        current_hour += (current_min//60)
        current_min = current_min%60
    
    if (current_hour == 24):
        current_hour = 0
    elif(current_hour > 24):
        current_hour = current_hour%24
    
    time = current_hour,current_min

    return time


def main():
    time = (00,00)
    hour,minute = time
    print(f"The current time is {hour:02d}:{minute:02d}")

    hour_to_add = int(input("Enter hours to add: "))
    condition = True
 
    while (condition):
        if (hour_to_add) >= 0:
            minute_to_add = int(input("Enter minutes to add: "))
            hour,minute = roll_forward(time,(hour_to_add),(minute_to_add))
            time = hour,minute
            print(f"{hour:02d}:{minute:02d}")
            hour_to_add = int(input("\nEnter hours to add: "))
        else:
            condition = False

if __name__ == "__main__":
        main()