import tkinter as tk


def appear_and_disappear(number, duration=1000):
    root = tk.Tk()
    root.title("Number Displayer")

    label = tk.Label(root, text=number, font=("Arial", 48))
    label.pack(pady=50)

    def close_window():
        root.destroy()

    root.after(duration, close_window)
    root.mainloop()