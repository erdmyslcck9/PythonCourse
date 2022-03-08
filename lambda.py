def square(num): return num ** 2

numbers = [1,3,5,9,11]

result = list(map(square, numbers))

for item in map(square, numbers):
    print(item)


print(result)