"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import array

arr = [3,17,4,82,7]

def median(arr):
    arr.sort()
    x = len(arr)
    if x % 2 == 1:
        return arr[x//2]
    else:
        before = arr[x//2 - 1]
        next = arr[x//2]
        return (before + next)/2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))



 