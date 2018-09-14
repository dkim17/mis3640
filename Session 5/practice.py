import turtle
import math

jack = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
# polyline(jack, 3, 100,30)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def circle(t,r):
    arc(t,r,360)

#1.
circle(jack, 100)
jack.up()
jack.goto(0,100)
jack.down()
jack.lt(60)
arc(jack, 100 , 60)
jack.lt(120)
arc(jack, 100 , 60)

jack.lt(60)
arc(jack, 100 , 60)
jack.lt(120)
arc(jack, 100 , 60)

jack.lt(240)
arc(jack, 100 , 60)
jack.lt(120)
arc(jack, 100 , 60)

jack.rt(60)
arc(jack, 100 , 60)
jack.lt(120)
arc(jack, 100 , 60)

jack.rt(360)
arc(jack, 100 , 60)
jack.lt(120)
arc(jack, 100 , 60)

jack.rt(540)
arc(jack, 100 , 60)
jack.lt(120)
arc(jack, 100 , 60)
turtle.mainloop()

#2.
jack.circle(100)
jack.up()
jack.goto(0, 100) 
jack.down()
jack.circle(50, 180)
jack.up()
jack.goto(0, 100)  
jack.down()
jack.circle(50, 180)
jack.up()
jack.goto(0, 35)  
jack.down()
jack.circle(20)
jack.up()
jack.goto(0, 125)  
jack.down()
jack.circle(20)

turtle.mainloop()