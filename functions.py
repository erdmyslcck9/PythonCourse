"""

def sayHello(name = 'user'):
    return 'Hello ' + name

msg = sayHello("Erdem")

print(msg)

"""


"""

num1 = int(input("num1: "))
num2 = int(input("num2: "))


def total(num1, num2):
    return num1 + num2

result = total(num1, num2)
print(result)

"""




birthDay = int(input("What's your birthday?: "))
name     = input("What's your name?: ")

def age(birthDay):
    return 2021 - birthDay

result = age(birthDay)

print(result)




def retiredHowMuch(birthDay, name):
    age1 = age(birthDay)
    retired = 65 - age1

    if retired > 0:
        print(f'{name}, Emekliliğine {retired} yıl kaldı')

    else:
        print(f'{name}, emeklisin')

retiredHowMuch(birthDay, name)

