def square(n): return n*n
def cube(n): return n*n*n
def average(values):
    return float(sum(values))/len(values) if values else 0.0

values = [2,4,6,8,10]
print("Values:", values)
print("Squares:", [square(v) for v in values])
print("Cubes:", [cube(v) for v in values])
print("Average:", average(values))
print()
