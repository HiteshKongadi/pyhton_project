import math

def area_of_circle(radius):
    return math.pi*radius*radius

def area_of_square(length):
    return length*length

def area_of_rectangle(length, breadth):
    return length*breadth

def area_of_trapezoid(base1,base2,height):
    return (base1+base2)*height/2

def module_description():
    print("calculate the area of 2D figures ")