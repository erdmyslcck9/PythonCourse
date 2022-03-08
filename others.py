# Identity Operator: is
# Aynı olup olmadıklarını kontrol etmemize yarıyor

# x = y = [1, 2, 3]
# z = [1, 2, 3]
# print(x == y)
# print(x == z)
# print(x is y)
# print(x is z)

# x = [1, 2, 3]
# y = [2, 4]
# del x[2]
# y[1] = 1
# y.reverse()
# print(x == y)
# print(x is y)
# print(x is not y)


# Membership Operator: in
# Elemanın liste içerisinde olup olmaadığını kontrol etmemize yarıyor

x = ['apple', 'banana',]
print('banana' in x)

name = "Erdem"
print("e" in name)
print("ğ" not in name)

