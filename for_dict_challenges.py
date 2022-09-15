# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = dict()
for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1
for name, count in names.items():              
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = [s["first_name"] for s in students]
names_and_count = {name: names.count(name) for name in names}
max_count = max(names_and_count.values())

for name, count in names_and_count.items():
    if count == max_count:
        print(name)
    


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

from collections import Counter

cl = 1
for item in school_students:
    temp = [i['first_name'] for i in item]
    c = Counter(temp)
    print(f'Самое частое имя в классе {cl}: {c.most_common()[0][0]}')
    cl += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Даша': False,
}

for clas in school:
    boys_count = 0
    girl_count = 0
    for student in clas['students']:
        for name in student.values():
            if is_male[name]:
                boys_count += 1
            else:
                girl_count += 1

    print("Класс {}: девочки {}, мальчики {} ".format(clas["class"],
                                                         girl_count,
                                                         boys_count)) 

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

clases = {}
for clas in school:
    clases[clas["class"]] = {"boys_count": 0, "girls_count": 0}
    boys_count = 0
    girl_count = 0
    for student in clas['students']:
        for name in student.values():
            if is_male[name]:
                clases[clas["class"]]["boys_count"] += 1
            else:
                clases[clas["class"]]["girls_count"] += 1
clas_with_max_girl = ''
max_boys = 0
max_girls = 0
clas_with_max_boy = ''
for clas in clases.keys():
    if max_boys < clases[clas]['boys_count']:
        max_boys = clases[clas]['boys_count']
        clas_with_max_boy = clas
    if max_girls < clases[clas]['girls_count']:
        max_girls = clases[clas]['girls_count']
        clas_with_max_girl = clas
print(f"Больше всего мальчиков в классе {clas_with_max_boy}")
print(f"Больше всего девочек в классе {clas_with_max_girl}")



