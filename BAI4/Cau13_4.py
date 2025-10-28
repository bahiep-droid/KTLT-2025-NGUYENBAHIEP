print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
ds = ['hello', 'abc', 'world', 'abc', 'python']

print("Danh sách:", ds)

try:
    vi_tri = ds.index('abc')
    print("Vị trí đầu tiên của 'abc':", vi_tri)
except ValueError:
    print("'abc' không có trong danh sách")

vi_tri_tat_ca = [i for i, x in enumerate(ds) if x == 'abc']
print("Tất cả vị trí của 'abc':", vi_tri_tat_ca)
