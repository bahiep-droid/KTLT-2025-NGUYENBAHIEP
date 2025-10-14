print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
a, b = 1, 2
total=0
print("a,end=', end=")
while(a<=4000000):
    if a%2==0:
        total +=a
    a, b=b, a+b
print("sum of prime numbers tern in fibonacci series: ", total)  
