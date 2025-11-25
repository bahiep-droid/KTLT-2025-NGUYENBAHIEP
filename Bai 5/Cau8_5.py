print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i  # Tìm thấy → trả về (True, chỉ số)
    return False, -1    # Không tìm thấy
# Test
arr = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
result = Sequential_Search(arr, 31)

print(f"Kết quả: {result}")  # (True, 3)

if result[0]:
    print(f"Tìm thấy {31} tại chỉ số: {result[1]}")
else:
    print(f"Không tìm thấy")
