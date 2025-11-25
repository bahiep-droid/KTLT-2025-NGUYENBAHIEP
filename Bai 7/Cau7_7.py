print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# Mở file ở chế độ đọc
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Đếm số dòng
num_lines = len(lines)

print(f"Số dòng trong file là: {num_lines}")
