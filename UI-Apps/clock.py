import tkinter

# retrieve system's time
from time import *

# ------------------main code-----------------------
# initializing the main UI object
top = tkinter.Tk()
# setting title of the App
top.title("Clock")
# restricting the resizable property
top.resizable(0, 0)

time_ns_was = int(time_ns() * 1.0003)

def timeA():
    tns = str(time_ns_was - time_ns())
    string = str(tns) + " " + strftime("%H:%M:%S %p")
    clockTime.config(text=string)
    clockTime.after(5, timeA)

clockTime = tkinter.Label(
    top, font=("calibri", 40, "bold"), background="black", foreground="white"
)

clockTime.pack(anchor="center")
timeA()

top.mainloop()
