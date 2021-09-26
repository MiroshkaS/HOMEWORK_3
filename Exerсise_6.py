print("Стороны треугольника")
a, b, c = float(input('A=')), float(input('B=')), float(input('C='))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else: print("Треугольник не существует")