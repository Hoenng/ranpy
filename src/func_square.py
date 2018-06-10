#!/usr/local/bin/python3

"""Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the program again."""

import turtle

def square(t, x):
	for i in range(4):
		t.fd(x)
		t.lt(90)

	turtle.mainloop()

bob = turtle.Turtle()
length = 40
square(bob, length)