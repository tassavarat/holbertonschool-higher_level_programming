#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 is 0 and i % 5 is 0:
            print("FizzBuzz", end=" ")
        elif i % 3 is 0:
            print("Fizz", end=" ")
        elif i % 5 is 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
