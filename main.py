# SSW-567 - HW00, HW01
# “Write a function classify_triangle() that takes three  parameters: a, b, and c.
# The three parameters represent the lengths of the sides of a triangle.
# The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,
# and whether it is a right triangle as well.”
# Name: Emay Pandarakutty
# Date: 09/10/2021
# email: epandara@stevens.edu

def classify_triangle(a, b, c):
    result = "not determined"
    #Triangle Inequality Theorem:
    # (Sum of any two sides of a triangle is greater than or equal to a third side of a triangle )
    if a+b >= c and a+c >= b and b+c >= a:
        if a == b == c:
            result = "equilateral"
        elif a == b or a == c or b == c:
            result = "isosceles"
        elif ((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((b**2 + c**2) == a**2):
            result = "right"
        else: # a != b and a != c and b != c
            result = "scalene"
    else:
        result = "Not a triangle"

    return result


if __name__ == '__main__':
    #HW00
    print('Hello world')
    #HW01
    print("Demo1-equilateral-classify_triangle(2,2,2)       ==>", classify_triangle(2,2,2))
    print("Demo2-isosceles-classify_triangle(2,2,3)         ==>", classify_triangle(2,2,3))
    print("Demo3-scalene-classify_triangle(1,2,3)           ==>", classify_triangle(1,2,3))
    print("Demo4-right-classify_triangle(3,4,5)             ==>", classify_triangle(3,4,5))
    print("Demo5-Not a triangle-classify_triangle(6,10,17)  ==>", classify_triangle(6,10,17))


