print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
ds = input("Nhap day tu: ").split()
do_dai_max = 0
tu_dai_nhat = []

for tu in ds:
    if len(tu) > do_dai_max:
        do_dai_max = len(tu)
        tu_dai_nhat = [tu]
    elif len(tu) == do_dai_max:
        tu_dai_nhat.append(tu)

print("Tu dai nhat:", tu_dai_nhat)
