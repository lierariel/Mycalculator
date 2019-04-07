# coding: utf-8



from tkinter import *

from  math import *

from decimal import *

#from PIL import *

import math

from setuptools import setup


class Calc:

    tk = None
    firstNumber = None
    # secondNumber = None
    #calc_value = None

    number_entry = None
    Result = None
    bg = None
    operation = None




    def __init__(self):

        self.tk = Tk()
        # self.calc_value = StringVar()
        self.firstNumber = float
        #self.Result = 0
        self.bg = PhotoImage(file="/Users/victoriarouch/Documents/tory1/tory1proje/Butterflies.png")
        self.tk.resizable(False, False)

        self.setupUi()


    def setupUi(self):
        background = Canvas(self.tk)
        background.pack(fill=BOTH, expand=YES)
        # background.geometry(height= 500, width=600)
        background.create_image(125, 125, image=self.bg)

        titleArea = Frame(background)
        titleArea.pack(pady=5, padx=5, )

        titleText = Label(titleArea, text="** Calculator **", border=1, width=15, anchor="w")
        titleText.pack(side=LEFT)

        firstInputArea = Frame(background)
        firstInputArea.pack(pady=5, padx=15)


        self.firstNumberEntry = Entry(firstInputArea, textvariable=self.firstNumber, width=20)
        self.firstNumberEntry.pack(side=LEFT)

        thirdInputArea = Frame(background)
        thirdInputArea.pack(pady=5, padx=5)
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

        # fifthInputArea = Frame(background)
        # fifthInputArea.pack(pady=5, padx=5)

        sixthButton = Button(fourthInputArea, text="=", width=10, anchor="w", command=self.Equals)
        sixthButton.pack(side=LEFT)

        fifthInputArea = Frame(background)
        fifthInputArea.pack(pady=5, padx=5)

        seventhButton = Button(fourthInputArea, text="CLEAR", width =10, anchor="w", command=self.delete)
        seventhButton.pack(side=LEFT)

        eighthButton = Button(fourthInputArea, text="Backspace", width=10, anchor="w", command=self.backspace)
        eighthButton.pack(side=LEFT)

        self.Result = Label(fifthInputArea, text="Result", width=20)
        self.Result.pack()

        sixthInputArea = Frame(background)
        sixthInputArea.pack(pady=5, padx=5)

        b1 = Button(sixthInputArea, text="1", width=5, anchor="w", command=self.press)
        b1.pack(side=LEFT)
        b2 = Button(sixthInputArea, text="2", width=5, anchor="w", command=self.press2)
        b2.pack(side=LEFT)
        b3 = Button(sixthInputArea, text="3", width=5, anchor="w", command=self.press3)
        b3.pack(side=LEFT)
        b4 = Button(sixthInputArea, text="4", width=5, anchor="w", command=self.press4)
        b4.pack(side=LEFT)
        b5 = Button(sixthInputArea, text="5", width=5, anchor="w", command=self.press5)
        b5.pack(side=LEFT)

        seventhInputArea = Frame(background)
        seventhInputArea.pack(pady=5, padx=5)

        b6 = Button(seventhInputArea, text="6", width=5, anchor="w", command=self.press6)
        b6.pack(side=LEFT)
        b7 = Button(seventhInputArea, text="7", width=5, anchor="w", command=self.press7)
        b7.pack(side=LEFT)
        b8 = Button(seventhInputArea, text="8", width=5, anchor="w", command=self.press8)
        b8.pack(side=LEFT)
        b9 = Button(seventhInputArea, text="9", width=5, anchor="w", command=self.press9)
        b9.pack(side=LEFT)
        b0 = Button(seventhInputArea, text="0", width=5, anchor="w", command=self.press0)
        b0.pack(side=LEFT)


        # def float_round (self, places = 0, direction = floor):
        #   return direction(firstNumber *(10**places))/float (10**places)







    def Equals(self):

        self.firstNumber = self.firstNumberEntry.get()
        
        #eliminating all acceptable characters from the input string.
        #If any characters remain in "numbers", the input string is invalid.
        numbers = self.firstNumber
        acceptable = '+-/*.√1234567890'
        
        #Deleting all acceptable characters in numbers:
        for x in acceptable:
            numbers = numbers.replace(x,'')
        
        #Verifying validity of input string
        if numbers == '': #If the variable numbers is an empty string, the input was valid:
            
            #resetting the numbers variable
            numbers = self.firstNumber
            
            # Calculating square root first.
            # First, split all terms of the equation by adding a "_" around all other operators except '√'
            acceptable = '+-/*'
            for x in acceptable:
                numbers = numbers.replace(x, ('_' + x + '_') )
                
            # Then split the new string where there is a "_" to form a list
            numbers=numbers.split('_')
            
            # Now go through all items on the split list
            for x in range(len(numbers)):
                # If the current item ends in '√', the square root should be calculated.
                if numbers[x][0] == '√':
                    numbers[x]=str(float(numbers[x][1:])**0.5)
            # now that all square roots have been calculated, the list can be rejoined
            numbers=''.join(numbers)
            
            Resultfit = eval(numbers)
        else: # If the variable numbers is NOT an empty string, the input was invalid:
            Resultfit = 'Invalid input.Please try again.\nOnly these characters are acceptable: +-/*.√1234567890'
        #input=  '+-/*1234567890'

        self.Result.config(text="Result is {}".format(Resultfit), width=200, font=("Arial, 16"))
        return

    def press(self):
        self.operation = "press"
        self.firstNumberEntry.insert(END, string="1")

    def press2(self):
        self.operation = "press2"
        self.firstNumberEntry.insert(END, string="2")

    def press3(self):
        self.operation = "press3"
        self.firstNumberEntry.insert(END, string="3")

    def press4(self):
        self.operation = "press4"
        self.firstNumberEntry.insert(END, string="4")

    def press5(self):
        self.operation = "press5"
        self.firstNumberEntry.insert(END, string="5")

    def press6(self):
        self.operation = "press6"
        self.firstNumberEntry.insert(END, string="6")

    def press7(self):
        self.operation = "press7"
        self.firstNumberEntry.insert(END, string="7")

    def press8(self):
        self.operation = "press8"
        self.firstNumberEntry.insert(END, string="8")

    def press9(self):
        self.operation = "press9"
        self.firstNumberEntry.insert(END, string="9")

    def press0(self):
        self.operation = "press0"
        self.firstNumberEntry.insert(END, string="0")



    def add(self):
        self.operation = 'add'
        self.firstNumberEntry.insert(END, string='+')


    def sub(self):
        self.operation = 'sub'
        self.firstNumberEntry.insert(END, string='-')


    def mul(self):
        self.operation = 'sub'
        self.firstNumberEntry.insert(END, string='*')


    def div(self):
        try:
            self.operation = 'sub'
            self.firstNumberEntry.insert(END, string='/')

        except ZeroDivisionError:
            self.Result.config(text= "Invalid input. Please try again", font=("Arial, 16"))
            return 0


    def sqrt (self):
        self.operation = 'sqrt'
        self.firstNumberEntry.insert(END, string='√')

    def delete (self):
        # self.operation = "delete"
        self.firstNumberEntry.delete(0, END)
        # self.firstNumberEntry.insert(0, new)

    def backspace(self):

        n = self.firstNumberEntry.get()
        self.firstNumberEntry.delete(0, END)
        self.firstNumberEntry.insert(END, string=n[:-1])

        # if self.current_line == "":
        #     self.current_line = len(self.current_line[0:-1])


     #   cancel[0:len(self.current_line) -1]
       # self.firstNumberEntry = self.firstNumberEntry.cancel

        #self.firstNumberEntry = (len(self.firstNumberEntry.get()) - 1)




app = Calc()
app.tk.geometry('600x500')


app.tk.mainloop()

if __name__ == '__main__':
    app = Calc()
