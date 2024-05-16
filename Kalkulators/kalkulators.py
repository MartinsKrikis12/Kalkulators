from tkinter import *

mansLogs = Tk()
mansLogs.title("Kalkulators")
mansLogs.configure(bg='#333333')


def btnClick(number):
    current = e.get()
    e.delete(0, END)
    newNumber = str(current) + str(number)
    e.insert(0, newNumber)


def btnCommand(command):
    global num1
    global mathOp
    mathOp = command
    num1 = int(e.get())
    e.delete(0, END)

def Vienads():
    num2 = int(e.get())
    result = 0
    if mathOp == "+":
        result = num1 + num2
    elif mathOp == "-":
        result = num1 - num2
    elif mathOp == "*":
        result = num1 * num2
    elif mathOp == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "AR NULLI DALĪT NEDRĪKST"
    else:
        result = 0
    e.delete(0, END)
    e.insert(0, str(result))


def notirit():
    e.delete(0, END)
    num1 = 0
    mathOp = "C"


e = Entry(mansLogs, width=15, bd=10, font=("Arial black", 20), justify="right")
e.grid(row=0, column=0, columnspan=4, pady=10)


button_style = {'padx': 30, 'pady': 20, 'bg': '#666666', 'fg': 'white', 'font': ('Arial', 14)}


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
]


for (text, row, col) in buttons:
    button = Button(mansLogs, text=text, **button_style, command=lambda t=text: btnClick(t) if t.isdigit() else (btnCommand(t) if t in "+-*/" else (notirit() if t == 'C' else Vienads())))
    button.grid(row=row, column=col, padx=5, pady=5)

mansLogs.mainloop()
