# 1. Area of Circle -  PI * Radius * Radius (PI = 3.14.....)
# 2. Circumference of Circle - 2 * PI * Radius

import math


def area_of_circle(radius):
    area = math.pi * radius * radius
    return area


def circumference_of_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference


print(f'Area of circle {area_of_circle(5)}')
print(f'Circumference of circle {circumference_of_circle(5)}')
