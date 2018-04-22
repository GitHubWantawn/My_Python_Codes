# CTI-110
# P2HW1 - Tip, Tax, Total
# Juan Hernaez
# 02/15/2018
#

foodCost= float(input("Enter cost of food:"))
tipAmount=foodCost*0.18
salesTax=foodCost*0.07
totalCost=foodCost+tipAmount+salesTax

print("The tip is",format(tipAmount,'.2f'))
print ("The sales tax is",format(salesTax,'.1f'))
print("The food cost is", totalCost)
