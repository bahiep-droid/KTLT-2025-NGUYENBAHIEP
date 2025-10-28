print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
# Hàm cộng
def add(x, y):
    return x + y

# Hàm trừ
def subtract(x, y):
    return x - y

# Hàm nhân
def multiply(x, y):
    return x * y

# Hàm chia
def divide(x, y):
    if y == 0:
        return "Lỗi: Không thể chia cho 0!"
    return x / y

# Hiển thị menu
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Nhập lựa chọn và 2 số
choice = input("Enter choice (1/2/3/4): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Xử lý theo lựa chọn
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    result = divide(num1, num2)
    print(num1, "/", num2, "=", result)
else:
    print("Invalid input")
