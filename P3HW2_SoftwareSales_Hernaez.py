# CTI-110
# P3HW2 - Software Sales
# Juan Hernaez
# 03/06/2018

# Define variables and/or get user input.



# This program asks the user to enter the number of packages purchased
# and then display the amount of the discount and the total purchase cost
# with the discount applied.

# To do: define variables:

quantity = float(input("Please enter the quantity of items purchased: "))
initial_price = 99
initial_price = quantity * 99
discount = 0.10 * initial_price
discount = 0.20 * initial_price
discount = 0.30 * initial_price
discount = 0.40 * initial_price
final_price = initial_price - discount

# Calculations:


if quantity >= 10 and quantity <= 19:
    
    print ("Your initial price is: $",format(initial_price, "0.2f"))
    print ("Your discount is: $",format(discount, "0.2f"))
    print ("Your final price is: $",format(final_price, "0.2f"))
     
elif quantity >= 20 and quantity <= 49:
    print ("Your initial price is: $",format(initial_price, "0.2f"))
    print ("Your discount is: $",format(discount, "0.2f"))
    print ("Your final price is: $",format(final_price, "0.2f"))

elif quantity >= 50 and quantity <= 99:
    print ("Your initial price is: $",format(initial_price, "0.2f"))
    print ("Your discount is: $",format(discount, "0.2f"))
    print ("Your final price is: $",format(final_price, "0.2f"))

else:
    print ("Your initial price is: $",format(initial_price, "0.2f"))
    print ("Your discount is: $",format(discount, "0.2f"))
    print ("Your final price is: $",format(final_price, "0.2f"))

    

    




