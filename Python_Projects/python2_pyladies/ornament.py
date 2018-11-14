from turtle import forward, right, left, exitonclick, penup, pendown

for i in range (0, 1000, 2):
    forward(i/360)
    left(5)

exitonclick()
