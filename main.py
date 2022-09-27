"""
This app allows the user to play Etch-a-Sketch using keyboard keys.
W key - forwards
S key - backwards
A key - counter-clockwise (left)
D key - clockwise (right)
C key - clear drawing

This script requires that `turtle` be imported.
"""
import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    """Moves turtle forward."""
    tim.fd(10)

def move_backward():
    """Moves turtle backward."""
    tim.bk(10)

def turn_left():
    """Turns turtle to the left."""
    tim.setheading(tim.heading() + 10)

def turn_right():
    """Turns turtle to the right."""
    tim.setheading(tim.heading() - 10)

def clear():
    """Clears drawing and returns turtle to starting position."""
    tim.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
