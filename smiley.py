#!/usr/bin/env python3

import turtle
import math

cursor = turtle.Turtle()
cursor.speed(0)
cursor.width(5)
cursor.penup()
window = cursor.getscreen()
window.colormode(255)
window.delay(0)

yellow = [247, 226, 109]
maroon = [120, 38, 70]
pink = [240, 196, 217]
black = [5, 6, 8]
white = [255, 255, 255]
gold = [210, 170, 57]

def main():
    turtle.tracer(0, 0) # pause drawing

    origin = [0,0]
    origin_10 = [10, 0]
    cursor.goto(origin)
    circle(origin_10, 150, 1000, cursor, yellow)
    half_cardiod_x(origin, 100, 1000, cursor, maroon, pink)
    half_cardiod_y([-60, 20], 40, 1000, cursor, white)
    half_cardiod_y([70, 20], 40, 1000, cursor, white)
    circle([-45, 75], 20, 1000, cursor, black)
    circle([85, 75], 20, 1000, cursor, black)
    cursor.hideturtle()
    input()

    turtle.update() # show drawing

## draws a circle
def circle(initial, radius, resolution, turt, fill):
    turt.penup()
    position = []
    for t in range(0, resolution):
        position.append([0,0])

        x_coordinate = initial[0] +\
            (radius * math.cos((2.1 * math.pi * t) / (resolution)))

        y_coordinate = initial[1] +\
            (radius * math.sin((2.1 * math.pi * t) / (resolution)))

        position[t][0] = x_coordinate
        position[t][1] = y_coordinate

    turt.color(black, fill)
    for t in range(0, resolution):
        turt.goto(position[t])
        if t == 0:
            turt.pendown()
            turt.begin_fill()

    turt.end_fill()
    turt.penup()

#used to draw a part of an ellipse
def ellipse(initial, a, b, resolution, turt, domain):
    turt.penup()
    position = []
    for t in range(0, resolution):
        position.append([0,0])

        x_coordinate = initial[0] +\
            (a * math.cos((domain * math.pi * t) / (resolution))) - a

        y_coordinate = initial[1] +\
            (b * math.sin((domain * math.pi * t) / (resolution)))

        position[t][0] = x_coordinate
        position[t][1] = y_coordinate

    for t in range(0, resolution):
        turt.goto(position[t])
        if t == 0:
            turt.pendown()

    turt.penup()

## meant to draw a mouth, also known as a cardiod
## note: this function also calls the elipse function to make a tongue
def half_cardiod_x(initial, scale, resolution, turt, fill_1, fill_2):
    turt.penup()
    initial[0] += scale
    turt.goto(initial[0], initial[1])
    position = []
    future = []
    for t in range(0, resolution):
        position.append([0,0])
        x_coordinate = initial[0] +\
            -scale * (1 + math.cos((math.pi * t) / (resolution))) *\
            math.cos((math.pi * t) / (resolution))

        y_coordinate = initial[1] +\
            -scale * (1 + math.cos((math.pi * t) / (resolution))) *\
            math.sin((math.pi * t) / (resolution))

        position[t][0] = x_coordinate
        position[t][1] = y_coordinate
        if (t == (resolution // 4)):
            future.append(position[t])
            t_1 = t
        if (t == (resolution // 2)):
            future.append(position[t])
            begin = position[t]
            t_2 = t

    turt.pendown()
    turt.color(black, fill_1)
    turt.begin_fill()
    for t in range(0, resolution):
        turt.goto(position[t])
    turt.end_fill()

    turt.color(black, fill_2)
    a = abs((future[0][0] - future[1][0]) / (math.cos(7 * math.pi / 6) * 2))
    b = abs((future[0][1] - future[1][1]) / math.sin(7 * math.pi / 6))
    turt.penup()
    turt.goto(future[1])
    turt.begin_fill()

    # We approximate the domain=1.1 value instead of computing the angle where
    # the tongue intersects the mouth.
    ellipse(begin, a, b, resolution, turt, 1.1)

    turt.pendown()
    for t in range(t_1, t_2):
        turt.goto(position[t])
    turt.penup()
    turt.end_fill()

## rotates the cardiod so that two eyes are made
def half_cardiod_y(initial, scale, resolution, turt, fill):
    turt.penup()
    turt.color(black, fill)
    position = []
    for t in range(0, resolution):
        position.append([0,0])
        x_coordinate = initial[0] +\
            scale *\
            (.75 + math.cos(((math.pi * t) / (resolution)) - (math.pi / 2))) *\
            math.cos((math.pi * t) / (resolution))

        y_coordinate = initial[1] +\
            scale *\
            (1 + math.cos(((math.pi * t) / (resolution)) - (math.pi / 2))) *\
            math.sin((math.pi * t) / (resolution))

        position[t][0] = x_coordinate
        position[t][1] = y_coordinate

    for t in range(0, resolution):
        turt.goto(position[t])
        if (t == 0):
            turt.pendown()
            turt.begin_fill()

    turt.goto(position[0])
    turt.penup()
    turt.end_fill()

if __name__ == '__main__':
    main()
