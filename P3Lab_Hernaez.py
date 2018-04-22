# CTI-110
# P3Lab - Debugging
# Juan Hernaez
# 03/06/2018

def main():

    # This program takes a number grade and outputs a letter grade.

    # System uses 10-point grading scale.

    # To do: define scores.
    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    score = int(input("Enter score value: "))

    if score >= A_score:
        print("Your grade is an A.")
    elif score >= B_score:
        print("Your score is a B.")
    elif score >= C_score:
        print("Your grade is a C.")
    elif score >= D_score:
        print("Your grade is a D.")
    else:
        print("Your grade is a F.")

# Program start
main()
