names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz asd

# names.append("Cenk")
# print(names)

# 2- "Sena" değerini listenin başına ekleyiniz

# names.insert(0, "Sena")
# print(names)

# 3- "Deniz" ismini listeden siliniz

# names.remove("Deniz")
# print(names)

# 4- "Deniz" isminin index'i nedir?

# index = names.index('Deniz')
# print(index)

# 5- "Ali", listenin bir elemanı mıdır?

# result = 'Ali' in names
# print(result)

# 6- Liste elemanlarını ters çevirin

# names.sort()
# names.reverse()
# print(names)

# 7- Liste elemanlarını alfabetif olarak sıralayınız

# names.sort()
# print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız

# years.sort()
# years.reverse()
# print(years)

# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

# str = "Chevrolet,Dacia"
# result = str.split(',')
# print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir?

# min = min(years)
# max = max(years)
# print (min, max)

# 11- years dizisinde kaç tane 1998 değeri vardır? 

# print(years.count(1998))

# 12- years dizisinin tüm elemanlarnı siliniz.

# years.clear()
# print(years)

# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız

x = input("Choose your first brand: ")
y = input("choose your second brand: ")
z = input("choose your third brand: ")

list1 = [x, y, z]
print(list1)