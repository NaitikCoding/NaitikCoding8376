import math
from functools import reduce


def triarea():
    height = int(input("hight: "))
    breadth = int(input("bredth: "))
    area = (1/2) * height * breadth
    print(area)


def sqrarea():
    height = int(input("hight: "))
    area = height * 2
    print(area)


def recarea():
    height = int(input("hight: "))
    breadth = int(input("bredth: "))
    area = height * breadth
    print(area)


def cirarea():
    radius = int(input("radius: "))
    area = math.pi * radius * radius
    print(area)

def prime():
    n = int(input("primes till: "))

    primes = reduce(lambda r, x: r - set(range(x**2, n, x))
                    if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))

    print(primes)


def CtoF():
    C = float(input("celsius= "))
    F = (C * 1.8) + 32
    print(F)


def FtoC():
    F = float(input("Fahrenheit= "))
    C = (F - 32) * (5/9)
    print(C)


type = input("type: ")


if type == "triarea":
    triarea()

if type == "sqrarea":
    sqrarea()

if type == "cirarea":
    cirarea()

if type == "recarea":
    recarea()

if type == "C to F":
    CtoF()

if type == "F to C":
    FtoC()

if type == "prime":
    prime()
