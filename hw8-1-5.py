# Author: Nolan (AMDG) 1/9/2021

def perimeter(length, width):
    '''Returns the perimeter given length and width.'''
    perimeter = 2 * (length + width)
    return (perimeter)


print(perimeter(20, 40) == 120)
print(perimeter(45, 75) == 240)
print(perimeter(90, 20) == 220)

