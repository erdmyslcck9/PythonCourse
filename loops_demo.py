"""

1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın

** "random modülü" için "python random" şeklinde arama yapın.

** 100 üzerinden puanlama yapın. her soru 20 puan.

** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
   üzerinden hesaplansın.

"""

import random

num = random.randint(1,10)
health = int(input("How many tries?: "))
tries = health
counter = 0

while tries > 0:
    tries -= 1
    counter += 1
    guess = int(input("What's your guess?: "))

    if num == guess:
        print(f"Congratulations, you know this number and you know {counter} times.")
        print(f"point: {100 - (100/health) * (counter-1)}")
        break

    elif num < guess:
        print("your number bigger than mystery number.")

    elif num > guess:
        print("your number smaller than mystery number.")

    if tries == 0:
        print(f"tries is over. mystery number is {num}")


    # EXCELLENT WORK

