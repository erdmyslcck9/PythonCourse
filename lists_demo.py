# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2- Liste kaç elemanlıdır ?

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# result = len(cars) 
# print(result)

# 3- Listenin ilk ve son elemanı nedir?

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# result = cars[0]
# result = cars[3]
# print(result)

# 4- Mazda değerini Toyota ile değiştirin.

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# cars[-1] = "Toyota"
# print(cars)

# 5- Mercedes listenin bir elemanı mıdır?

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# isTrue = "Mercedes" in cars  
# print(isTrue)
# in operatörü 'içinde var mı?' araması yapar

# 6- Listenin -2 indeksindeki değer nedir?

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# result = cars[-2]
# print(result)

# 7- Listenin ilk 3 elemanını alın

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# result = cars[0:3]
# print(result)

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" ekleyin 

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# cars[-2:] = ['Toyota', 'Renault']
# print(cars)

# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# result = cars + ["Audi", "Nissan"]
# print(result)

# 10- Listenin son elemanını silin.

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# del cars[-1] 
# result = cars
# print(result)
# del komutu istediğini silmene yardımcı olur.

# 11- Liste elemanlarını tersten yazınız.

# cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# x = cars[::-1]
# print(x)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

# studentA: Erdem Yeşilçiçek  2010,  (70,60,70)
# studentB: Mustafa Burak     1999,  (80,80,70)
# studentC: Buğra Arslan      1998,  (80,70,90)

# studentA = ["Erdem","Yeşilçiçek",2010,[70,60,70]]
# studentB = ["Mustafa","Burak",1999,[80,80,70]]
# studentC = ["Buğra","Arslan",1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

# studentA = ["Erdem","Yeşilçiçek",2010,[70,60,70]]
# studentB = ["Mustafa","Burak",1999,[80,80,70]]
# studentC = ["Buğra","Arslan",1998,[80,70,90]]
# result = studentA[0]
# result = studentA[1]
# result = studentA[2]
# result = studentA[3]
# result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {studentA[3][0] + studentA[3][1] + studentA[3][2]/3} "
# print(result)