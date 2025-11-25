print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Choose your favourite programming language")
root.geometry("400x300")

# Biến lưu lựa chọn
v = tk.StringVar()
v.set("Python")  # giá trị mặc định

# Danh sách ngôn ngữ
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị kết quả
def ShowChoice():
    choice = v.get()
    tk.Label(root, text=f"Your favourite programming language: {choice}",
             font=("Arial", 12), fg="blue").pack(pady=20)

# Tiêu đề
tk.Label(root, text="Choose your favourite programming language:",
         font=("Arial", 14)).pack(pady=20)

# Tạo các Radio Button (có indicator đẹp như hình)
for lang, val in languages:
    tk.Radiobutton(root,
                   text=lang,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=lang,           # giá trị là tên ngôn ngữ
                   indicatoron=True,     # hiển thị chấm tròn (indicator)
                   ).pack(anchor=tk.W)

# Nút Justify (không bắt buộc, nhưng có trong hình)
tk.Button(root, text="Justify", width=10).pack(pady=10)

root.mainloop()
