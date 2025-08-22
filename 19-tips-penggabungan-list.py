a = [10, 'budi', 30.55]
b = [False, 50, 'wati']
c = [None]*(len(a) + len(b))
for i in range(len(a)):
	c[i] = a[i]
for i in range(len(b)):
	c[i+len(a)] = b[i]
print(f'c: {c}')

# Pythonic
a = [10, 'budi', 30.55]
b = [False, 50, 'wati']
c = a + b
print(f'c: {c}')