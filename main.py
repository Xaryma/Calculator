try:
    a = int(input('Введи число: '))
    b = int(input('Введи число: '))
    print('А теперь выбери действие: *, /, +, -')
    operator = input()
    if operator == "+":
        print(a + b)
    if operator == "-":
        print(a - b)
    if operator == "*":
        print(a * b)
    if operator == "/":
        if b != 0:
            print(a / b)
        else:
            print('Невозможно вычеслить')
except:
    print('Не число!')
