from random import randint

# TODO Задание 1
# Дан словарь, создать новый словарь, поменяв местами ключ и значение.


print("Задание 1")
print("Дан словарь, создать новый словарь, поменяв местами ключ и значение")
print("*******************************************************************")

d = {'dict_1': 1, 'dict_2': 2}
print("Значение d", d)
d = dict([(1, 'STOP'), (2, 'PAUSE')])
d[1] = 'FWD'
d[2] = 'END'
d[3] = 'PLAY'
print("Новое значение d", d)
d_new = dict(zip(d.values(), d.keys()))
print("Значение d_new", d_new)
print(type(d_new))

d_new_2 = dict([val, key] for key, val in d.items())
print("Значение d_new_2", d_new_2)
print(type(d_new_2))
print("*******************************************************************")
#
#
# TODO Задание 2
# Написать программу для нахождения факториала. Реализацию выполнить
#   в виде рекурсивной функции.


print("Задание 2")
print("Написать программу для нахождения факториала. Реализацию выполнить "
      "в виде рекурсивной функции")
print("*******************************************************************")

num = input("Введите число: ")
if num.isdigit():
    num = int(num)
    print(num)
else:
    print("Ошибка!")


def fact_n_recursive(num):
    if num == 1:
        return 1
    else:
        return num * fact_n_recursive(num - 1)


print('Значение', num, 'Факториал', fact_n_recursive(num))
print("*******************************************************************")

# TODO Задание 3
# Написать программу для нахождения факториала. Реализацию выполнить
#   в виде рекурсивной функции.


print("Задание 3")
print("Дан список чисел. Подсчитать сколько раз встречается каждое число.  "
      "Использовать словарь. Для нахождения элемента в словаре использовать  "
      " метод get(), либо оператор in ")
print("*******************************************************************")


List_1 = []
for i in range(10):
    List_1.append(randint(0, 10))
print(List_1)
print(type(List_1))

my_list = sorted(List_1)

dublicate = []
for i in my_list:
    if my_list.count(i) > 1:
        if i not in dublicate:
            dublicate.append(i)
print(dublicate)
