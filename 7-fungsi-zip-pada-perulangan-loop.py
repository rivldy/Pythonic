nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
for i, data_nama in enumerate(nama):
	print(f'{nim[i]}--{data_nama}')

# Pythonic
nim = ['001', '002', '003']
nama = ['bejo', 'karti', 'tejo']
hobi = ['makan', 'nyanyi', 'tidur']
for d_nim, d_nama, d_hobi in zip(nim, nama, hobi):
	print(f'{d_nim}--{d_nama}--{d_hobi}')