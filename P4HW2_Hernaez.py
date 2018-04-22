# CTI-120
# P4HW2 - Running Total
# Juan Hernaez
# 03/23/2018

# User input:

total = 0
end = int(input("How many students do you have? "))

print("The running total is: ")

for stu in range (1, end+1):
    print("Student # ",stu)
    score = int(input("Enter student's score: "))

    print("The running total number is: ")

    while score < 0:
        print("You've entered a negative score. Please enter the score again.")
        score = int(input("enter student's score: "))

    if score >= 90:
        print("Your grade is an A.")
        
    elif score >= 80:
        print("Your grade is a B.")

    elif score >= 70:
        print("Your grade is a C.")

    elif score >= 60:
        print("Your grade is a D.")

    else:
        print("Your grade is a F.")

    total = total + score

    print("The total score is", total)
        
        
