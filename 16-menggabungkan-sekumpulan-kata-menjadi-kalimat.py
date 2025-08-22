listku = ['belajar', 'python', 'dasar']
kalimat = ''
for kata in listku:
	kalimat += kata + ' '
print(f'listku: {listku}')
print(f'kalimat: {kalimat}')

# Pythonic
listku = ['belajar', 'python', 'dasar']
kalimat = ' '.join(listku)
print(f'listku: {listku}')
print(f'kalimat: {kalimat}')