print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
str=input('Enter a string')
words=str.split()
d={}
for word in words:
    d[word]=d.get(word, 0)+1
print(d)    
