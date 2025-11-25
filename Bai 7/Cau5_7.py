print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# 5. Ghi thêm (append) nội dung vào file và hiển thị lại
with open('ada.txt', 'a', encoding='utf-8') as f:   # 'a' = append
    f.write("Python Exercises\n")
    f.write("Java Exercises\n")

# Đọc lại và hiển thị toàn bộ nội dung
with open('myfile.txt', 'r', encoding='utf-8') as f:
    print(f.read())
