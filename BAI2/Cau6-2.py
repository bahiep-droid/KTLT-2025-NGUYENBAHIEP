print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
j = []
for i in range(2000, 3210):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))        
