#!/usr/bin/env python
import turtle
turtle.Screen().setup(600, 400)

pet = turtle.Turtle()
pet.pensize(2)
pet.speed(1)
letter_spacing = 20


def end_letter(start_pos, debug=False):
    if debug:
        pet.pencolor("blue")
    else:
        pet.penup()

    pet.seth(0)  # set angle to 0
    pet.setpos(start_pos)
    pet.forward(letter_spacing)

    if debug:
        pet.pencolor("black")
    else:
        pet.pendown()


def debug_size_lines(length):
    # lower line
    pet.speed(10)
    pet.penup()
    pet.setpos(0, -3)
    pet.pendown()
    pet.forward(1000)

    # Upper line determined by length + 3 input like any other character
    pet.penup()
    pet.setpos(0, length+3)
    pet.pendown()
    pet.forward(1000)

    # Return to starting pos
    pet.penup()
    pet.setpos(0, 0)
    pet.pendown()
    pet.speed(1)


def a(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length/4*3)
    pet.right(45)
    pet.forward(length/3)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/3)
    pet.right(45)
    pet.forward(length/4*3)

    pet.left(180)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/3*2)

    end_letter(start_pos)
    return "A"


def b(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second Stroke
    pet.right(90)
    pet.forward(length/3)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/3)

    # Third stroke
    pet.right(180)
    pet.forward(length/2.5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/4)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/2.5)

    # End and prepare for next letter
    end_letter(start_pos)
    return "B"


def c(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.left(90)
    pet.penup()
    pet.forward(length)
    pet.right(90)
    pet.forward(length/3*2)
    pet.right(180)
    pet.pendown()

    # First stroke
    pet.forward(length/2)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/1.9)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "C"


