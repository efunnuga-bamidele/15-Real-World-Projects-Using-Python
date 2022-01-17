from calendar import c
import tkinter as tk
from tkcalendar import *

root = tk.Tk()

root.title("Calendar")

root.geometry("600x400")

cal = Calendar(root, year = 2022, month = 1, day =17)
# label = tk.Label(text = "GUI Calendar")
# label = tk.Label(text="GUI Calendar", fg="white", bg="black")
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )

# label.pack(pady=20)
# button.pack()
cal.pack(pady =50)

root.mainloop()
