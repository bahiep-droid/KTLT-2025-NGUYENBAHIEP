print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class Nguoi:
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Kiểm tra
aNam = Nam()
aNu = Nu()

print(aNam.getGender())  # Kết quả: Nam
print(aNu.getGender())   # Kết quả: Nữ

# Thử với class cha
aNguoi = Nguoi()
print(aNguoi.getGender())  # Kết quả: Unknown
