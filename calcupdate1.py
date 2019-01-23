from tkinter import *

from  math import *

from decimal import *

from PIL import *

import math

class Calc:
    tk = None
    firstNumber = None
    secondNumber = None
    Result = None
    bg = None
    #TWOPlACES = D(10) ** -2
    #resizable = None


    def __init__(self):
        self.tk = Tk()
        self.firstNumber = StringVar()
        self.secondNumber = StringVar()
        self.bg = PhotoImage(file ="Butterflies.png")
        self.tk.resizable(False, False)
        self.TWOPlACES = Decimal(10) ** -2
        #self.canv = Canvas()
        #self.canv.pack
        #self.create_image(image=bg)
        #self.create_image.pack
        self.setupUi()


    def setupUi(self):

        #bg = PhotoImage("YAKl2RO.png")
        #bg = Image.PhotoImage(img)



        background = Canvas(self.tk)
        background.pack(fill=BOTH, expand=YES)
        #background.geometry(height= 500, width=600)
        background.create_image(125,125, image=self.bg)


        #self.img_copy = self.image.copy()

        #background = PhotoImage(file= "YAKl2RO.png")
        #background.bind('<Configure>', self._resize_image)

    #def _resize_image(self, event):

    #   new_width = event.width
    #  new_height = event.height
    # self.img_copy = self.bg.copy()
    #self.bg = self.bg.resize((new_width, new_height))


        #label.image =background
        #label.pack()

        titleArea = Frame(background)
        titleArea.pack( pady=5, padx=5, )

        titleText = Label(titleArea, text="** Calculator **", border=1, width=15, anchor="w")
        titleText.pack(side=LEFT)

        firstInputArea = Frame(background)
        firstInputArea.pack( pady=5, padx=15)

        firstNumberLabel = Label(firstInputArea, text="First number:", width=15, anchor="w")
        firstNumberLabel.pack(side=LEFT)
        firstNumberEntry = Entry(firstInputArea, textvariable=self.firstNumber, width=10)
        firstNumberEntry.pack(side=LEFT)

        secondInputArea = Frame(background)
        secondInputArea.pack( pady=5, padx=5)

        secondNumberLabel = Label(secondInputArea, text="Second number:", width=15, anchor="w")
        secondNumberLabel.pack(side=LEFT)
        secondNumberEntry = Entry(secondInputArea, textvariable=self.secondNumber, width=10)
        secondNumberEntry.pack(side=LEFT)

        thirdInputArea = Frame(background)
        thirdInputArea.pack( pady=5, padx=5)
        firstButton = Button(thirdInputArea, text="Add", width=10, anchor="w", command=self.add)
        firstButton.pack(side=LEFT)

        secondButton = Button(thirdInputArea, text="Subtract", width=10, anchor="w", command=self.sub)
        secondButton.pack(side=LEFT)

        thirdButton = Button(thirdInputArea, text="Multiply", width=10, anchor="w", command=self.mul)
        thirdButton.pack(side=LEFT)

        fourthButton = Button(thirdInputArea, text="Divide", width=10, anchor="w", command=self.div)
        fourthButton.pack(side=LEFT)

        fourthInputArea = Frame(background)
        fourthInputArea.pack(pady=5, padx=5)

        fifthButton = Button(fourthInputArea, text="√", width=10, anchor="w", command=self.sqrt)
        fifthButton.pack(side=LEFT)

        fifthInputArea = Frame(background)
        fifthInputArea.pack( pady=5, padx=5)

        self.Result = Label(fifthInputArea, text="Result", width=20)
        self.Result.pack()

    #def float_round (self, places = 0, direction = floor):
     #   return direction(firstNumber *(10**places))/float (10**places)

    def add(self):
        firstNumber = (self.firstNumber.get())
        secondNumber = (self.secondNumber.get())
        fp= (self, float, "3f")
        if "." in firstNumber:
            firstNumber = float(firstNumber)
        else:
            firstNumber = int(firstNumber)
        if "." in secondNumber:
            secondNumber = float(secondNumber)
        else:
            secondNumber = int(secondNumber)


        #Result=firstNumber+secondNumber
        #getcontext().prec = 3
        Result= "{0:.5f}".format(firstNumber+secondNumber)
        #self.Result.config(text="Result is " "{0:3f}".format(Result), font=("Arial, 16"))
        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
        #getcontext().prec = 3
        #round(float(Result [2]))
        #float(quantize(Result("0.00")))
        #float(Result.quantize('{0:3f}'.format(Result)))
        #float_round(Result, 3, round)

        #float(Result.quantize, rounding=ROUND_UP))
        return
        #(firstNumber+secondNumber).quantize(fp)

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

        #Result = firstNumber-secondNumber
        Result = "{0:.5f}".format(firstNumber-secondNumber)
        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
        #"{0:2f}".format(Result)
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

        #Result = firstNumber*secondNumber
        Result = "{0:.5f}".format(firstNumber*secondNumber)
        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
        "{0:2f}".format(Result)
        #float(Result.quantize(D("0.00"), rounding=ROUND_UP))
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
            #Result = firstNumber/secondNumber
            Result = "{0:.5f}".format(firstNumber/secondNumber)
            self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))
            #"{0:2f}".format(Result)
            #float(Result.quantize(D("0.00"), rounding=ROUND_UP))
            return
        except ZeroDivisionError:
            self.Result.config(text= "Invalid input. Please try again", font=("Arial, 16"))
            return 0


    def sqrt (self):

        firstNumber = (self.firstNumber.get())

        if "." in firstNumber:
            firstNumber = float(firstNumber)
            Result = "{0:.5f}".format(math.sqrt(firstNumber))
        else:
            firstNumber = int(firstNumber)
            Result = "{0:.0f}".format(math.sqrt(firstNumber))


        self.Result.config(text="Result is {}".format(Result), font=("Arial, 16"))


       # if "." in secondNumber:
         #   secondNumber = float(secondNumber)
        #else:
          #  secondNumber = int(secondNumber)
        return


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
