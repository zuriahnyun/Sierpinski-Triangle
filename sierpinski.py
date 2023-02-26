#Author: Zuriahn Yun
#Date:2/18/2023
#Description: Sierspinki Triangle in different colors
import turtle
import sys
import random
import math
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t


def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my

def random_corner(left,right,middle):
    #List for all of the corners
    list = [left,right,middle]
    #Randomly picking from list
    return random.choice(list)
    

def distance(corner, midpoint):
    #Dividing both given functions into points
    cx, xy = corner
    mx, my = midpoint
    #Distance formula
    x = (mx - cx)**2
    y = (my - xy)**2
    distance = math.sqrt(x+y)
    return int(distance)

def color(left,middle,right,midpoint):
    #Absolute value so that negatives will not occur
    red = abs(255 - (distance(middle_corner,m)))
    green = abs(255 - (distance(left_corner,m)))
    blue= abs(255 - (distance(right_corner,m)))
    #If rgb values are higher than 255 an error will occur
    #Rgb values now cap out at 255
    if red>255:
        red = 255
    if green> 255:
        green = 255
    if blue > 255:
        blue = 255
    #Returning rgb values
    rgb = (red,blue,green)
    return rgb


    

def draw(point,colors):
    xx, yy = point
    #Moving to point and adding the color
    t.color(colors)
    t.goto(point)
    #Dot must be 2 or it wont show up 
    t.dot(2)
    
    
    
    
    

if __name__ == "__main__":
    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])
    left_corner = (0,0)
    right_corner= (canv_width,0)
    middle_corner = (canv_width/2,canv_height)
    # Start by calling the turtle_setup function.
    t = turtle_setup(canv_width, canv_height)
    # Then implement the pseudocode below,
    # using the above turtle to color pixels:
    # Chaos game - pseudocode from the assignment handout:
    # p = a random corner of the triangle
    # loop 10000 times:
    #     c = a random corner of the triangle
    #     m = the midpoint between p and c
    #     choose a color for m
    #     color the pixel at m
    #     p=m
    #Random Corner function to find a random corner
    p = random_corner(left_corner,right_corner,middle_corner)
    #Count set to 0 so that it loops 10000 times
    count = 0
    while count != 10000:
        #Finding another random corner
        c = random_corner(left_corner,right_corner,middle_corner)
        #Calling midpoint function to find midpoint
        m = midpoint(p,c)
        #Calling color to get rgb values and input it into draw
        rgb = color(left_corner,right_corner,middle_corner,m)
        #Drawing the dot
        draw(m,rgb)
        p = m
        #Adding to count so it loops correctly
        count+=1
        #Every 2500 Loops Update turtle
        if count % 2500 == 0:
            turtle.update()