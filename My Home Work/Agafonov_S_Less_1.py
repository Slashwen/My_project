# Калькулятор
# Возможные операции калькулятора +, -, /, *
number_1 = input("Введите первое число: ")
if number_1.isdigit():
    number_1 = int(number_1)
    print(number_1)
else:
    print("Ошибка!")
    exit(0)
number_2 = input("Введите второе число: ")
if number_2.isdigit():
    number_2 = int(number_2)
    print(number_2)
else:
    print("Ошибка!")
    exit(0)
operation = input("Введите значение операции: ")
if operation != "+" and operation != "-" and operation != "+" \
        and operation != "*" and operation != "/":
    print("Ошибка!")
    exit(0)
if operation == "+":
    print("Результат: ", number_1 + number_2)
if operation == "-":
    print("Результат: ", number_1 - number_2)
if operation == "*":
    print("Результат: ", number_1 * number_2)
if operation == "/" and number_2 == 0:
    print("Деление на ноль!!!")
    exit(0)
if operation == "/" and number_2 != 0:
    print("Результат: ", number_1 / number_2)
