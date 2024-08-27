grade_list = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
grade_letter = input("Enter grade letter: ")

count = 0 
for i in range(len(grade_list)):
    if grade_letter == grade_list[i]:
        count += 1

percentage = float(count/(len(grade_list))*100)

print(f"{percentage:.1f} %")