print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
def get_sum(*num):
    tmp=0
    for i in num:
        tmp += i
    return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)
