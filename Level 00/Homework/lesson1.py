from turtle import *
#shape("arrow")
speed (12)
width(6)

#home
color("green")
begin_fill()
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(75)
end_fill()

#door
color("brown")
begin_fill()
left(90)
forward(100)
right(90)
forward (60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

#roof
color("red")
begin_fill()
right(140)
forward(150)
left(100)
forward (150)
end_fill()

penup()
goto(55, 135)
pendown()

color ("white")
begin_fill()
right(50)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(130, 135)
pendown()
color ("white")
begin_fill()
left(180)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

color("orange")
begin_fill()
penup()
goto(-200,200)
pendown()
circle(80)
end_fill()

begin_fill()
penup()
goto(-150,5)
pendown()
forward(50)
left(70)
forward(75)
right(90)
forward(95)
right(90)
forward(75)
right(90)
forward(100)
end_fill()


exitonclick()









