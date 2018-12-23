
# 'Calculator;'

from tkinter import *
from functools import partial



root = Tk()
root.geometry("600x500")
root.title("       <3 <3 <3 <3 <3 <3      CALCULATOR   <3 <3 <3 <3 <3 <3")

number1 = StringVar()
number2 = StringVar()

# "Labels"

LabelTitle = Label(root, text=" CALCULATOR", font=("Arial",12,'bold'))
LabelTitle.grid(row=0,column=0)
LabelNum1 = Label(root, text="Please enter the first argument?",font=("Arial",12,))
LabelNum1.grid(row=1, column=0)
LabelNum2 = Label(root, text="     Please enter the second argument?",font=("Arial",12,))
LabelNum2.grid(row=2, column=0)
LabelNum3 = Label(root, text="     Please select an operation",font=("Arial",12,))
LabelNum3.grid(row=3, column=0)
label_result = Label(root)
label_result.grid(row=18, column=0)

# "Entry buttons"
EntryNum1 = Entry(root, textvariable = number1).grid(row=1, column=2)
EntryNum2 = Entry(root, textvariable = number2).grid(row=2, column=2)

#

def add(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

add = partial(add, label_result, number1, number2,)
buttonCal = Button(root, text = "Add",font=("Arial", 16),
                      command=add).grid(row=4, column=0)

def sub(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) - int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

sub = partial(sub, label_result, number1, number2,)
buttonCa2 = Button(root, text = "Subtract",font=("Arial", 16),
                      command=sub).grid(row=4, column=1)

def mul(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) * int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

mul = partial(mul, label_result, number1, number2,)
buttonCa3 = Button(root, text = "Multiply",font=("Arial", 16),
                      command=mul).grid(row=4, column=2)

def div(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) / int(num2)
    label_result.config(text="Result is %d" % result, font=("Arial",16,))
    return

div = partial(div, label_result, number1, number2,)
buttonCa4 = Button(root, text = "Divide",font=("Arial", 16),
                      command=div).grid(row=4, column=3)




root.mainloop()