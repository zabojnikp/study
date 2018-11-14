from turtle import forward, right, left, exitonclick, penup, pendown
from math import sqrt

#nakresli trojuhelnik
#for i in range(3):
 #   forward(50)
  #  left(120)

#nakresli domecek
for i in range(5):
    forward(50)
    left(135)
    forward(float(sqrt(50**2 + 50**2)))
    right(135)
    forward(50)
    left(135)
    forward(float(sqrt(50**2/2)))
    left(90)
    forward(float(sqrt(50**2/2)))
    left(45)
    forward(50)
    left(135)
    forward(sqrt(50**2 + 50**2))
    right(135)
    forward(50)
    left(90)
    penup()
    forward(50)
    pendown()

exitonclick()