fruits = { "orange", "apple", "banana", }

# print(fruits[0]) İNDEKSLENEMEZ

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango", "grape", "apple"])

fruits.remove("mango")
fruits.discard("apple")
fruits.pop()

# Aynı eleman birden fazla kez eklenemez.

print(fruits)

# myList = [1,2,5,4,4,2,1,7,9,9]
# print(set(myList))

# set komutu ile tekrarlanan elemanlar çıkarılır.

