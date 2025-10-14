print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import math
a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
c=float(input('Nhap c: '))

if a==0:
        if b==0:
            print('Phuong trinh vo nghiem')
        else:
            print('Phuong trinh co mot nghiem:', -c/b)
else:
    delta=b**2-4*a*c
    if delta < 0:
        print('Phuong trinh vo nghiem:')
    elif delta ==0:
        x=b/ (2*a)
        print('Phuong trinh co nghiem kep x1=x2', x)
    else:
        x1=(-b + math.sqrt(delta)) / (2*a)
        x2=(-b - math.sqrt(delta)) / (2*a)
        print('Phuong tring co hai nghiem phan biet')
        print('x1=', x1, ',x2=', x2)

