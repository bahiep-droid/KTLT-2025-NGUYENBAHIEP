print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import turtle
import random

# Danh sách màu
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Thiết lập
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)  # vẽ nhanh nhất
turtle.bgcolor("black")  # nền đen để nổi màu

for i in range(10):  # vẽ 10 vòng tròn lồng nhau
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)

turtle.done()
