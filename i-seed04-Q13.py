import turtle
import random
from tkinter.simpledialog import *
import math

inStr = ''
swidth, sheight = 500, 500
radius = 200
txtSize = 20

# 문자열 입력 받기
inStr = askstring('문자열 입력', '거북이가 쓸 문자열을 입력')

num_chars = len(inStr)
angle_per_char = (360 * 2) / (num_chars)

turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

for i, ch in enumerate(inStr):
    angle = i * angle_per_char
    spiral_radius = radius - (3 * i)
    x = spiral_radius * math.cos(math.radians(angle))
    y = spiral_radius * math.sin(math.radians(angle))

    turtle.goto(x, y)
    r, g, b = random.random(), random.random(), random.random()
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

turtle.done()