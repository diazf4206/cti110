# Francis Diaz

# 03/03/2024

# P2LAB2

# Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

print(f'{num1 * num2 * num3 * num4:.0f} {(num1 + num2 + num3 + num4) / 4:.0f}')

print(f'{num1 * num2 * num3 * num4:.3f} {(num1 + num2 + num3 + num4) / 4:.3f}')
