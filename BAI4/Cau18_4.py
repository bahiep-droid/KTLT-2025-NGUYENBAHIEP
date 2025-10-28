print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
n = int(input("Nhap n: "))
fib = [0, 1]
while True:
    next_fib = fib[-1] + fib[-2]
    if next_fib >= n:
        break
    fib.append(next_fib)

print(fib)
