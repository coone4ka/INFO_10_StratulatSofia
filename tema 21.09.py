print ('Struguri','100','kg', sep='    ',end='\n')
print ('Mere','10','tone', sep='        ',end='\n')
print ('Cartofi','250','kg', sep='     ',end='\n')
print ('Varza','1000','q', sep='       ',end='\n')

a = 5
b = 2
print ('Suma = ', a + b)
print ('Diferența = ', a - b)
print ('Produsul = ', a - b)
print ('Câtul este = ', a // b)
print('Restul este =', a % b)
print ('Puterea este =', a ** b)

l = 4
print('Perimetrul cubului este: ' , 4 * l )
print('Aria cubului este: ', 12 * l )
print('Volumul cubului este: ', l ** 3)

n = 14
cm = n * 100
mg = n * 1000000
luni = n * 12
saptamani = n * 52
zile = n * 365
print(n, 'metri', '=', cm, 'cm')
print(n, 'kg', '=', mg, 'mg')
print(n, 'ani', '=', luni, 'luni')
print(n, 'ani', '=', saptamani, 'săptămâni')
print(n, 'ani', '=', zile, 'zile')

x = True
y = False 
print(x and y)
print(x or y)
print(not x)
print(not y)

n_1 = 5267
print('Ultima cifră al acestui număr este', n_1 % 10 )
print('Penultima cifră al acestui număr este', (n_1 // 10) % 10 )
print('Restul împărțirii acestui număr cu 9 este', n_1 % 9 )
print('Câtul împărțirii acestui număr cu 9 este', int(n_1 % 9) )
print('Suma cifrelor acestui număr este', (n_1 // 1000) + ((n_1 // 100) % 10) + ((n_1 // 10) % 10) + (n_1 % 10) )
print('Răsturnatul acestui număr este', (n_1 % 10)*1000 + ((n_1 // 10) % 10) * 100 + ((n_1 // 100) % 10) * 10 + (n_1 // 1000))