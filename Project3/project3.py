print()
grade = input("Enter your grade (choose a number between 1-100): ")
grade = int(grade)

if grade >= 90 and grade <= 100:
    letter = "A"
elif grade >= 80 and grade <= 89:
    letter = "B"
elif grade >= 70 and grade <= 79:
    letter = "C"
elif grade >= 60 and grade <= 69:
    letter = "D"
elif grade <= 59:
    letter = "F"

    
print()    
print(f"Your grade is: {letter}\n")    

if grade >= 70:
    print("Congratulations! You've passed!")
else:
    print("Sorry, you have to take the class again.")
print()