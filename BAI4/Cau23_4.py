print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
s = input("Nhập câu: ")
chu_cai = 0
chu_so = 0

for char in s:
    if char.isalpha():
        chu_cai += 1
    elif char.isdigit():
        chu_so += 1

print(f"Số chữ cái: {chu_cai}")
print(f"Số chữ số: {chu_so}")
