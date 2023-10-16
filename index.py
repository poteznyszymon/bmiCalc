import tkinter as tk
import ttkbootstrap as ttk
#from tkinter import ttk
from math import pow

def calculate():
    heightIn = inputHeight.get()
    weightIn = inputWeight.get()
    bmiOut = (int(weightIn)/pow(int(heightIn),2)*10000)
    window.geometry('500x200')
    outString.set(round(bmiOut, 1))
    captionWeight.destroy()
    captionHeight.destroy()
        
#window
window = ttk.Window(themename='sandstone')
window.title('Bmi calculator')
window.geometry('500x170')
window.resizable(0,0)

#title
titleFrame = ttk.Label(master=window, text='Calcualte your BMI', font='Calibri 24 bold')
titleFrame.pack(pady=20)

#inputFrame 
inputFrame = ttk.Frame(master=window)

#inputHeight
heightInt = tk.IntVar()
inputHeight = ttk.Entry(master=inputFrame, textvariable=heightInt)

#inputWeight
weightInt = tk.IntVar()
inputWeight = ttk.Entry(master=inputFrame, textvariable=weightInt)

#button
button = ttk.Button(master=inputFrame, text="Calculate", command=calculate)

#paccking
inputHeight.pack(side='left', padx=10)
inputWeight.pack(side='left')
button.pack(side='left',padx=10)
inputFrame.pack()

#caption
captionHeight = ttk.Label(master=window, text="Enter your height [cm]", font='Roboto 10')
captionWeight = ttk.Label(master=window, text="Enter yout weight [kg]", font='Roboto 10')
captionHeight.pack(side='left', padx=18)
captionWeight.pack(side='left', padx=10)

#output
outString = tk.StringVar()
outLabel = ttk.Label(master=window, text="Output", font='Calibri 24', textvariable=outString)
outLabel.pack(pady=10)

window.mainloop()
