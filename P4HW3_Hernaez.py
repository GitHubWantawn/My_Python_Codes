# CTI-110
# P4HW3 - Factorial
# Juan Hernaez
# 03/20/2018

# Define variables:

n_factorial = 1
end = int(input("Enter the number to calculate the factorial: "))

# Calculations:

while end < 0:
    print("You've entered a incorrect number.")
    print("Please enter a nonnegative number.")
    end = int(input("Enter the number to claculate the factorial."))

for factor in range (1,end+1):
    n_factorial = n_factorial * factor

print("The factorial is: ", n_factorial)

# Display the results:
