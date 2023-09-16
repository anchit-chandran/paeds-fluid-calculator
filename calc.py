from tkinter import *


class CalculatorGUI:
    def __init__(self):
        self.root = Tk()
        self.memory = []

        self.BUTTON_SIZE = 30

        self.entry = Entry(
            self.root, width=55, bg="darkgreen", fg="white", borderwidth=5
        )

    def insert_char(self, text):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, current + text)

    def _reset_memory(self) -> None:
        self.memory = []

    def clear_entry(self) -> None:
        self.entry.delete(0, END)
        self._reset_memory()

    def append_operation(self, operand: str) -> None:
        self.memory.append(self.entry.get())
        self.memory.append(operand)
        self.entry.delete(0, END)

    def evaluate_from_memory(self) -> None:
        self.memory.append(self.entry.get())
        self.entry.delete(0, END)

        answer = eval("".join(self.memory))
        
        self.entry.insert(0, answer)
        
        self._reset_memory()

    def main(self) -> None:
        self.entry.grid(row=0, column=0, columnspan=4)

        button_1 = Button(
            self.root, text="1", padx=40, pady=20, command=lambda: self.insert_char("1")
        )
        button_2 = Button(
            self.root, text="2", padx=40, pady=20, command=lambda: self.insert_char("2")
        )
        button_3 = Button(
            self.root, text="3", padx=40, pady=20, command=lambda: self.insert_char("3")
        )
        button_4 = Button(
            self.root, text="4", padx=40, pady=20, command=lambda: self.insert_char("4")
        )
        button_5 = Button(
            self.root, text="5", padx=40, pady=20, command=lambda: self.insert_char("5")
        )
        button_6 = Button(
            self.root, text="6", padx=40, pady=20, command=lambda: self.insert_char("6")
        )
        button_7 = Button(
            self.root, text="7", padx=40, pady=20, command=lambda: self.insert_char("7")
        )
        button_8 = Button(
            self.root, text="8", padx=40, pady=20, command=lambda: self.insert_char("8")
        )
        button_9 = Button(
            self.root, text="9", padx=40, pady=20, command=lambda: self.insert_char("9")
        )
        button_0 = Button(
            self.root, text="0", padx=40, pady=20, command=lambda: self.insert_char("0")
        )

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

        button_clear = Button(
            self.root, text="C", padx=40, pady=20, command=self.clear_entry
        )
        button_clear.grid(row=4, column=0)

        button_plus = Button(
            self.root,
            text="+",
            padx=40,
            pady=20,
            command=lambda: self.append_operation("+"),
        )
        button_minus = Button(
            self.root,
            text="-",
            padx=40,
            pady=20,
            command=lambda: self.append_operation("-"),
        )
        button_multiply = Button(
            self.root,
            text="*",
            padx=40,
            pady=20,
            command=lambda: self.append_operation("*"),
        )
        button_divide = Button(
            self.root,
            text="/",
            padx=40,
            pady=20,
            command=lambda: self.append_operation("/"),
        )

        button_plus.grid(row=1, column=3)
        button_minus.grid(row=2, column=3)
        button_multiply.grid(row=3, column=3)
        button_divide.grid(row=4, column=3)

        button_equals = Button(
            self.root,
            text="=",
            padx=40,
            pady=20,
            command=lambda: self.evaluate_from_memory(),
        )
        button_equals.grid(row=4, column=2)

        debugger = Button(self.root, text="debug", command=lambda: print(self.memory))
        debugger.grid(row=5, column=1)
        
        

        self.root.mainloop()


if __name__ == "__main__":
    CalculatorGUI().main()
