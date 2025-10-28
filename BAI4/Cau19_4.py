print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

P = tuple(i for i in range(2, 1_000_000) if is_prime(i))
print("Tuple số nguyên tố < 1 triệu:")
print(P[:10], "... (tổng cộng:", len(P), "số)")
