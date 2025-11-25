print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# 2. Đếm ký tự, từ, dòng
char_count = word_count = line_count = 0

with open('ada.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_count += 1
        char_count += len(line)
        word_count += len(line.split())  

print(f"The no. of chars is {char_count}\nThe no. of words is {word_count}\nThe no. of lines is {line_count}")
