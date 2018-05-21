import tkinter as tk 
import random
window = tk.Tk()


def buttonClick():
    name = nameEntry.get()
    # result.delete(0, tk.END)
    # result.insert(0, sentence)

nameLabel = tk.Label(window, text="重力加速度:")

# nameLabel.grid(row=0)
nameEntry = tk.Entry(window)
nameEntry.insert(10, '5000')
# nameEntry.grid(row=0,column=1)

# button = tk.Button(window, text="确定", command=buttonClick)
button = tk.Button(window, text="确定", command=window.quit)

# result = tk.Entry(window)
nameLabel.pack()
nameEntry.pack()
button.pack()

window.mainloop()