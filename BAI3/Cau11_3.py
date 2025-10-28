print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
def fib(k):
    if k <= 0:
        return 0
    elif k == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, k + 1):
        a, b = b, a + b
    return b

# Nhập k
k = int(input("Nhập số thứ tự k (bắt đầu từ 0): "))
print(f"Số Fibonacci thứ {k} là: {fib(k)}")
