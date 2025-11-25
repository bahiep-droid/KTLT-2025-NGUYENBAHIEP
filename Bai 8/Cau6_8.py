print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import tkinter as tk
from tkinter import messagebox, filedialog

# ------------------- BƯỚC 3: Các hàm xử lý -------------------
def NewFile():
    messagebox.showinfo("New File", "Bạn đã chọn: New File!")

def OpenFile():
    messagebox.showinfo("Open File", "Bạn đã chọn: Open File!")
    # Có thể mở filedialog thật nếu muốn
    # file = filedialog.askopenfilename()

def Exit():
    if messagebox.askyesno("Thoát chương trình", "Bạn có chắc muốn thoát không?"):
        root.destroy()

def InsText():
    messagebox.showinfo("Insert", "Bạn đã chọn: Text")

def InsPic():
    messagebox.showinfo("Insert", "Bạn đã chọn: Picture")

def About():
    messagebox.showinfo("About", "Đây là chương trình demo Menu Tkinter\nTác giả: Bạn của Grok")

# ------------------- Tạo cửa sổ chính -------------------
root = tk.Tk()
root.title("tk")
root.geometry("400x300")

# ------------------- Tạo thanh Menu -------------------
menu = tk.Menu(root)
root.config(menu=menu)

# Menu File
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()                    # đường kẻ ngang
filemenu.add_command(label="Exit", command=Exit)

# Menu Insert
insertmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Menu Help
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# ------------------- Chạy chương trình -------------------
root.mainloop()
