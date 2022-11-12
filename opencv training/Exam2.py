'''
This is your Exam 2 programming problem
Read and complete the instructions below

Instructions:
For this programming problem you will write the following function

calcShape - This function takes in a numerical value (can be decimal)
    representing the perimeter of a shape. The shape is determined by
    a single character passed in corresponding to the shapes below:

        NOTE: in geometry, a regular polygon is one where all sides are equal and all interior angles are equal
        c = circle
        t = regular 3-sided polygon (triangle)
        s = regular 4-sided polygon (square)
        p = regular 5-sided polygon (pentagon)
        h = regular 6-sided polygon (hexagon)


    The function returns a tuple containing the area and the ratio of the perimeter to the area.
    NOTE: To help you out, I am giving you the formula for a regular triangle: (s**2) * (3**(1/2)) / 4
    NOTE: In the above formulate side = 1/3 the total perimeter
    NOTE: All of the formulas can be done withouot trig
        Search hint example: area of regular pentagon using only side
        NOTE: Many mathematical notations will use lowercase 'a' to represent the side length of a regular polygon

    Thus the following:
        calcShape(3,'t')
    would return:
        (0.4330127018922193, 6.92820323027551)

    The only import you may have is:
        from math import pi
    so that you can use a full pi value for any necessary calculations

    Remember, I am not asking you to print out the values, I am asking you to return a tuple with the area and perimeter/area ratio.
'''

#1.73205080757 heres root 3, its super useful.
#also cuz I cant use sqrt without importing math
from math import pi

def calcShape (p,sides = "a"):

    if sides == 'c' or sides == 'C':
        r = p/(2*pi)
        a = pi*(r**2)
    elif sides == 't' or sides == 'T':
        s = p / 3
        a = (1.73205080757 / 4) * s ** 2
    elif sides == 's' or sides == 'S':
        s = p / 4
        a = s ** 2
    elif sides == 'p' or sides == 'P':
        s = p / 5
        a = s*1.72047740059
    elif sides == 'h' or sides == 'H':
        s = p / 6
        a = (3*1.73205080757/2)*(s**2)
    return (a,p/a)




#test function
print (calcShape(5, 'p'))

