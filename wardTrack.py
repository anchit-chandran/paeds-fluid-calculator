import tkinter as tk
import sqlite3

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

        if not self.db_exists():
            self._create_db()
            self._seed_pts()

        self.draw_pts()
        
        debug_button = tk.Button(self.root, text='DEBUG', command=lambda: self.debug())
        debug_button.grid(row=1, column=0)
        
        self.root.mainloop()
    
    def debug(self)->None:
        conn = self.connect_to_db()
        conn.row_factory = sqlite3.Row
        
        c = conn.cursor()
        
        c.execute("""SELECT * FROM ward_pts""")
        records = [dict(item) for item in c.fetchall()]
        print(records)
        
        conn.commit()
        conn.close()
    
    def get_all_records(self)->list[tuple]:
        conn = self.connect_to_db()
        conn.row_factory = sqlite3.Row
        
        c = conn.cursor()
        
        c.execute("""SELECT * FROM ward_pts""")
        records = [dict(item) for item in c.fetchall()]     
        conn.commit()
        conn.close()
        
        return records
    
    def db_exists(self):
        import os
        
        cwd = os.getcwd()
        
        db_name = 'ward.db'
        
        return os.path.isfile(os.path.join(cwd, db_name))
        
    
    def connect_to_db(self):
        return sqlite3.connect('ward.db')

    def _create_db(self):
        conn = sqlite3.connect("ward.db")

        c = conn.cursor()

        c.execute(
            """CREATE TABLE ward_pts (
                first_name text,
                last_name text,
                age int,
                sex text,
                bed int,
                diagnosis text
            )"""
        )

        conn.commit()

        conn.close()

    def _seed_pts(self) -> None:
        conn = sqlite3.connect("ward.db")

        c = conn.cursor()

        for pt in self.get_all_records():
            c.execute(
                """INSERT INTO ward_pts VALUES (:first_name, :last_name, :age, :sex, :bed, :diagnosis )""",
                {
                    "first_name": pt["first_name"],
                    "last_name": pt["last_name"],
                    "age": pt["age"],
                    "sex": pt["sex"],
                    "bed": pt["bed"],
                    "diagnosis": pt["diagnosis"],
                },
            )

        conn.commit()
        conn.close()

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
