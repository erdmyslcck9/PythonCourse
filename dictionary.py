# key = value

# 41 => Kocaeli 34 => İstanbul

"""

DİCTİONARY KULLANMADAN, LİSTE YÖNTEMİ İLE NASIL YAZILIR

citys  = ['kocaeli', 'istanbul']
plates = [41, 34]

print(plates[citys.index('istanbul')])

"""

# print(plakalar['kocaeli'])  => 41 
# print(plakalar['istanbul']) => 34

# plates = {'kocaeli' : 41, 'istanbul' : 34}
# print(plates['kocaeli'])
# print(plates['istanbul'])

# plates['ankara'] = 6
# print(plates)

users = {
    'erdmyslcck9': {
        'age': 18,
        'email': 'erdem@gmail.com',
        'address': 'Nevşehir',
        'phone': '99856458'
    },
    'bgrarslan': {
        'age': 18,
        'email': 'bgr@gmail.com',
        'address': 'İstanbul',
        'phone': '88574565412'
    }
}

print(users['erdmyslcck9']['phone'])
print(users['erdmyslcck9']['age'])
print(users['erdmyslcck9']['email'])