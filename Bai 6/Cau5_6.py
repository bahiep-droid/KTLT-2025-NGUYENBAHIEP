print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class PySolution:
    def reverse_words(self, s):
        return ' '.join(word[::-1] for word in s.split())

# Kiểm tra
print(PySolution().reverse_words('hello .py'))  
# Kết quả: olleh yp.
