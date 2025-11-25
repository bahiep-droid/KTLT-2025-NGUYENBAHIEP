print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
with open('ada.txt', 'r', encoding='utf-8') as f:
    last_line = f.readlines()[-1].strip()
    print(last_line)
