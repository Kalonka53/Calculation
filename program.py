def get_number(prompt):
    while True:
        try:
            n = float(input(prompt))
            return n
        except ValueError:
            print('Неправильный выбор. напиши число: ')
def operation():
    op = input('Выберите операцию (+, -, *, /): ')
    if op in ['+', '-', '*', '/',]:
        return op
    print('Неправильный выбор. Выберите (+, -, *, /): ')
def calculation(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        if num1 == 0:
            print(f'На {num1}, делить нельзя')
        return num1 / num2
def main():
    while True:
        print('Простой числовой калькулятор')
        num1 = get_number('Введите первое число: ')
        op = operation()
        num2 = get_number('Введите второе число: ')
        section = calculation(num1, op, num2)
        print(f'Результат: {int(section)}')
        choise = input('Хотите произвести расчёт, ещё раз ? (да/нет?): ')
        if choise != 'да':
            print('Досвидания')
            break

if __name__ == "__main__":
    main()