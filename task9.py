number1 = int(input('Первое число: '))
number2 = int(input('Второе число '))
znak = input("Что нужно сделать - /, *, +, -, %" )

def value ():
    try:
        if znak == '/':
            print(number1 / number2)
        elif znak == '*':
            print(number1 * number2)
        elif znak == '+':
            print(number1 + number2)
        elif znak == '-':
            print(number1 - number2)
        elif znak == '%':
            print(number2 * 100 / number1)
        else:
            pass
    except ZeroDivisionError:
        print('На ноль делить нельзя')
value()
    



