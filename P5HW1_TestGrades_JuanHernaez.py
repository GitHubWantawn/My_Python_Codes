# This program asks the user to enter five test grades. The program displays 
# a letter grade for each score, and finally the averages the test scores.
# 04/18/2018
# CTI-110 P5HW1 - Test Averages and Grades
# Juan Hernaez

def main():
    print()

# Perform function to assign letter grade:

def letter_grade(test_score):
    if (test_score in range (90, 101)):
        return "A"
    elif (test_score in range (80, 90)):
        return "B"
    elif (test_score in range (70, 80)):
        return "C"
    elif (test_score in range (60, 70)):
        return "D"
    else:
        return "F"

# Declare loop variables:

test_score_total = 0
num_tests = 5

# The loop runs five times and stores the accumulated test scores for the five
# tests which are passed into the calc_average function:

for test in range(1, num_tests + 1):
    test_score = float(input("Enter the numerical test score for test #{} ".format(test)))
    test_score_total = test_score_total + test_score
    print("The score is: {}. The letter grade is: {} ".format(test_score, letter_grade(test_score)))

# Get average test score and grade:

def calc_average(test_score_total):
    return test_score_total / 5;

# Result:

print("The overall average is: {}.".format(calc_average(test_score_total)))
print("The average letter grade is: {}".format(letter_grade(calc_average(test_score_total))))


main()
