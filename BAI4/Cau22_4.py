print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
ket_qua = []
for num in range(1000, 3001):
    s = str(num)
    if all(int(d) % 2 == 0 for d in s):
        ket_qua.append(s)

print(','.join(ket_qua))
