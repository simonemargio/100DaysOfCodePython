from tkinter import *


def label_create(string):
    new_label = Label(text=string)
    return new_label

def convert():
    miles = float(input.get())
    km = miles * 1.609
    label_km.config(text=km)

w = Tk()
w.title("Mile to KM Converter")
w.minsize(400,100)
w.config(padx=20, pady=30)

label_miles = label_create("Miles")
label_miles.grid(column=0, row=0)

input = Entry(width=5)
input.insert(END, string="0")
input.grid(column=2,row=0)

label_covert = label_create("is euqal to")
label_covert.grid(column=3, row=0)

label_km = label_create("0.0")
label_km.grid(column=4, row=0)

label_km_convert = label_create("Km")
label_km_convert.grid(column=5, row=0)

button = Button(text="Convert", command=convert)
button.grid(column=6, row=0, padx=30)


w.mainloop()