import math

x = 1

# true value of e^1
x_true = math.exp(x)

# 3 steps Maclaurin series
x_approx = 1 + x + (x**2)

# E(r) = | x(true) - x(approx) |
e_rounding_error = abs(x_true - x_approx)

print("True value of e^1: ", x_true)  # 2.718281828459045
print("Approximate value of e^1 (3 steps): ", x_approx)  # 3
print("Rounding error : ", e_rounding_error)  # 0.2817181715409549
