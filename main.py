from tkinter import *

root = Tk()

input_box = Entry(root, width=50, bg="red")
input_box.pack()
input_box.insert(0, 'Enter your name: ')


def buttonCallback():
    name = input_box.get()
    buttonLabel = Label(root, text=f"Patient's name: {name}").pack()


myButton = Button(
    root, text="Please enter patient's name", padx=50, pady=50, command=buttonCallback
)
myButton.pack()

root.mainloop()
