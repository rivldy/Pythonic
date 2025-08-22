def tambah(a, b):
	return a + b

def kali(a, b):
	return a * b

x, y = 10, 20
kondisi = True
if kondisi:
	hasil = tambah(x, y)
else:
	hasil = kali(x, y)
print(f'hasil: {hasil}')

# Pythonic
def tambah(a, b):
	return a + b

def kali(a, b):
	return a * b

x, y = 10, 20
kondisi = True
hasil = (tambah if kondisi else kali)(x, y)
print(f'hasil: {hasil}')