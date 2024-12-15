# 1. Area of Circle -  PI * Radius * Radius (PI = 3.14.....)
# 2. Circumference of Circle - 2 * PI * Radius

import math

def details_of_circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference #Returning 2 variables/data. Multiple return values

circle_area, circle_circumference = details_of_circle(5)
#Values will be assigned based on the order of variables in return statements

print(f'Area of circle is {circle_area} \nCircumference of circle is {circle_circumference}')
