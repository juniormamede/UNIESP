import math

# Input the values of A, B, and C
A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: "))
C = float(input("Enter the value of C: "))

# Calculate the discriminant (Delta)
delta = B**2 - 4*A*C

# Check the value of delta
if delta > 0:
    # Two distinct real roots
    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)
    print("The equation has two distinct real roots:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    # One real root (repeated)
    x = -B / (2*A)
    print("The equation has one real root (repeated):")
    print("x =", x)
else:
    # No real roots (complex roots)
    real_part = -B / (2*A)
    imaginary_part = math.sqrt(-delta) / (2*A)
    print("The equation has two complex roots:")
    print("x1 =", real_part, "+", imaginary_part, "i")
    print("x2 =", real_part, "-", imaginary_part, "i")
