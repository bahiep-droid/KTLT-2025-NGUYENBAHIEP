print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import tkinter as tk
from tkinter import ttk

# ------------------- CÂU 4 -------------------
window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")

# Label chào
lbl = tk.Label(window, text="Hello", font=("Arial", 20))
lbl.grid(column=0, row=0)

# Hàm khi nhấn nút
def clicked():
    lbl.configure(text="Button was clicked !!")

# Nút Click Me
btn = tk.Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)

# Thay đổi màu nền và chữ của button (theo yêu cầu d)
btn.configure(bg="orange", fg="black")   # hoặc dùng bg="bg", fg="fg" đều được

window.mainloop()
