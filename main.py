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
    t1.insert(END, str(int(e1.get()) + int(e2.get())) + "\n")

def subtract():
    t1.insert(END, str(int(e1.get()) - int(e2.get())) + "\n")

def multiply():
    t1.insert(END, str(int(e1.get()) * int(e2.get())) + "\n")

def divide():
    try:
        t1.insert(END, str(int(e1.get()) / int(e2.get())) + "\n")
    except ZeroDivisionError:
        t1.insert(END, "Cannot divide by zero\n")

b1 = Button(text="+", bg="white", fg="green", command=add)
b2 = Button(text="-", bg="white", fg="green", command=subtract)
b3 = Button(text="*", bg="white", fg="green", command=multiply)
b4 = Button(text="/", bg="white", fg="green", command=divide)

l1.pack()
l2.pack()
e1.pack()
e2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
t1.pack()

root.mainloop()