def d(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.right(90)
    pet.forward(length/3*1.1)
    pet.right(45)
    pet.forward(length/3)
    pet.right(45)
    pet.forward(length/2)
    pet.right(45)
    pet.forward(length/3)
    pet.right(45)
    pet.forward(length/3*1.1)

    # End and prepare for next letter
    end_letter(start_pos)
    return "D"


def e(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.right(90)
    pet.forward(length/3*2)
    pet.left(180)
    pet.forward(length/3*2)

    # Third stroke
    pet.left(90)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/2)
    pet.left(180)
    pet.forward(length/2)

    # Fourth stroke
    pet.left(90)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/3*2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "E"


def f(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.right(90)
    pet.forward(length/3*2)
    pet.left(180)
    pet.forward(length/3*2)

    # Third stroke
    pet.left(90)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/2)
    pet.left(180)
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "F"


def g(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.left(90)
    pet.penup()
    pet.forward(length)
    pet.right(90)
    pet.forward(length/3*2)
    pet.right(180)
    pet.pendown()

    # First stroke
    pet.forward(length/2)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/1.9)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "G"


def h(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.left(180)
    pet.forward(length/2)
    pet.left(90)
    pet.forward(length/2*1.2)

    # Third stroke
    pet.left(90)
    pet.forward(length/2)
    pet.left(180)
    pet.forward(length)

    # End and prepare for next letter
    end_letter(start_pos)
    return "H"


def i(length):
    start_pos = pet.pos()

    # First stroke
    pet.forward(length/2*1.2)
    pet.left(180)
    pet.forward(length/2*1.2/2)

    # Second stroke
    pet.right(90)
    pet.forward(length)

    # Third storke
    pet.left(90)
    pet.forward(length/2*1.2/2)
    pet.left(180)
    pet.forward(length/2*1.2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "I"


def j(length):
    start_pos = pet.pos()

    # First stroke
    pet.forward(length/2*0.9)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # Second stroke
    pet.forward(length/3*2.2)

    # Third storke
    pet.left(90)
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "J"


def k(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.left(180)
    pet.forward(length/2)
    pet.left(135)
    pet.forward(length/3*2)
    pet.left(180)
    pet.forward(length/2)

    # Third stroke
    pet.left(85)
    pet.forward(length/4*3)

    # End and prepare for next letter
    end_letter(start_pos)
    return "K"


def l(length):  # noqa: E743, E741 (ambigous function name)
    start_pos = pet.pos()

    # First stroke
    pet.forward(length/2*1.2)
    pet.left(180)
    pet.forward(length/2*1.2)

    # Second stroke
    pet.right(90)
    pet.forward(length)

    # End and prepare for next letter
    end_letter(start_pos)
    return "L"


def m(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.right(150)
    pet.forward(length/1.5)

    # Third stroke
    pet.left(120)  # changed to only turn 120 from 180 and turning right for 60
    pet.forward(length/1.5)

    # Fourth Stroke
    pet.right(150)
    pet.forward(length)

    # End and prepare for next letter
    end_letter(start_pos)
    return "M"


def n(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.right(150)
    pet.forward(length*1.15)

    # Third stroke
    pet.left(150)
    pet.forward(length)

    # End and prepare for next letter
    end_letter(start_pos)
    return "N"


def o(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.forward(length/5)
    pet.pendown()

    # First quarter
    pet.forward(length/4)  # bottom
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # First quarter
    pet.forward(length/2)  # left side
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # First quarter
    pet.forward(length/3)  # top
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # First quarter
    pet.forward(length/2)  # left
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/4)

    # End and prepare for next letter
    end_letter(start_pos)
    return "O"


def p(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second Stroke
    pet.right(90)
    pet.forward(length/2.5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/2.5)

    # End and prepare for next letter
    end_letter(start_pos)
    return "P"


def q(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.forward(length/5)
    pet.pendown()

    # First quarter
    pet.forward(length/4)  # bottom
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # First quarter
    pet.forward(length/2)  # left side
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # First quarter
    pet.forward(length/3)  # top
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    # First quarter
    pet.forward(length/2)  # left
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/4)

    # Q stripe
    pet.penup()
    pet.left(90)
    pet.forward(length/3)
    pet.right(90)
    pet.forward(length/10)
    pet.right(45)
    pet.pendown()
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "Q"


def r(length):
    start_pos = pet.pos()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second Stroke
    pet.right(90)
    pet.forward(length/2.5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/2.5)

    # Third stroke
    pet.left(135)
    pet.forward(length/1.8)

    # End and prepare for next letter
    end_letter(start_pos)
    return "R"


def s(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.left(90)
    pet.penup()
    pet.forward(length)
    pet.right(90)
    pet.forward(length/3*2)
    pet.right(180)
    pet.pendown()

    # First stroke
    pet.forward(length/2)
    pet.left(45)
    pet.forward(length/5)
    pet.left(45)
    pet.forward(length/5)
    pet.left(45)
    pet.forward(length/5)
    pet.left(45)
    pet.forward(length/3)

    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/4)
    pet.right(45)
    pet.forward(length/5)
    pet.right(45)
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "S"


def t(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.forward(length/2*1.2/2)
    pet.pendown()

    # First stroke
    pet.left(90)
    pet.forward(length)

    # Second stroke
    pet.right(90)
    pet.forward(length/2*1.7/2)
    pet.left(180)
    pet.forward(length/2*1.7)

    # End and prepare for next letter
    end_letter(start_pos)
    return "T"


def u(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.left(90)
    pet.forward(length)
    pet.left(180)
    pet.pendown()

    # First stroke
    pet.forward(length/4*3)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)

    pet.forward(length/4)
    pet.left(45)
    pet.forward(length/3)
    pet.left(45)
    pet.forward(length/4*3)

    # End and prepare for next letter
    end_letter(start_pos)
    return "U"


def v(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.left(90)
    pet.forward(length)
    pet.left(180)
    pet.pendown()

    # First stroke
    pet.left(20)
    pet.forward(length)
    pet.left(140)
    pet.forward(length)

    # End and prepare for next letter
    end_letter(start_pos)
    return "V"


def w(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.left(90)
    pet.forward(length)
    pet.left(180)
    pet.pendown()

    # First stroke
    pet.left(10)
    pet.forward(length)
    pet.left(150)
    pet.forward(length/2)
    pet.right(150)
    pet.forward(length/2)
    pet.left(160)
    pet.forward(length)

    # End and prepare for next letter
    end_letter(start_pos)
    return "W"


def x(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.left(90)
    pet.forward(length)
    pet.left(180)
    pet.pendown()

    # First stroke
    pet.left(25)
    pet.forward(length*1.1)

    pet.penup()
    pet.left(155)
    pet.forward(length)
    pet.pendown()

    # Second stroke
    pet.left(155)
    pet.forward(length*1.1)

    # End and prepare for next letter
    end_letter(start_pos)
    return "X"


def y(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.left(90)
    pet.forward(length)
    pet.left(180)
    pet.pendown()

    # First stroke
    pet.left(25)
    pet.forward(length*1.1/2)

    # Second stroke
    pet.left(125)
    pet.forward(length*1.1/2)
    pet.left(180)
    pet.forward(length*1.1/2)

    # Third stroke
    pet.left(25)
    pet.forward(length/2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "Y"


def z(length):
    start_pos = pet.pos()

    # Postion before first stroke
    pet.penup()
    pet.left(90)
    pet.forward(length)
    pet.right(90)
    pet.pendown()

    # First stroke
    pet.forward(length/3*2)

    # Second stroke
    pet.right(125)
    pet.forward(length*1.2)

    # Third stroke
    pet.left(125)
    pet.forward(length/3*2)

    # End and prepare for next letter
    end_letter(start_pos)
    return "Z"


def space():
    start_pos = pet.pos()
    # End and prepare for next letter
    end_letter(start_pos)
    return '("space")'


# I've limited the movent types to Forward, Left, Right.
# and based my characters on your M
# (with slight modification to assure consistency)

# if students wonder why there is length/3*2 and how it works,
# it is simply using rules of PEMDAS to get a desired amount in parts
# first you take length and divide it by 3 so 99 would now be 33
# secondly you apply the multiplication so 33 times 2 would be 66
# this way, i've got 2 thirds of the length

# if some weird errors ocurr,try renamimg line 341-function l
# i've silenced the warning
# since this project doesn't cause issues on my computer

# Adding åäö, norwegian and danish variants shoulnd't be to hard

alphabet = "abcdefghijklmnopqrstuvwxyz"

# debug_size_lines(letter_spacing)

for letter in alphabet:
    try:
        function = eval(letter)
        function_return = function(letter_spacing)
        print(f'letter "{function_return}" complete.')
    except NameError:
        print(f'Letter "{letter}" not found')


turtle.done()
