numbers = [1,3,5,7,9,12,19,21]

# 1- numbers listesini while ile ekrana yazdırın.

# i = 0
# while (i < len(numbers)):
#     print(numbers[i])
#     i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana basın

"""

firstnum  = int(input('Enter first number: '))
secondnum = int(input('Enter second number: '))

while (firstnum <= secondnum):
    if(firstnum % 2 == 1):
        print(firstnum)
    firstnum += 1 

"""

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın

# i = 100
# while i > 0:
#     i -= 1
#     print(i)

# 4- kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.

# number1 = []

# i = 0

# while i < 5:
#     num = int(input('num: '))
#     number1.append(num)
#     i+=1
# number1.sort()      # .sort() metodu sayıları değerlerine göre sıralamamıza yarar
# print(number1)

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
#    ** ürün sayısını kullanıcıya sorun
#    ** dictionary yapısı (name, price) şeklinde olsun
#    ** ürün ekleme işi bittiğinde ürünleri ekrana while ile listeleyiniz

products = []

count = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while (i < count):
    name  = input('ürün ismi: ')
    price = input('ürün fiyatı: ') 
    products.append({
        'name': name,
        'price': price
    })
    i += 1

for p in products:
    print(f"ürün adı: {p['name']} ürün fiyatı: {p['price']}")
