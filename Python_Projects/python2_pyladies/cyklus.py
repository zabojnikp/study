for cislo in range(5):
    print(cislo)

for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
    print(pozdrav + '!')

soucet = 1
for cislo in 8, 45, 9, 21:
    soucet = soucet + cislo

print(soucet)

from turtle import forward, left, exitonclick, penup, pendown

for i in range (20):
    forward(i)
    penup()
    forward(10)
    pendown()

exitonclick()
