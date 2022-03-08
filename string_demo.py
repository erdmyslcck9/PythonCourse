website = "http://www.erdembey.com"
course = "Python Kurus: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

result = len(course)
length = len(website)
# 2- 'website' içinden www karakterlerini alın.

result = website[7:10]

# 3- 'website' içinden com karakterlerini alın.

result = website[22:25]
result = website[length-3:length]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

result = course[:15]
result = course[14:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::] #tüm karakterleri alır.

s = '123456789' * 7
print(s[::3]) # 3'er 3'er alır.

name, surname, age, job = 'Erdem','Yeşilçiçek', 18, 'Bilgisayar Mühendisliği'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Erdem Yeşilçiçek, yaşım 18 ve mesleğim Bilgisayar Mühendisliği'

result = "Benim adım "+ name + " " + surname + ", " + "yaşım " + str(age) + " ve mesleğim " + job
result = 'Benim adım {} {}, yaşım {} ve mesleğim {}.'.format(name,surname,age, job)
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

e = 'Hello world'
e = e[0:6] + 'W' + e[-4:]
e.replace('w','W')

print(e)

# 8- 'Erdem' ifadesini 3 defa yazdrın.

result = 'Erdem ' * 3

print(result)