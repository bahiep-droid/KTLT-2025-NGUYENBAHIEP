print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import math

def Tinh(R):
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    return chu_vi, dien_tich

# Nhập bán kính
R = float(input("Nhập bán kính R: "))

# Tính toán
cv, dt = Tinh(R)

# In kết quả
print(f"Chu vi hình tròn: {cv:.2f}")
print(f"Diện tích hình tròn: {dt:.2f}")
