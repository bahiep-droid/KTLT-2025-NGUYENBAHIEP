print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
s = input("Nhap chuoi: ")
ket_qua = ""
for ch in s:
    if not ch.isdigit():  
        ket_qua += ch
print(ket_qua)
