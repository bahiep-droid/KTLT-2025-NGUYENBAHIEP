print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
tong = 0
print("Nhập nhật ký giao dịch (D/R + số tiền), nhập dòng trống để kết thúc:")

while True:
    line = input()
    if not line.strip():
        break
    loai, so_tien = line.split()
    so_tien = int(so_tien)
    if loai == 'D':
        tong += so_tien
    elif loai == 'W':
        tong -= so_tien

print("Số dư cuối cùng:", tong)
