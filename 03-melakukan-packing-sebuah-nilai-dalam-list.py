a = 10
b = 20
c = 30
d = [None]*3
d[0] = a
d[1] = b
d[2] = c
print(f'a={a}, b={b}, c={c}')
print(f'd={d}')

# Pythonic
a, b, c = 10, 20, 30
d = [a, b, c]
print(f'a={a}, b={b}, c={c}')
print(f'd={d}')