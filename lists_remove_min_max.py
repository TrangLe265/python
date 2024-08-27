def remove_min_max(list):
    if len(list) == 0:
        list = []
    elif len(list) == 1:
        list.remove(max(list))
    else: 
        list.remove(max(list))
        list.remove(min(list))
      
def main():     
    a = [3, 1, 4, 1, 5]     
    remove_min_max(a)     
    print(a)  

if __name__ == "__main__":
        main() 