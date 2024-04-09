## 3번
from tkinter import *
window = Tk()

def rdo_change():
    if var.get() ==1:
        label1.configure(text="벤츠")
    else :
        label1.configure(text="포르쉐")

var = IntVar()
rdo1 = Radiobutton(window, text="벤츠", variable=var, value=1)
rdo2 = Radiobutton(window, text="포르쉐", variable=var, value=2)
label1 = Label(window, text="선택한 차량", fg="red")

rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()

## 4번
from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

# (1)
button1.pack(side = LEFT)
button1.pack(side = LEFT)
button1.pack(side = LEFT)

# (2)
button1.pack(side = RIGHT)
button1.pack(side = RIGHT)
button1.pack(side = RIGHT)

# (3)
button1.pack(side = TOP)
button1.pack(side = TOP)
button1.pack(side = TOP)

# (4)
button1.pack(side = BOTTOM)
button1.pack(side = BOTTOM)
button1.pack(side = BOTTOM)

window.mainloop()

## 5번
from tkinter import *
from time import *

fnameList = ["jeju1.gif""jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif",
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
num = 0

def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    pLabel.configure(text = fnameList[num])

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    pLabel.configure(text = fnameList[num])

window = Tk()
window.geometry("500x200")

btnPrev = Button(window, text = "<<이전", command=clickPrev)
btnNext = Button(window, text = "다음>>", command=clickNext)
pLabel = Label(window)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
