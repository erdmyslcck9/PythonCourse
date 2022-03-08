'''

numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

names = ["Erdem", "Buğra", "Osman"]

for name in names:
    print(f'my name is {name}')


name = 'Erdem Yeşilçiçek'

for n in name:
    print(n)

'''

'''

tuple = (1,2,3,4,5)

for t in tuple:
    print(t)


tuple = [(1,2),(3,4),(5,9)]

for a,b in tuple:
    print(a)  # yalnızca ilk elemanları alır
    print(b)  # yalnızca ikinci elemanları alır

'''

d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print(item)

for item in d.items():    # d.items() eleman gruplarına tek tek ulaşmak için kullanırız.
    print(item)

for key,value in d.items():
    print(key, value)