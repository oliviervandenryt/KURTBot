import tkinter as tk

libraries_files = {"Agora": "agora.csv", "CBA": "cba.csv"}

login_screen = tk.Tk()
login_screen.title("KURTBot - F*ck KURT")
login_screen.geometry("350x400")
login_screen.grid_
login_screen.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
labels = [tk.Label(text="gebruikersnaam"), tk.Label(text="wachtwoord"), tk.Label(text="tijdsloten"), tk.Label(text="zitje"),
          tk.Label(text="datum")
          ]
username_entry = tk.Entry()
password_entry = tk.Entry()
time_entries = [tk.Entry(width=10) for i in range(6)]
seat_entry = tk.Entry()
date_entry = tk.Entry()
values = [tk.StringVar() for k in range(10)]
labels[0].grid(row=0, columnspan=3, column=0)
username_entry.grid(row=1, column=1)
labels[1].grid(row=2, columnspan=3, column=0)
password_entry.grid(row=3, column=1)
labels[2].grid(row=4, columnspan=3, column=0)
for i in range(6):
    row = i//2
    column = i % 2
    if column == 1:
        column = 2
    time_entries[i].grid(row=5+row, column=column, )

confirm_button = tk.Button(
    text="Login",
    width=10,
    height=2,
    bg="white",
    fg="black",
)

login_screen.mainloop()