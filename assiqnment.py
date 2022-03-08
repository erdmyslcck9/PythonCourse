# x = 5
# y = 9
# z = 20

x, y, z = 5, 9, 20

# x, y = y, x
# x += 5      # x = x + 5
# x -= 5      # x = x - 5
# x *= 5      # x = x * 5
# x /= 5      # x = x / 5
# x //= 5      # x = x // 5
# x **= 5      # x = x ** 5

# print(x, y, z)

values = 1, 2, 3, 4, 9

print(values)
print(type(values))

x, y, *z = values

print(x, y, z)

# başına yıldız ekledik geriye kalan elemanların hepsi z'ye gitti

