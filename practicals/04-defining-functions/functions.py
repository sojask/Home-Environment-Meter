from math import *

log = log2(1024)
root = sqrt(2401)
print(log)
print(root)

def displayTwice(msg):
    print(msg)
    print(msg)


displayTwice('Hello World!')
displayTwice('SASKA YOU MADE IT')

def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
        max = a
    else:
        max = b
    return max


findMax(20,50)
print(findMax(6,7))