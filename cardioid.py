from turtle import *

points=[]
origin1=0.00,-300.00
hideturtle()
Screen().bgcolor("black")
pencolor("blue")
speed(1000000)
width(1)
table=int(numinput("TimeTables","Table : "))
m=400	#modulo with number of points

def draw(modulo):
    for x in range(modulo):
        points.append(pos())
        circle(310, 360 / modulo)
        
        
penup()
goto(origin1)
pendown()
draw(m)

for i in points:
	goto(i)
	goto(points[(points.index(i)*table)%m])
	goto(i)
	
