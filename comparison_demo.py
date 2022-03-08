# 1- Girilen iki sayıdan hangisi büyüktür?

# a = int(input("First number (a): "))
# b = int(input("Second number (b): "))
# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırınız

# v1 = float(input("First visa: "))
# v2 = float(input("Second visa: "))
# f1 = float(input("Final: "))
# average = (((v1 + v2) / 2) * 0.6) + (f1 * 0.4)
# print(f"not ortalamanız : {average} ve dersten geçme durumunuz: {average>=50}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# number = int(input("number: "))
# fonk = (number % 2 == 0)
# print(f"girilen sayının çift olma durumu: {fonk}")

# 4- Girilen sayının negatif-pozitif durumunu yazdırın.

# number = int(input("number: "))
# isPositive = (number > 0)
# print(f'girilen sayının pozitif olma durumu: {isPositive}')

# 5- Parola ve e-mail bilgisini isteyip doğruluğunu kontrol ediniz.
#    (e-mail: email@erdmyslcck.com parola:148369)

email    = "email@erdem.com"
password = "erdm999"
a = (input("Enter e-mail: "))
b = (input("Enter Password: "))
isMail     = (email == a)
isPassword = (password == b)
print(f'Email bilgisi doğru mu: {isMail} ve parola doğru mu: {isPassword}')

