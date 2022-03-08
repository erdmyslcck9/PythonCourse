# numbers = [1,2,3,4,5]
# 1-100'e kadar

'''

x = 1
while x <= 100:
    if(x % 2 == 1):
        print(f'tek sayı: {x}')
    else:
        print(f'çift sayı: {x}')
    x += 1

print('bitti...')

'''

name = '' #False

while not name.strip():            # .strip() kullanıcı boşluk girerse siler.
    name = input('Enter name: ')

print(f'Merhaba, {name}')
