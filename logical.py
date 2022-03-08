x = 6
hak = 5 
devam = 'e'
result = 5 <= x < 10
print(result)

# and 

#  True, True  => True
#  True, False => False

result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == 'e')
print(result)

# or

# True,  False => True
# True,  True  => True
# False, False => False

result = (x > 0) or (x % 2 == 0)
print(result)

# not

# İstediğimiz cevabın tam tersini verir yani; bu yanlış mı? demektense, bu doğru mu?

result = not(x > 0)

# x, 5-10 arasında olan bir çift sayı mıdır?

result = ((x > 5) and (x < 10)) and (x % 2 == 0)
print(result)