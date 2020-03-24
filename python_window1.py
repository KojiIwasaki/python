import tkinter

window1 = tkinter.Tk()

def close():
    window1.quit()

def resize():
    window1.geometry("400x100")
    
button1 = tkinter.Button(master=window1, text="Close", command=close)
button2 = tkinter.Button(master=window1, text="Resize", command=resize)
button1.pack()
button2.pack()

window1.mainloop()