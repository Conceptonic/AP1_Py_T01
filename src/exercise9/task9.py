first_line = input().split()
degree = int(first_line[0])
x = float(first_line[1])

coeffs = [float(input()) for _ in range(degree + 1)]

# coeffs[0] is for x^degree, coeffs[1] for x^(degree-1), ..., coeffs[degree] for x^0
# Derivative term for coeffs[i] * x^(degree-i) is (degree-i) * coeffs[i] * x^(degree-i-1)
result = 0.0
for i in range(degree):
    power = degree - i
    result += power * coeffs[i] * (x ** (power - 1))

print(f"{result:.3f}")
