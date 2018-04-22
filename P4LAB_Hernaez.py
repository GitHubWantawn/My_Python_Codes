# CTI-110
# P4LAB - Nested Loops - Snowflake
# Juan Hernaez
# 03/20/2018

import turtle
import random
juan = turtle.Turtle()

turtle.Screen().bgcolor("blue")
colours = ["cyan", "purple", "white", "blue"]

juan.color("orange")

juan.penup()
juan.forward(90)
juan.left(45)
juan.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            juan.forward(30)
            juan.backward(30)
            juan.right(45)
        juan.left(90)
        juan.backward(30)
        juan.left(45)
    juan.right(90)
    juan.forward(90)

for i in range(8):
    branch()
    juan.left(45)

