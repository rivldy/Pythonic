nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
for i in range(len(nim)):
	print(f'{nim[i]}--{nama[i]}')

# Pythonic
nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
for i, data_nim in enumerate(nim):
	print(f'{data_nim}--{nama[i]}')