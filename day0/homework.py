from turtle import *


#we want to paint house
color("green")
#step 1: draw a square
speed(6)

width(7)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
left(90)


color("brown")
begin_fill()

forward(120)
right(90)


forward(60)
right(90)




forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
begin_fill()
color("blue")
right(150)
forward(200)

left(120)
forward(200)
end_fill()

right(50)
left(120)
color("green")
forward(9)

color("white")
forward(30)

color("red")
left(60)
right(100)
forward(35)
left(90)

forward(35)
left(90)
forward(35)
left(90)
forward(35)


right(180)
forward(17.5)
right(90)
forward(35)
left(90)


forward(17.5)
left(90)
forward(17.5)
left(90)
forward(35)
penup()


goto(200, 200)
pendown()
right(150)
right(120)
right(45)

color("green")
forward(9)
color("white")
forward(30)
color("red")

right(45)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)


left(90)
forward(17.5)
left(90)


forward(35)
right(90)
forward(17.5)
right(90)
forward(17.5)


right(90)
forward(35)
penup()
goto(90, 0)
pendown()
color("green")


begin_fill()
forward(65)
forward(45)
right(90)
left(90)
forward(650)


left(180)
forward(850)
forward(800)
left(90)
forward(850)
left(90)
forward(1650)


left(90)
forward(850)
end_fill()
exitonclick()