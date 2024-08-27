female_student = int(input("Enter the number of female students: "))
male_student = int(input("Enter the number of male students: "))
total_student = female_student + male_student

if total_student == 0: 
    print("\nFemale: 0.0 %")
    print("Male: 0.0 %")
else:
    female_percentage = (female_student/total_student * 100)
    male_percentage = (male_student/total_student * 100)
    print(f"\nFemale: {female_percentage:.1f} %")
    print(f"Male: {male_percentage:.1f} %")