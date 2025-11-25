print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
def tim_max_min(danh_sach):
    if not danh_sach:
        return None, None
    
    lon_nhat = danh_sach[0]
    nho_nhat = danh_sach[0]
    
    for num in danh_sach:
        if num > lon_nhat:
            lon_nhat = num
        if num < nho_nhat:
            nho_nhat = num
    
    return lon_nhat, nho_nhat

# Test
ds = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_val, min_val = tim_max_min(ds)
print("Phần tử lớn nhất:", max_val)
print("Phần tử nhỏ nhất:", min_val)
max_val, min_val = tim_max_min([])
if max_val is None:
    print("Danh sách rỗng, không có max/min")
else:
    print("Max:", max_val, "Min:", min_val)
