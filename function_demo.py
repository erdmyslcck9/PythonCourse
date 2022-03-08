# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

"""
def myFunc(word, num):
    print(word * num)    

myFunc('Erdem\n', 9)
myFunc('Ayşe\n\n', 3)
"""

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonları yazdırınız

"""
def createList(*params):
    list =[]
    for param in params:
        list.append(param)

    return list
result = createList('Yüce Erdem Hazretleri', 9, 'White Chocolate Mocha', 8)

print(result)
"""

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def findPrimeNum(num1, num2):
    for num in range(num1, num2+1):
        if num > 1:
            for i in range(2, num):
                if(num % i == 0):
                    break
            else:
                print(num)

        else:
            print("your number is smaller than 1")
        break
findPrimeNum(num1,num2)
"""

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

"""
num3 = int(input("Enter number: "))

def findPerfectDivisors(num3):
    perfectDivisor = []

    for i in range(2, num3):
        if (num3 % i == 0):
            perfectDivisor.append(i)
        else:
            print("Your number is prime")
        break
    return perfectDivisor

result3 = findPerfectDivisors(num3)

print(result3)
"""

