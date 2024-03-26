# Using a function and variables entered from the keyboard
# Write a program that calculates the area of a triangle of base=2, and height=3.
# Formula A = 1/2 x b x h

#Approach One
def areaOfTriangle():

    base = int(input('\nEnter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))

    area = (1/2) * base * height

    print(f"The area of a triangle of base {base} and height {height} is {area:.2f}")

#areaOfTriangle()



#Approach Two

base = int(input('\nEnter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))

def areaOfTriangleApproachTwo(b,h):

    area = (1/2) * b * h

    print(int(area))

areaOfTriangleApproachTwo(base,height)

