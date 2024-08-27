from pathlib import Path
fileName = input("Enter file name: ")
try:
    path = Path(fileName)
    contents = path.read_text(encoding="UTF-8")
    print()
    print(contents)   
except FileNotFoundError:
    print(f"\nThe file {fileName} is not found")

