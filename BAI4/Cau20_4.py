print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
from math import comb

n = int(input("Nhập n: "))
pascal_line = [comb(n, k) for k in range(n + 1)]
print("Dòng", n, "của tam giác Pascal:", pascal_line)
