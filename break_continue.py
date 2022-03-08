# BREAK döngüyü tamamen kırar

# name = 'Erdem Yeşilçiçek'

# for letter in name:
#     if letter == 'ş':
#         break
#     print(letter) 


# CONTINUE döngünün o aşamasını es geçer

# name = 'Erdem Yeşilçiçek'

# for letter in name:
#     if letter == 'ş':
#         continue
#     print(letter)


# BREAK PRENSİP OLARAK AYNI İLERLİYOR

# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x+=1


# CONTINUE'DAN SONRA ARTTIRIRSAK İŞLEM GERÇEKLEŞMEZ 2'YE TAKILI KALIR
# O YÜZDEN X+=1 İFADESİNİ CONTINUE'DEN ÖNCE KOYARIZ

# x = 0
# while x < 5:
#     x+=1
#     if x == 2:
#         continue
#     print(x)

# 1-100'e kadar olan tek sayıların toplamı nedir?

x = 0
result = 0

while x <= 100:
    x+=1
    if x % 2 == 0:
        continue
    result += x
print(f'toplam: {result}')