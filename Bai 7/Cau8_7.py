print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# Danh sách mẫu
my_list = ["Xin chào", "Đây là dòng thứ hai", "Python rất thú vị"]

# Ghép danh sách thành một chuỗi duy nhất, cách nhau bởi dấu cách
content = " ".join(my_list)

# Ghi chuỗi vào file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Đã ghi danh sách thành một chuỗi duy nhất vào file output.txt")
