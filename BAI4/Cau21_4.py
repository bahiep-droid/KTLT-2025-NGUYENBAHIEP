print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
chuoi = input("Nhập các số nhị phân 4 chữ số (cách nhau bởi dấu phẩy): ")
ds = chuoi.split(',')
ket_qua = []

for bin_str in ds:
    bin_str = bin_str.strip()
    if len(bin_str) == 4 and all(c in '01' for c in bin_str):
        so_thap_phan = int(bin_str, 2)
        if so_thap_phan % 5 == 0:
            ket_qua.append(bin_str)

print("Các số chia hết cho 5:", ','.join(ket_qua))
