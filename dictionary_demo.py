"""

Student = {
    '941': {
        'name': 'Erdem',
        'surname': 'Yeşilçiçek',
        'Phone': '541 397 1338',
    },
    '150': {
        'name': 'Osman',
        'surname': 'Yıldız',
        'Phone': '541 555 55 55',
    },
    '1031': {
        'name': 'Buğra',
        'surname': 'Arslan',
        'Phone': '541 444 44 44',
    },
}
print(Student['941'])

"""

# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız

# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

students ={}
number  = input("Student no: ")
name    = input("Student name: ")
surname = input("Student surname: ")
phone   = input("Student phone: ")

# students[number] = {
#     'name'    : name,
#     'surname' : surname,
#     'phone'   : phone,
# },

students.update({
    number: {
        'name': name,
        'surname' : surname,
        'phone'   : phone,
    }
}),

number  = input("Student no: ")
name    = input("Student name: ")
surname = input("Student surname: ")
phone   = input("Student phone: ")

students.update({
    number: {
        'name': name,
        'surname' : surname,
        'phone'   : phone,
    }
}),

number  = input("Student no: ")
name    = input("Student name: ")
surname = input("Student surname: ")
phone   = input("Student phone: ")

students.update({
    number: {
        'name': name,
        'surname' : surname,
        'phone'   : phone,
    }
})


print('*'*40)

studentsNo = input('Student No: ')
student = students[studentsNo]


print(f"Aradığınız {studentsNo} nolu öğrencinin adı: {student['name']} soyadı: {student['surname']} ve telefonu ise {student['phone']}")

