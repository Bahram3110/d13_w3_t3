number = input()
number1 = int(number[0])
number2 = int(number[1])
number3 = int(number[2])
if len(number) == 3:
    def num_sum (number):
        number_sum = number1 + number2 + number3
        return str(number_sum)
    print("Вы ввели 3 значное число " + number)



print("Сумма 3 значного числа: " + num_sum(number))

    