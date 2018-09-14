import turtle
import math


jack = turtle.Turtle()

# for i in range(4):
#     jack.fd(100)
#     jack.lt(90)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# square(jack,100)


#3
# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)

#4
# def circle(t, r):
#     circumference = 2* math.pi * r
#     n= int(circumference/3)+1
#     length = circumference / n
#     polygon(t, n, length)

jack = turtle.Turtle()

# circle(jack, 150)

#5
# polygon(t=jack, n = 7, length=70)


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
circle(jack, 100)

turtle.mainloop()
