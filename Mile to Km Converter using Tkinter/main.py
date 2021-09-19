from tkinter import *


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)
miles_input.insert(END, string="0")

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

km_output = Label(text="0")
km_output.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)


window.mainloop()
