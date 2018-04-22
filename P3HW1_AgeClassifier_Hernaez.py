# CTI-110
# P3HW1 - Age Classifier
# Juan Hernaez
# 03/06/2018

# Define variables

age = int(input("Enter your age: "))

# Calculations

if age > 0 and age <=1:
    print("He or she is an infant.")
elif age > 1 and age <= 13:
    print("He or she is a child.")
elif age >= 13 and age < 20:
    print("He or she is a teenager.")
elif age >= 20:
    print("He or she is an adult.")

# Display the results
