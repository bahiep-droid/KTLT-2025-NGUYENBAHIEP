print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import math

# Khởi tạo vị trí robot
pos = [0, 0]  # [x, y]

while True:
    s = input()
    if not s:  # Nếu nhập rỗng (Enter) thì dừng
        break
    movement = s.split(" ")
    direction = movement[0].upper()  # Lấy hướng, chuyển thành chữ hoa
    steps = int(movement[1])         # Lấy số bước

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        pass  # Bỏ qua lệnh không hợp lệ

# Tính khoảng cách Euclidean
distance = math.sqrt(pos[0]**2 + pos[1]**2)

# Làm tròn về số nguyên gần nhất
print(round(distance))
