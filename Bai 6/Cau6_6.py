print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.str1.upper())

# Sử dụng class
obj = IOString()
obj.get_String()
obj.print_String()
