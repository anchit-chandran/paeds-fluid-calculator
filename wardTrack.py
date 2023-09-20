import tkinter as tk

data = [
    {
        "first_name": "Anchit",
        "last_name": "Chandran",
        "age": 20,
        "sex": "M",
        "bed": 1,
        "diagnosis": "htn",
    },
    {
        "first_name": "Billy",
        "last_name": "Joel",
        "age": 30,
        "sex": "F",
        "bed": 2,
        "diagnosis": "asthma",
    },
    {
        "first_name": "Crikey",
        "last_name": "Ditre",
        "age": 40,
        "sex": "M",
        "bed": 3,
        "diagnosis": "copd",
    },
]


class WardApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.geometry(f"{200*len(data)}x400")
        self.root.title("WardTrack 2.0")

        self.draw_pts()

        self.root.mainloop()

    def draw_pts(self) -> None:
        for ix, pt in enumerate(data):
            frame = tk.Frame(self.root)

            name = tk.Label(
                frame,
                text=f'B{pt["bed"]}: {pt["first_name"]} {pt["last_name"]} ({pt["age"]}{pt["sex"]})',
                bg="darkred",
            )
            name.grid(row=0, column=0)

            diagnosis = tk.Label(frame, text=pt["diagnosis"])
            diagnosis.grid(row=1, column=0)

            frame.grid(
                row=0,
                column=ix,
                padx=10,
                pady=15,
            )


if __name__ == "__main__":
    WardApp(tk.Tk())
