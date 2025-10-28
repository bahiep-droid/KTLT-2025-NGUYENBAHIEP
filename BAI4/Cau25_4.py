print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
s = input("Nhập dãy số (cách nhau bởi dấu cách): ")
ds = list(map(int, s.split()))
le = [x for x in ds if x % 2 != 0]
print("Các số lẻ:", le)
