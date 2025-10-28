print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
s = input("Nhập câu: ")
hoa = 0
thuong = 0

for char in s:
    if char.isupper():
        hoa += 1
    elif char.islower():
        thuong += 1

print(f"Chữ hoa: {hoa}")
print(f"Chữ thường: {thuong}")
