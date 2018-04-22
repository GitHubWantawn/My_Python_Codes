# CTI-110
# P4HW1 - Distance Traveled
# Juan Hernaez
# 03/23/2018

# Define variables and user input:

speed = int(input("What is the speed of the vehicle in mph? "))
hour = int(input("How many hours has the vehicle traveled? "))

# Calculations:

print("Hour\t\tDistance Traveled")
print("------------------------------------")

for time in range(1,hour+1):
    distance_traveled = speed * time
    print(time,'\t\t',distance_traveled)

