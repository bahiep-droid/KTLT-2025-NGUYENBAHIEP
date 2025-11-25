print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# Mở file nguồn để đọc
with open("input.txt", "r", encoding="utf-8") as source:
    content = source.read()

# Mở file đích để ghi
with open("output.txt", "w", encoding="utf-8") as destination:
    destination.write(content)

print("Đã sao chép nội dung từ input.txt sang output.txt")
