'''

def change(n):
    n[0] = 'Erdem'

names = ['mustafa', 'buğra']
n = names[:] #slicing

n[0] = ' Erdem'

print(names)
print(n)

'''


# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# def add(a, b, c):
#     return sum((a,b,c))

# result = add(a, b, c)

# print(result)

def displayUser(**params):
    for key, value in params.items():
        print('{} is {}'.format(key,value))
    
displayUser(name = 'Erdem', age = 18, city = 'Trabzon')
displayUser(name = 'Su', age = 30, city = 'İstanbul', phone = '987987987')
displayUser(name = 'Şima', age = 27, city = 'Sakarya', phone = '645645645', email = 'sima@gmail.com')

# * yollanırsa tuple list, ** yollanırsa dictionary list oluşur.

def myFunc(e, y, *args, **kwargs):
    print(e)
    print(y)
    print(args)
    print(kwargs)
    print(args)

myFunc(9,10,7,6,5,4,23,21,34,45,56,67,78,89,809, key1 = 'value 1', key2 = 'value 2',  key3 = 'value 3')

#   ilk değerleri 'e' ve 'y'ye attı ondan sonra geriye kalan değerler ile *args'ta bir liste oluşturdu
#  son olarak **kwargs ile bir key value tarzı bir dic listesi oluşturdu.

