print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import turtle
import random

colors = ["#ff0000", "#ff8800", "#ffff00", "#00ff00", "#0088ff", "#0000ff", "#ff00ff"]

turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(4)
turtle.hideturtle()

for i in range(50):
    turtle.pencolor(random.choice(colors))
    turtle.circle(110)
    turtle.left(7.2)  # 360/50 = 7.2 → chia đều

turtle.done()
