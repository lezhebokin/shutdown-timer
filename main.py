from tkinter import Tk, ttk, IntVar, messagebox
from datetime import timedelta
import subprocess
import re


def change(*args):
    hour_label["text"] = f"Часы: {hour.get()}"
    minute_label["text"] = f"Минуты: {minute.get()}"


def enable(preset=None):
    if preset is None:
        preset = (int(hour.get())*3600 + int(minute.get())*60)
        if not preset:
            messagebox.showerror(title="Ошибка", message="Время не настроено")
            return
        for var in [hour, minute]:
            var.set(0)
        change(None)

    command = subprocess.run(["shutdown", "/s", "/t", f"{preset}"], capture_output=True, text=True)
    if re.search("1190", command.stderr):
        messagebox.showerror(title="Ошибка", message="Таймер уже активирован")
    else:
        messagebox.showinfo(title="Успех", message=f"{'Компьютер выключится через'} {timedelta(seconds=preset)}")


def disable():
    command = subprocess.run(["shutdown", "/a"], capture_output=True, text=True)
    if re.search("1116", command.stderr):
        messagebox.showerror(title="Ошибка", message="Таймер не активирован")
    else:
        messagebox.showinfo(title="Успех", message="Таймер деактивирован")


root = Tk()
root.title("Shutdown Timer")
root.geometry("350x230")
root.resizable(width=False, height=False)

ttk.Frame(relief="solid").place(x=10, y=20, width=330, height=80)
ttk.Label(text="Быстрый старт").place(x=135, y=10)
ttk.Button(text="0:30", command=lambda: enable(1800)).place(x=20, y=30, width=70, height=25)
ttk.Button(text="1:00", command=lambda: enable(3600)).place(x=100, y=30, width=70, height=25)
ttk.Button(text="1:30", command=lambda: enable(5400)).place(x=180, y=30, width=70, height=25)
ttk.Button(text="2:00", command=lambda: enable(7200)).place(x=260, y=30, width=70, height=25)
ttk.Button(text="2:30", command=lambda: enable(9000)).place(x=20, y=65, width=70, height=25)
ttk.Button(text="3:00", command=lambda: enable(10800)).place(x=100, y=65, width=70, height=25)
ttk.Button(text="3:30", command=lambda: enable(12600)).place(x=180, y=65, width=70, height=25)
ttk.Button(text="4:00", command=lambda: enable(14400)).place(x=260, y=65, width=70, height=25)

hour = IntVar(value=0)
hour_label = ttk.Label(text=f"Часы: {hour.get()}")
hour_label.place(x=10, y=110)
ttk.Scale(from_=0, to=23, orient="horizontal", variable=hour, command=change, length=160).place(x=10, y=130)

minute = IntVar(value=0)
minute_label = ttk.Label(text=f"Минуты: {minute.get()}")
minute_label.place(x=180, y=110)
ttk.Scale(from_=0, to=59, orient="horizontal", variable=minute, command=change, length=160).place(x=180, y=130)

ttk.Button(text="АКТИВИРОВАТЬ", command=enable).place(x=10, y=165, width=330)
ttk.Button(text="ДЕАКТИВИРОВАТЬ", command=disable).place(x=10, y=195, width=330)

root.mainloop()
