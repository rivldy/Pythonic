a = 10
b = 20
print('sebelum pertukaran')
print(f'a={a}, b={b}')
c = a
a = b
b = c
print('setelah pertukaran')
print(f'a={a}, b={b}')

# Pythonic
a, b = 10, 20
print('sebelum pertukaran')
print(f'a={a}, b={b}')
a, b= b, a
print('setelah pertukaran')
print(f'a={a}, b={b}')