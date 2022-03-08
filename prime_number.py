"""

Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

"""

num = int(input("What's your number?: "))
isPrime = True

if num == 1:
    print("1 isn't a prime number.")

for i in range(2,num):
    if (num % i == 0):
        isPrime = False
        break
    
if isPrime:
    print(f"{num} is a prime number")

else:
    print(f"{num} isn't a prime number")

