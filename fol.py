import tkinter as tk

from tkinter import StringVar

from functools import partial

top = tk.Tk()
top.geometry('600x500')
top.title("       <3 <3 <3 <3 <3 <3      CALCULATOR   <3 <3 <3 <3 <3 <3")

img = tk.PhotoImage(file="YAKl2RO.png")
img = img.subsample(1, 1)

background = tk.Label(top, image=img, bd=0)
background.pack(fill='both', expand=True)
background.image = img

background.rowconfigure(3, weight=500)
background.rowconfigure(4, weight=500)
background.columnconfigure(3, weight=500)
background.columnconfigure(4, weight=500)

number1 =StringVar()
number2 = StringVar()


LabelTitle = tk.Label(background, text=" CALCULATOR", font=("Arial",12,'bold'))
LabelTitle.grid(row=0,column=0,  sticky='news')
LabelNum1 = tk.Label(background, text="Please enter the first argument?",font=("Arial",12,))
LabelNum1.grid(row=1, column=0, sticky='news')
LabelNum2 = tk.Label(background, text="     Please enter the second argument?",font=("Arial",12,))
LabelNum2.grid(row=2, column=0)
LabelNum3 = tk.Label(background, text="     Please select an operation",font=("Arial",12,))
LabelNum3.grid(row=3, column=0)

label_result = tk.Label(background)
label_result.grid(row=7, column=0)


# "Entry buttons"
EntryNum1 = tk.Entry(background, textvariable = number1).grid(row=1, column=2)
EntryNum2 = tk.Entry(background, textvariable = number2).grid(row=2, column=2)
#number1.set()
#number2.set("HI")


def add(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

add = partial(add, label_result, number1, number2,)
buttonCal = tk.Button(background, text = "Add",font=("Arial", 16),
                      command=add).grid(row=4, column=0)


def sub(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) - int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

sub = partial(sub, label_result, number1, number2,)
buttonCa2 = tk.Button(background, text = "Subtract",font=("Arial", 16),
                      command=sub).grid(row=4, column=1)

def mul(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) * int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

mul = partial(mul, label_result, number1, number2,)
buttonCa3 = tk.Button(background, text = "Multiply",font=("Arial", 16),
                      command=mul).grid(row=4, column=2)

def div(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) / int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

div = partial(div, label_result, number1, number2,)
buttonCa4 = tk.Button(background, text = "Divide",font=("Arial", 16),
                      command=div).grid(row=4, column=3)



top.mainloop()