# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.

"""

print("write all letters lowercase")
name = input("Enter name: ")
age  = int(input("Enter age: "))
education = input("Enter education info: ")

if (age >= 18) and (education == 'high school' or education == 'university'):
    print("you can take driving license")
else: 
    print("you can't take driving licanse")

"""

# 2- Bir öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24   => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

"""

exam1  = int(input("First exam: "))
exam2  = int(input("Second exam: "))
oralexam = int(input("Oral examination: "))

average = (exam1 + exam2 + oralexam) / 3 

if (average >= 0) and (average <= 24):
    print(f"your average: {average}, your grade is equal to 0 ")

elif (average >= 25) and (average <= 44):
    print(f"your average: {average}, your grade is equal to 1 ")

elif (average >= 45) and (average <= 54):
    print(f"your average: {average}, your grade is equal to 2 ")

elif (average >= 55) and (average <= 69):
    print(f"your average: {average}, your grade is equal to 3 ")

elif (average >= 70) and (average <= 84):
    print(f"your average: {average}, your grade is equal to 4 ")

elif (average >= 85) and (average <= 100):
    print(f"your average: {average}, your grade is equal to 5 ")

"""

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl 
#    2. Bakım => 2. yıl 
#    3. Bakım => 3. yıl 
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#    *** datetime modülünü kullanmanız gerekiyor.
#    (şimdi) - (2020/11/1) => gün

# 2 ADET ÇÖZÜM OLUŞTURDUM İLKİ BASİT, İKİNCİSİ DATETİME KULLANILARAK YAPILDI.

# 1. ÇÖZÜM
"""

days = int(input("How many days has your vehicle been in traffic?: "))

if (days <= 365):
    print("First service interval")

elif (days > 365) and (days <= 365*2):
    print("Second service interval")

elif (days > 365*2) and (days <= 365*3):
    print("Third service interval")

else:
    print("Wrong time")

"""

# 2. ÇÖZÜM (TAM ANLAŞILAMAYAN BİR ÇÖZÜM OLDU CEVABA ÇOK GÜVENME)

"""

import datetime

date = input("What date was your vehicle on the road?(2019/8/9): ")
date = date.split('/')
print(date)

# print(date[0])
# print(date[1])
# print(date[2])

traffic = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
now = datetime.datetime.now()
gap = now - traffic
days = gap.days

if (days <= 365):
    print("First service interval")

elif (days > 365) and (days <= 365*2):
    print("Second service interval")

elif (days > 365*2) and (days <= 365*3):
    print("Third service interval")

else:
    print("Wrong time")

"""

