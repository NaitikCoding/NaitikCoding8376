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


type = input("type: ")

if type == "triarea":
    triarea()

if type == "sqrarea":
    sqrarea()

if type == "cirarea":
    cirarea()

if type == "recarea":
    recarea()
