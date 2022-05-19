print("The area is the length of a side squared.")
side = float(input("What is the length of a side of the square you want to calculate? "))
print()
area = side ** 2
print(f"The area of the square is: {area}")
print()
print("The area is the length multiplied by the width.")
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print()
print(f"The area of the rectangle is: {area}")
print("The area is Pi multiplied by the radius squared.")
print()
from cgi import print_form
from cmath import pi
import math
radius = float(input("What is the radius of the circle? "))
area = pi * (radius ** 2)
area_round = round(area, 2)
print(f"The area of the circle is: {area_round}")
print()

numX = float(input("Enter a number please: "))
print()
SquareArea = numX ** 2
SquareArea_round = round(SquareArea, 2)
print()
CircleArea = pi * (numX ** 2)
CircleArea_round = round(CircleArea, 2)
print()
CubeVolume = numX ** 3
CubeVolume_round = round(CubeVolume, 2)
print()
SphereVolume = (4/3) * pi * (numX ** 3)
SphereVolume_round = round(SphereVolume, 2)
print()
print(f"The area of the square is: {SquareArea_round}")
print()
print(f"The area of the circle is: {CircleArea_round}")
print()
print(f"The volume of the cube is: {CubeVolume_round}")
print()
print(f"The volume of the sphere is: {SphereVolume_round}")
print()
#----------------------------------------------------------------------------------
#!STRECH 3 START
side = float(input("What is the length of a side of the square in centimeters? "))
areaCM_sqr = side ** 2
areaCM_sqr_round = round(areaCM_sqr, 2)
print(f"The area of the square in square centimeters  is: {areaCM_sqr_round}")
print()

areaMTS_sqr = areaCM_sqr / 10000
areaMTS_sqr_round = round(areaMTS_sqr, 2)
print(f"The area of the square in square meters is: {areaMTS_sqr_round}")
print()

lengthCM_tri = float(input("What is the length of rectangle in centimeters? "))
widthCM_tri = float(input("What is the width of the rectangle in centimeters? "))

areaCM_tri = lengthCM_tri * widthCM_tri
areaCM_tri_round = round(areaCM_tri, 2)
print(f"The area of the rectangle in square centimeters is: {areaCM_tri_round}")
print()

areaMTS_tri = areaCM_tri / 10000
areaMTS_tri_round = round(areaMTS_tri, 2)
print(f"The area of the rectangle in square meters is: {areaMTS_tri_round}")
print()

radius = float(input("What is the radius of the circle in centimeters? "))
areaCM_cir = pi * (radius ** 2)
areaCM_cir_round = round(areaCM_cir, 2)
print(f"The area of the circle in square centimeters is: {areaCM_cir_round}")
print()

areaMTS_circ = areaCM_cir / 10000
areaMTS_circ_round = round(areaMTS_circ, 2)
print(f"The area of the circle in square meters is: {areaMTS_circ_round}")
#!STRECH 3 END
#----------------------------------------------------------------------------------

