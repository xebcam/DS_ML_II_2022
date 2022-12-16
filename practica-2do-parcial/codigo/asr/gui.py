#!/bin/python

import tkinter as tk

win = tk.Tk()
# Define a function to print something inside infinite loop
condition = True


def infinite_loop():
    if condition:
        tk.Label(win, text="Infinite Loop!", font="Arial, 25").pack()

    # Call the infinite_loop() again after 1 sec win.after(1000, infinite_loop)
    win.after(1000, infinite_loop)


def start():
    global condition
    condition = True


def stop():
    global condition
    condition = False


# Create a button to start the infinite loop
start = tk.Button(win, text="Start the Loop",
                  font="Arial, 12", command=start).pack()
stop = tk.Button(win, text="Stop the Loop",
                 font="Arial, 12", command=stop).pack()

# Call the infinite_loop function after 1 sec.
win.after(1000, infinite_loop)

win.mainloop()
