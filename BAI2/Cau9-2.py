print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
str=input('Enter a string:')
dict_={}
for i in str:
    dict_[i]=dict_.get(i, 0)+1
print(dict_)    

          
