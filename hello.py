#!/usr/bin/env python3

# run with:./hello.py -c 4

import sys
print("Hello Python")
z = sys.argv[2]
print(z)
x = int((sys.argv[2]))
print("x is ",x)
for i in range(int(sys.argv[2])):
    print(i)

from tkinter import *
root = Tk()
root.geometry('300x300')
root.title("Tkinter Window")
text = Label(root, text=z)
text.pack()

text2 = Label(root, text='Some text')
text2.pack()


root.mainloop()
