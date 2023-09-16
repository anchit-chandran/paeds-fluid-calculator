from tkinter import *

root = Tk()

button_size = 30

entry = Entry(
    root,
    width=55,
    bg="darkgreen",
    fg="white",
    borderwidth=5,
)
entry.grid(
    row=0,
    column=0,
    columnspan=4,
)


def insert_char(text):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + text)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: insert_char("1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: insert_char("2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: insert_char("3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: insert_char("4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: insert_char("5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: insert_char("6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: insert_char("7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: insert_char("8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: insert_char("9"))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: insert_char("0"))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)

def clear_entry():
    entry.delete(0, END)

button_clear = Button(root, text="C", padx=40, pady=20, command=clear_entry)
button_equals = Button(root, text="=", padx=40, pady=20,)

button_clear.grid(row=4, column=0)
button_equals.grid(row=4, column=2)

button_plus = Button(root, text="+", padx=40, pady=20,)
button_minus = Button(root, text="-", padx=40, pady=20,)
button_multiply = Button(root, text="*", padx=40, pady=20,)
button_divide = Button(root, text="/", padx=40, pady=20,)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
