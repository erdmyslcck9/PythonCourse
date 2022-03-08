# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

# number = int(input("Enter number: "))
# result = (number > 0) and (number < 100)
# print(result)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

# number = int(input("Enter number: "))
# result = (number > 0) and (number % 2 == 0)
# print(result)

# 3- email ve parola giriş belgeleri ile giriş konrolu yapınız

"""

email    = "erdem@gmail.com"
password = "yesilcicek" 

enteredEmail    = input("enter e-mail: ")
enteredPassword = input("Enter password: ")

if (email == enteredEmail) and (password == enteredPassword):
    print("login verified")

else:
    print("login couldn't be verified")

"""

# 4- Girilne 3 sayıyı büyüklük olarak karşılaştırınız

"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a > b) and (a > c):
    print("a is the largest number")

elif (b > a) and (b > c):
    print("b is the largest number")

elif (c > a) and (c > b):
    print("c is the largest number")

"""

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#    b-) Finalden 70 alındığında ortalamnın önemi kalmasın

"""

visa1 = float(input("First visa: "))
visa2 = float(input("Second visa: "))
final = float(input("Final: "))

average = (((visa1 + visa2)/2) * 0.6) + (final * 0.4)

result  = (average >= 50) and (final >= 50)
result  = (average >= 50) or (final >= 70)

if (average >= 50):
    if (final >= 50):
        print(f'average: {average} ve passed the lesson?: correct')
        print('correct')
    else:
        print(f'average: {average} ve passed the lesson?: not correct')

else:
    print('not correct')

"""

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input("name: ")
kg   = float(input("weight: "))
hg   = float(input("height: "))

index = (kg) / (hg ** 2)

if (index >= 0) and (index <= 18.4):
    print(f'{name}, weight index: {index} ve weight evaluation thin')

elif (index > 18.4) and (index <= 24.9):
    print(f'{name}, weight index: {index} ve weight evaluation normal')

elif (index > 24.9) and (index <= 29.9):
    print(f'{name}, weight index: {index} ve weight evaluation overweight')

elif (index > 29.9) and (index <= 34.9):
    print(f'{name}, weight index: {index} ve weight evaluation Obesse')

else:
    print("your information is wrong, try again.")

