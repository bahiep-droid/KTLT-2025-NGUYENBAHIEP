print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class Circle:
    def __init__(self, ban_kinh):
        self.r = ban_kinh

    def dien_tich(self):
        return 3.14 * self.r * self.r

    def chu_vi(self):
        return 2 * 3.14 * self.r

# Kiểm tra
hinh_tron = Circle(5)
print(f"Diện tích: {hinh_tron.dien_tich()}")   
print(f"Chu vi: {hinh_tron.chu_vi()}")      
