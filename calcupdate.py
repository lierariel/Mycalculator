from tkinter import *

import decimal as D

from PIL import *

class Calc:
    tk = None
    firstNumber = None
    secondNumber = None
    Result = None
    bg = None


    def __init__(self):
        self.tk = Tk()
        self.firstNumber = StringVar()
        self.secondNumber = StringVar()
        #self.bg =PhotoImage(file ="YAKl2RO.png")
        #self.canv = Canvas()
        #self.canv.pack
        #self.create_image(image=bg)
        #self.create_image.pack
        self.setupUi()


    def setupUi(self):

        #bg = PhotoImage("YAKl2RO.png")
        #bg = Image.PhotoImage(img)



        #background = Canvas(self,)
        #background = PhotoImage(file= "YAKl2RO.png")

        #label.image =background
        #label.pack()

        titleArea = Frame(self.tk)
        titleArea.pack(fill=X, pady=5, padx=5, )

        titleText = Label(titleArea, text="** Calculator **", border=1)
        titleText.pack(fill=X)

        firstInputArea = Frame(self.tk)
        firstInputArea.pack(fill=X, pady=5, padx=5)

        firstNumberLabel = Label(firstInputArea, text="First number:", width=15, anchor="w")
        firstNumberLabel.pack(side=LEFT)
        firstNumberEntry = Entry(firstInputArea, textvariable=self.firstNumber, width=10)
        firstNumberEntry.pack(side=LEFT)

        secondInputArea = Frame(self.tk)
        secondInputArea.pack(fill=X, pady=5, padx=5)

        secondNumberLabel = Label(secondInputArea, text="Second number:", width=15, anchor="w")
        secondNumberLabel.pack(side=LEFT)
        secondNumberEntry = Entry(secondInputArea, textvariable=self.secondNumber, width=10)
        secondNumberEntry.pack(side=LEFT)

        thirdInputArea = Frame(self.tk)
        thirdInputArea.pack(fill=X, pady=5, padx=5)
        firstButton = Button(thirdInputArea, text="Add", width=10, anchor="w", command=self.add)
        firstButton.pack(side=LEFT)

        secondButton = Button(thirdInputArea, text="Subtract", width=10, anchor="w", command=self.sub)
        secondButton.pack(side=LEFT)

        thirdButton = Button(thirdInputArea, text="Multiply", width=10, anchor="w", command=self.mul)
        thirdButton.pack(side=LEFT)

        fourthButton = Button(thirdInputArea, text="Divide", width=10, anchor="w", command=self.div)
        fourthButton.pack(side=LEFT)

        fourthInputArea = Frame(self.tk)
        fourthInputArea.pack(fill=X, pady=5, padx=5)

        self.Result = Label(fourthInputArea, text="Result", width=40)
        self.Result.pack()

    def add(self):
        firstNumber = (self.firstNumber.get())
        secondNumber = (self.secondNumber.get())
        if "." in firstNumber:
            firstNumber = float(firstNumber)
        else:
            firstNumber = int(firstNumber)
        if "." in secondNumber:
            secondNumber = float(secondNumber)
        else:
            secondNumber = int(secondNumber)


        Result= firstNumber+secondNumber
        #self.Result.config(text="Result is " "{0:3f}".format(Result), font=("Arial, 16"))
        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
        float(Result.quantize(D("0.00"), rounding=ROUND_UP))
        return

    def sub(self):
        firstNumber = (self.firstNumber.get())
        secondNumber = (self.secondNumber.get())
        if "." in firstNumber:
            firstNumber = float(firstNumber)
        else:
            firstNumber = int(firstNumber)
        if "." in secondNumber:
            secondNumber = float(secondNumber)
        else:
            secondNumber = int(secondNumber)

        Result = firstNumber-secondNumber
        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
        float(Result.quantize(D("0.00"), rounding=ROUND_UP))
        return

    def mul(self):
        firstNumber = (self.firstNumber.get())
        secondNumber = (self.secondNumber.get())
        if "." in firstNumber:
            firstNumber = float(firstNumber)
        else:
            firstNumber = int(firstNumber)
        if "." in secondNumber:
            secondNumber = float(secondNumber)
        else:
            secondNumber = int(secondNumber)

        Result = firstNumber*secondNumber
        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
        float(Result.quantize(D("0.00"), rounding=ROUND_UP))
        return

    def div(self):
        firstNumber = (self.firstNumber.get())
        secondNumber = (self.secondNumber.get())
        if "." in firstNumber:
            firstNumber = float(firstNumber)
        else:
            firstNumber = int(firstNumber)
        if "." in secondNumber:
            secondNumber = float(secondNumber)
        else:
            secondNumber = int(secondNumber)


        try:
            Result = firstNumber/secondNumber
            self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
            float(Result.quantize(D("0.00"), rounding=ROUND_UP))
            return
        except ZeroDivisionError:
            self.Result.config(text= "Invalid input. Please try again", font=("Arial, 16"))
            return 0

app = Calc()
app.tk.geometry('600x500')
#canvas = Canvas(app)
#canvas.pack(expand=YES, fill=BOTH)

#canvas.create_image(50,10, image=bg)
#canvas = Canvas(app)
#canvas.pack()
#bg = PhotoImage(file ="YAKl2RO.png")
#canvas.create_image(125, 125, image=bg)
app.tk.mainloop()
