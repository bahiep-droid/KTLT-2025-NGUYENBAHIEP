print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Welcome")
window.geometry("420x280")
window.resizable(False, False)  # không cho thay đổi kích thước

# ------------------- a) Các ô nhập thông tin cá nhân -------------------
tk.Label(window, text="HỌ VÀ TÊN:", font=("Arial", 10)).place(x=20, y=20)
entry_hoten = tk.Entry(window, width=35)
entry_hoten.place(x=120, y=20)

tk.Label(window, text="NGÀY SINH:", font=("Arial", 10)).place(x=20, y=60)
entry_ngaysinh = tk.Entry(window, width=35)
entry_ngaysinh.place(x=120, y=60)
entry_ngaysinh.insert(0, "dd/mm/yyyy")  # gợi ý

tk.Label(window, text="MSSV:", font=("Arial", 10)).place(x=20, y=100)
entry_mssv = tk.Entry(window, width=35)
entry_mssv.place(x=120, y=100)

# ------------------- b) 3 Radio Button + Nút Click Me -------------------
# Biến lưu lựa chọn radio
lua_chon = tk.IntVar()
lua_chon.set(1)  # mặc định chọn First

tk.Radiobutton(window, text="First", variable=lua_chon, value=1).place(x=80, y=160)
tk.Radiobutton(window, text="Second", variable=lua_chon, value=2).place(x=180, y=160)
tk.Radiobutton(window, text="Third", variable=lua_chon, value=3).place(x=280, y=160)

# Hàm xử lý khi nhấn nút Click Me
def click_me():
    ten = entry_hoten.get().strip()
    ngaysinh = entry_ngaysinh.get().strip()
    mssv = entry_mssv.get().strip()
    chon = lua_chon.get()
    
    if ten == "" or ngaysinh == "" or ngaysinh == "dd/mm/yyyy" or mssv == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    # Chuẩn hóa ngày sinh
    try:
        ngay_sinh = datetime.strptime(ngaysinh, "%d/%m/%Y").strftime("%d/%m/%Y")
    except:
        ngay_sinh = ngaysinh
    
    # Hiển thị thông báo đẹp
    messagebox.showinfo("Thông tin của bạn",
                        f"Họ và tên: {ten}\n"
                        f"Ngày sinh: {ngay_sinh}\n"
                        f"MSSV: {mssv}\n"
                        f"Lựa chọn của bạn: Thứ {chon}")

# Nút Click Me
btn = tk.Button(window, text="Click Me", width=12, height=2, 
                bg="lightblue", command=click_me)
btn.place(x=300, y=200)

# Tiêu đề Welcome ở trên cùng
tk.Label(window, text="Welcome", font=("Arial", 16, "bold")).place(x=180, y=200)

# Chạy chương trình
window.mainloop()
