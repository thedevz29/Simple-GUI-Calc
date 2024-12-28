from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Simple Calculator in Tkinter")

l1 = Label(text="This is a very simple calculator made by Atharv Sharma", bg="#00FF00", fg="#000000")
l2 = Label(text="Enter the two numbers in the input boxes below: ")

e1 = Entry()
e2 = Entry()

t1 = Text(width=30, height=5)

def add():
    try:
        t1.insert(END, str(float(e1.get()) + float(e2.get())) + "\n")
    except ValueError:
        t1.insert(END, "Invalid input! Enter numbers only.\n")

def subtract():
    try:
        t1.insert(END, str(float(e1.get()) - float(e2.get())) + "\n")
    except ValueError:
        t1.insert(END, "Invalid input! Enter numbers only.\n")

def multiply():
    try:
        t1.insert(END, str(float(e1.get()) * float(e2.get())) + "\n")
    except ValueError:
        t1.insert(END, "Invalid input! Enter numbers only.\n")

def divide():
    try:
        t1.insert(END, str(float(e1.get()) / float(e2.get())) + "\n")
    except ZeroDivisionError:
        t1.insert(END, "Cannot divide by zero\n")
    except ValueError:
        t1.insert(END, "Invalid input! Enter numbers only.\n")

b1 = Button(text="+", bg="white", fg="green", command=add)
b2 = Button(text="-", bg="white", fg="green", command=subtract)
b3 = Button(text="*", bg="white", fg="green", command=multiply)
b4 = Button(text="/", bg="white", fg="green", command=divide)

l1.grid(row=0, column=0, columnspan=2, pady=10)
l2.grid(row=1, column=0, columnspan=2, pady=10)

e1.grid(row=2, column=0, padx=5, pady=5)
e2.grid(row=2, column=1, padx=5, pady=5)

b1.grid(row=3, column=0, pady=5)
b2.grid(row=3, column=1, pady=5)
b3.grid(row=4, column=0, pady=5)
b4.grid(row=4, column=1, pady=5)


t1.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
