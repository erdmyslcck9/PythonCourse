# RANGE

# for item in range(50,100,20):
#     print(item)
# print(list(range(50,100,20))) # range elemanlarını listeye çevirdi

# ENUMERATE

'''

index = 0
greeting = 'Hello There'

for letter in greeting:
    print(f'index: {index} letter: {letter}')
    index += 1

'''

# greeting = 'Hello'

# for index,letter in enumerate(greeting):
#     print(f'index: {index} letter: {letter}')


# ZİP

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500,600,700]

print(list(zip(list1, list2,list3)))
