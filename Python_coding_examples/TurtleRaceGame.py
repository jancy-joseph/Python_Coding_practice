#!/bin/python3

from turtle import *
from random import randint
penup()
speed(10)
goto(-140,140)

for step in range(15):
  write(step,align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada=Turtle()
ada.color('Red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
for turn in range(10):
  ada.right(36)
ada.pendown()

bob=Turtle()
bob.color('Blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
for turn in range(10):
  bob.right(36)
bob.pendown()

cat=Turtle()
cat.color('Green')
cat.shape('turtle')

cat.penup()
cat.goto(-160,40)
for turn in range(10):
  cat.right(36)
cat.pendown()

dog=Turtle()
dog.color('Yellow')
dog.shape('turtle')

dog.penup()
dog.goto(-160,10)
for turn in range(10):
  dog.right(36)
dog.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  cat.forward(randint(1,5))
  dog.forward(randint(1,5))
