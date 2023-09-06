def equilateral(sides):
    if 0 in sides: return False
    a, b, c = sides
    return a == b == c

def isosceles(sides):
    if 0 in sides: return False
    a, b, c = sides
    return (a == b or b == c or a == c) and (a + b >= c and b + c >= a and c + a >= b)

def scalene(sides):
    if 0 in sides: return False
    a, b, c = sides
    return (a != b and b != c and c != a) and (a + b > c and b + c > a and c + a > b)