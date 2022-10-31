#!/usr/bin/env python
import turtle
turtle.Screen().setup(600, 400)

pet = turtle.Turtle()
pet.pensize(2)
pet.speed(1)
letter_spacing = 30

def m(length):
    pet.left(90)
    pet.forward(length)
    pet.right(150)
    pet.forward(length)
    pet.left(180)
    pet.right(60)
    pet.forward(length)
    pet.right(150)
    pet.forward(length)

    pet.penup()
    pet.left(90)
    pet.forward(letter_spacing)
    pet.pendown()

def a(length):
    pet.left(60)
    pet.forward(length)
    pet.left(180)
    pet.left(60)
    pet.forward(length)
    pet.left(180)
    pet.forward(length/2)
    pet.left(60)
    pet.forward(length/2)

    pet.left(180)
    pet.forward(length/2)
    pet.right(60)
    pet.forward(length/2)
    
    pet.penup()
    pet.left(60)
    pet.forward(letter_spacing)
    pet.pendown()


m(60)
a(60)
m(60)
m(60)
a(60)

turtle.done()

