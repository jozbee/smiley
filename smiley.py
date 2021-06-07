import turtle
import math
##from multiprocessing import Process

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
    origin = [0,0]
    origin_10 = [10, 0]
    cursor.goto(origin)
    circle(origin_10, 150, 100, cursor, yellow)
    half_cardiod_x(origin, 100, 100, cursor, maroon, pink)
    half_cardiod_y([-60, 20], 40, 100, cursor, white)
    half_cardiod_y([70, 20], 40, 100, cursor, white)
    circle([-45, 75], 20, 100, cursor, black)
    circle([85, 75], 20, 100, cursor, black)
    cursor.hideturtle()
    input()
##    lines(origin_10, 150, 0, math.pi / 6, 100, gold, black, 10)

## Was meant to be called with multiple instances in a multithreaded process,
## but I couldn't get it to work after a couple of hours so I gave up
def lines(initial, radius, begin_angle, angle_separation, resolution, fill_1, fill_2, turtle_width):
    height = window.window_height() // 2
    width = window.window_width() // 2
##    turtle_2 = turtle.Turtle()
##    turtle_2.speed(0)
    turtle_1 = turtle.Turtle()
    turtle_1.speed(0)
    turtle_1.color(fill_1)
    turtle_1.width(turtle_width)
    window_1 = turtle_1.getscreen()
    window_1.delay(0)
    turtle_1.penup()
    turtle_2 = turtle.Turtle()
    turtle_2.speed(0)
    turtle_2.color(fill_2)
    turtle_2.width(turtle_width)
    window_2 = turtle_2.getscreen()
    window_2.delay(0)
    turtle_2.penup()
    position = []
    for t in range(0, resolution):
        position.append([0, 0, 0])
        x_coordinate = initial[0] + (radius * math.cos(begin_angle + ((2 * math.pi * t) / (resolution))))
        y_coordinate = initial[1] + (radius * math.sin(begin_angle + ((2 * math.pi * t) / (resolution))))
        position[t][0] = x_coordinate
        position[t][1] = y_coordinate
        position[t][2] = begin_angle + ((2 * math.pi * t) / (resolution))
    t = 0
    separation = int((angle_separation * resolution) / (2 * math.pi))
    while(True):
        turtle_1.penup()
        turtle_1.goto(position[t % (resolution)][0], position[t % (resolution)][1])
        turtle_1.right(turtle_1.heading())
        turtle_1.left(math.degrees(position[t % (resolution)][2]))
        turtle_1.pendown()
        position_1 = turtle_1.position()
        while (abs(position_1[0]) <= width and abs(position_1[1]) <= height):
            turtle_1.forward(100)
            position_1 = turtle_1.position()
        turtle_2.penup()
        turtle_2.penup()
        turtle_2.goto(position[t % (resolution) - separation][0], position[t % (resolution) - separation][1])
        turtle_2.right(turtle_2.heading())
        turtle_2.left(math.degrees(position[t % (resolution) - separation][2]))
        turtle_2.pendown()
        position_2 = turtle_2.position()
        while (abs(position_2[0]) <= width and abs(position_2[1]) <= height):
            turtle_2.forward(10)
            position_2 = turtle_2.position()
        turtle_2.penup()
        t += 1
    
## draws a circle
def circle(initial, radius, resolution, turt, fill):
    turt.penup()
    position = []
    for t in range(0, resolution):
        position.append([0,0])
        x_coordinate = initial[0] + (radius * math.cos((2.1 * math.pi * t) / (resolution)))
        y_coordinate = initial[1] + (radius * math.sin((2.1 * math.pi * t) / (resolution)))
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
        x_coordinate = initial[0] + (a * math.cos((domain * math.pi * t) / (resolution))) - a
        y_coordinate = initial[1] + (b * math.sin((domain * math.pi * t) / (resolution)))
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
        x_coordinate = initial[0] + (
                                        -scale *
                                        (1 + math.cos((math.pi * t) / (resolution))) *
                                        math.cos((math.pi * t) / (resolution))
                                    )
        y_coordinate = initial[1] + (
                                        -scale *
                                        (1 + math.cos((math.pi * t) / (resolution))) *
                                        math.sin((math.pi * t) / (resolution))
                                    )
        position[t][0] = x_coordinate
        position[t][1] = y_coordinate
        if (t == (resolution // 4)):
            future.append(position[t])
            t_1 = t
        if (t == (resolution // 2)):
            future.append(position[t])
            begin = position[t]
            t_2 = t
##    print("future =", future)
    turt.pendown()
    turt.color(black, fill_1)
    turt.begin_fill()
    for t in range(0, resolution):
        turt.goto(position[t])
    turt.end_fill()
    turt.color(black, fill_2)
    a = abs (
               (future[0][0] - future[1][0]) / (math.cos(7 * math.pi / 6) * 2)
            )
##    print("a =", a)
    b = abs (
               (future[0][1] - future[1][1]) / math.sin(7 * math.pi / 6)
            )
##    print("b =", b)
##    print("begin =", begin)
##    print("future[0][0] - future[1][0] =", future[0][0] - future[1][0])
##    print("future[0][1] - future[1][1] =", future[0][1] - future[1][1])
    turt.penup()
    turt.goto(future[1])
    turt.begin_fill()
    ellipse(begin, a, b, resolution, turt, 7/6)
    turt.pendown()
    for t in range(t_1, t_2):
        turt.goto(position[t])
    turt.penup()
    turt.end_fill()

## rotates the cardiod so that two eyes are made
def half_cardiod_y(initial, scale, resolution, turt, fill):
    turt.penup()
    turt.color(black, fill)
##    cursor.goto(initial)
##    initial[0] += scale
##    turt.goto(initial[0] - (2 * scale), initial[1])
##    return
    position = []
    for t in range(0, resolution):
        position.append([0,0])
        x_coordinate = initial[0]+ (
                                        scale *
                                        (.75 + math.cos(((math.pi * t) / (resolution)) - (math.pi / 2))) *
                                        math.cos((math.pi * t) / (resolution))
                                    )
        y_coordinate = initial[1] + (
                                        scale *
                                        (1 + math.cos(((math.pi * t) / (resolution)) - (math.pi / 2))) *
                                        math.sin((math.pi * t) / (resolution))
                                    )
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

#calls main
main()
##
##if __name__ == '__main__':
##        p = Process(target = lines, args = ([10, 0], 150, 0, math.pi / 6, 100, gold, black, 10,))
##        p.start()
##        p.join()
##
##
##from multiprocessing import Process
##
##def f(name):
##    print('hello', name)
##
##if __name__ == '__main__':
##    p = Process(target=f, args=('bob',))
##    p.start()
##    p.join()
##








