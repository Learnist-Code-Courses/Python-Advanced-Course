#!/usr/bin/env python
import turtle
turtle.Screen().setup(600, 400)

print("We have opened turtle")

pet = turtle.Turtle()
pet.pensize(2)
pet.speed(1)

def build_polygon(sides, length):
    for _ in range(sides):
        pet.forward(length)
        pet.left(360/sides)

build_polygon(3, 200)
build_polygon(3, 400)
pet.forward(200)
build_polygon(3, 200)
pet.left(60)
pet.forward(200)
pet.left(120)
pet.forward(200)


turtle.done()


