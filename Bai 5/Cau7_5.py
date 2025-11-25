print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
import numpy as np

data_type = [('name', 'U10'), ('class', 'U10'), ('height', float)]

students_data = [
    ('James', '5', 48.5), ('Nail', '6', 52.5), ('Paul', '5', 42.10),
    ('Pit', '5', 40.11)
]

students = np.array(students_data, dtype=data_type)

print("Original array:")
print(students)

print("\nSort by height:")
print(np.sort(students, order='height'))
