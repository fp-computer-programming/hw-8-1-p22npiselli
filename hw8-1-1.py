# Author: Nolan (AMDG) 1/9/2021

def half(string):
    length = len(string)
    half_length = length // 2

    print(string[0:half_length])
    print(string[half_length:length])


half("word")
half("hola")
half("howdy")