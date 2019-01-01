from tkinter import *
from PIL import *
import subprocess

class App(Frame):

    def __init__(self, master):

        self.master = master
        Frame.__init__(self, master)
        dialog_frame = Frame(self)
        dialog_frame.pack(padx=0, pady=0)
        self.pack()
        self.master.title("Calculator")


        self.master.resizable(False, False)
        self.master.tk_setPalette(background= "pink")

        self.label1 = Label(dialog_frame, text=" CALCULATOR", font=("Arial", 12, 'bold'), anchor="w").pack(fill="both")
        self.label2 = Label(dialog_frame, text=" \n\n Please enter you first argument", font=("Arial", 12, 'bold')).pack(fill=X,)
        self.label3 = Label(dialog_frame, text=" \n\n\n\n Please enter you second argument",
                            font=("Arial", 12, 'bold')).pack(fill=X, )

        self.label_result = Label(dialog_frame, text="Result", font=("Arial", 12, 'bold'), anchor="w").pack(fill="both")

        self.buttonCal1 = Button(dialog_frame, text="Add", font=("Arial, 16"), command=self.add).pack()

        self.number1 = StringVar()
        self.number2 = StringVar()

        self.entrynum1 = Entry(dialog_frame, textvariable=self.number1).pack()
        self.entrynum2 = Entry(dialog_frame, textvariable=self.number2).pack()

    def add(self):
        num1= (self.number1.get())
        num2 = (self.number2.get())
        result=int(num1)+int(num2)
        self.label_result.config(text="Result is %d" % result, font=("Arial, 16"))
        return



root = Tk()
root.geometry("500x500")
app = App(root)
app.mainloop()


