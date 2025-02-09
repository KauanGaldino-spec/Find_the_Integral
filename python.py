def integrate(coefficient, exponent):
     new_exponent = exponent + 1
     new_coefficient = coefficient // new_exponent
     return f"{new_coefficient}x^{new_exponent}"

print(integrate(3, 2))
print(integrate(12, 5))
print(integrate(20, 1))
print(integrate(40, 3))
print(integrate(90, 2))
