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
            postoffice[postcode] = {"fin":fields[1],"swe":fields[2]} 
        return postoffice
    except FileNotFoundError:
        #print(f"\nThe file {fileName} is not found")
        return None

def main():
    fileName = input("Enter postcode file name: ")
    try:     
        postoffice = load_data(fileName)#dictionary of pc and pp    
        if postoffice is None: 
            print(f"\nThe file {fileName} is not found")
        else:
            print(f"{len(postoffice)} rows") 
            postcode = input("\nEnter postcode: ") 
            if postcode not in postoffice: 
                print("Unknown postcode")
            else:
                print(postcode ,postoffice[postcode]["fin"] )
                print(postcode, postoffice[postcode]["swe"]) 

    except FileNotFoundError:
        print(f"\nThe file {fileName} is not found")
            

if __name__ == "__main__":
    main()
