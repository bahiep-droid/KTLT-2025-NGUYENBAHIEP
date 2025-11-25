print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import turtle

# Thiết lập màn hình
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tạo con rùa
painter = turtle.Turtle()
painter.fillcolor("blue")
painter.pencolor("blue")
painter.pensize(3)

# Hàm vẽ một "cánh hoa" (thực ra là vòng tròn nhỏ)
def draw_sq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

# Vẽ tâm hoa (vòng tròn lớn ở giữa)
painter.begin_fill()
for i in range(180):
    painter.forward(18)
    painter.left(2)  # 360/180 = 2 độ mỗi lần
painter.end_fill()

# Vẽ các cánh hoa xung quanh (18 cánh)
for i in range(18):
    painter.penup()
    painter.goto(0, 0)
    painter.setheading(i * 20)  # chia 360 độ thành 18 phần → mỗi cánh cách 20 độ
    painter.forward(200)
    painter.pendown()
    draw_sq(painter, 100)  # vẽ hình vuông làm cánh hoa
    painter.penup()
    painter.goto(0, 0)

window.mainloop()
