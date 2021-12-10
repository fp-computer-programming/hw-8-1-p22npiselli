# Author: Nolan (AMDG) 1/9/2021

def totalpoints(freethrow, twopoint, threepoint):
    totalpoints = 0
    totalpoints = (1 * freethrow) + (2 * twopoint) + (3 * threepoint)
    return totalpoints



print(totalpoints(32,9,13))

print(totalpoints(8,25,32))

print(totalpoints(11,10,13))
