print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# Đọc nội dung từ file văn bản
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Tách nội dung thành các từ (dựa trên khoảng trắng)
words = content.split()

# Tìm độ dài lớn nhất
max_length = max(len(word) for word in words)

# Lọc ra những từ có độ dài bằng độ dài lớn nhất
longest_words = [word for word in words if len(word) == max_length]

print(f"Độ dài lớn nhất: {max_length}")
print("Những từ dài nhất trong văn bản là:")
for w in longest_words:
    print(w)
