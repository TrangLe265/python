from pathlib import Path
def load_data(fileName):
    try: 
        path = Path(__file__).resolve().parent
        path = path / fileName
        postoffice = {}
        contents = path.read_text(encoding = "UTF-8")
        lines = contents.splitlines()
        for line in lines: 
            fields = line.split(";")
            postcode = fields[0] 
            postoffice[postcode] = {"postcode":postcode,"fin":fields[1],"swe":fields[2]} 
        return postoffice
    except FileNotFoundError:
        #print(f"\nThe file {fileName} is not found")
        return None

def main(): 
    try:
        fileName = "postcodes.csv"
        new_list = load_data(fileName)
        if new_list is None: 
           print(f"\nThe file {fileName} is not found")
        else: 
            place = input("Enter place name: ").upper() 
            print()
            placefound = False
            for key,value in new_list.items():
                if place == value["fin"] or place == value["swe"]: 
                    print(value["postcode"], place)
                    placefound = True

            if placefound == False:
                print("No postoffice found") 
                   
    except FileNotFoundError:
        print(f"\nThe file {fileName} is not found")

if __name__ == "__main__":
    main()
