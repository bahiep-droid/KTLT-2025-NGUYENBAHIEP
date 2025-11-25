print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# Đọc file và in từng dòng theo thứ tự ngược lại
with open('ada.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()          
# In ngược lại
for line in reversed(lines):
    print(line.strip())                 
