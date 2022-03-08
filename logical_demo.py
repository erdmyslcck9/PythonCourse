# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

# x = int(input("Enter number: "))
# result = (x > 0) and (x < 100)
# print(result)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

# x = int(input("Enter number: "))
# result = (x > 0) and (x % 2 == 0)
# print(result)

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız

# email    = "erdem@gmail.com"
# password = "erd999"
# enteremail    = input("Enter email: ")
# enterpassword = input("Enter password: ")
# result = (enteremail == email) and (enterpassword == password)
# print(result)

# 4- Girilen üç sayıyı büyüklük olarak karşılaştırınız

"""

firstnumber  = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
thirdnumber  = int(input("Enter third number: "))

result = (firstnumber > secondnumber) and (firstnumber > thirdnumber)
print(f'firstnumber en büyük sayıdır: {result}')

result = (secondnumber > firstnumber) and (secondnumber > thirdnumber)
print(f'secondnumber en büyük sayıdır: {result}')

result = (thirdnumber > secondnumber) and (thirdnumber > firstnumber)
print(f'thirdnumber en büyük sayıdır: {result}')

"""

# 5- Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesalayınız
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#    a-) Ortalama 50olsa bile final notu en az 50 olmalıdır
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın

"""

firstVisa  = float(input("Enter first visa: "))
secondVisa = float(input("Enter second visa: "))
firstFinal = float(input("Enter final: "))

average = (((firstVisa + secondVisa)/2) * 0.6) + (firstFinal * 0.4)

result = (average >= 50) and (firstFinal >= 50)                        # A MADDESİNİN ÇÖZÜMÜ
result = (average >= 50) or (firstFinal >= 70)                         # B MADDESİNİN ÇÖZÜMÜ

print(f'Öğrencinin ortalaması: {average} ve geçme durumu: {result}')

"""

# 6- Kişinin ad, kilo, boy bilgilerini alıp kilo indekslerini hesaplayınız
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

"""

name   = input("Enter name: ")
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

weightIndex = (weight / (height ** 2))

thin       = (weightIndex > 0)    and (weightIndex < 18.4)
normal     = (weightIndex > 18.5) and (weightIndex < 24.9)
overweight = (weightIndex > 25.0) and (weightIndex < 29.9)
Obese      = (weightIndex > 30.0) and (weightIndex < 34.9)
megaObese  = (weightIndex > 34.9)

print(f'{name} kilo indeksin: {weightIndex} ve kilo değerlendirmen zayıf: {thin}')
print(f'{name} kilo indeksin: {weightIndex} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {weightIndex} ve kilo değerlendirmen fazla kilolu: {overweight}')
print(f'{name} kilo indeksin: {weightIndex} ve kilo değerlendirmen obez: {Obese}')
print(f'{name} kilo indeksin: {weightIndex} ve kilo değerlendirmen mega obez: {megaObese}')

"""

