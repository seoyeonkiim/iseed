from tkinter import *
import random

btnList = [None] * 9
fnameList = ['honeycomb.png', 'donut.png', 'jellybean.png', 'cupcake.png',
             'tiramisu.png', 'marshmallow.png', 'nougat.png', 'oreo.png', 'gingerbread.png']
random.shuffle(fnameList)
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("528x528")

for i in range(0, 9):
    photoList[i] = PhotoImage(file = 'D:/Document/공부/수업/i-SEEDprogramming/img/' + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 176
    xPos = 0
    yPos += 176

window.mainloop()