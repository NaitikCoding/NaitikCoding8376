import math


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
