from turtle import *


#we want to paint house

#step one draw a square
width (7)
color ("black")

forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)


forward (70)
color ("red")
begin_fill ()
left(90)
forward (120)
right (90)
forward (60)
right (90)
forward (120)
end_fill ()

penup ()
goto (200, 200)
pendown ()


color ("blue")
begin_fill ()
right (150)
forward (200)
left (120)
forward (200)
end_fill ()

penup ()
goto (200, 200)
pendown ()

color ("green")
begin_fill ()
left (30)
forward (60)
right (90)
forward (60)
right (90)
forward (60)
right (90)
forward (60)

end_fill ()

exitonclick ()