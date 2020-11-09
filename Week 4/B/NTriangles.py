import math


def pythagorean(a, b):
    return math.sqrt(a**2 + b**2)


def solve(a, b, n):
    ratio = a / b
    for i in range(0, n):
        hypotenuse = pythagorean(a, b)
        a = hypotenuse
        b = a*ratio
    return hypotenuse


# if width > length, then the side of the triangle that overlaps the hypotenuse of the previous is the longer side.
# otherwise, it is the shorter side.
length = float(input())
width = float(input())
new_triangles = int(input())

print(solve(length, width, new_triangles))
