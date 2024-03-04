# Francis Diaz

# 03/03/2024

# P2LAB1

# Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.
  
miles_gal = float(input())
dollars_gal = float(input())

print(f'{dollars_gal / miles_gal * 20:.2f} {dollars_gal / miles_gal * 75:.2f} {dollars_gal / miles_gal * 500:.2f}')
