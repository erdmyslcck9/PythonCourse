"""
Daire Alanı   : pir**2
Daire Çevresi : 2pir

*Yarı çapı verilen bir dairenin alan
ve çevresini hesaplayınız. (r: 3.14)

"""

r = float(input("Enter Radius: "))
pi = 3.14

circlearea = pi * (r**2)
print("Circle Area: ", circlearea)

circumcircle = 2*pi*r
print("Circum Circle: ", circumcircle)