print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius ** 2 * 3.14 
aCircle = Circle(2)

print(aCircle.area())
