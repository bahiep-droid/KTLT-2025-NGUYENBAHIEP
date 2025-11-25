print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class HinhChuNhat:
    def __init__(self, dai, rong):
        self.chieudai = dai
        self.chieurong = rong

    def area(self):
        return self.chieudai * self.chieurong

# Ví dụ
hcn = HinhChuNhat(5, 3)
print(hcn.area()) 
