# Author: Nolan (AMDG) 1/9/2021

def sorting(my_string):
    my_list = list(my_string)
    sorted_list = my_list.copy()
    sorted_list.sort()

    if sorted_list == my_list:
        print("This list is sorted.")
    else:
        print("This list is not sorted.")


sorting("abcd")
sorting("cabd")
sorting("lamc")