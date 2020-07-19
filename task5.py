date_input = int(input('Введите число: '))
month_input = int(input('Введите месяц: '))
year_input = int(input('Введите год: '))



def chek_date (date, month, year):
    if date_input <= 31 and month_input <= 7 and month_input % 2 != 0:
        print("Такая дата существует") #Проверяем первые 7 мес ищем мес. кот. кончаются на 31 день
    elif date_input <= 30 and month_input/1 != 2 and month_input <=7 and month_input % 2 == 0:
        print("Такая дата существует") #первые 7 мес. и ввыод мес. которые конч на 30 исключаем Февраль
    elif date_input <= 29 and month_input == 2 and year_input % 4 == 0 and year_input % 100 != 0 or year_input % 400 == 0:
        print("Такая дата существует, год Висакосный") #Ввыводим февраль високосный
    elif date_input <= 28 and month_input == 2:
        print("Такая дата существует") #Ввыводим февраль обычный год
    elif date_input <= 31 and month_input >= 8 and month_input <= 12 and month_input % 2 == 0:
        print("Такая дата существует")#Проверяем от 8 по 12 мес ищем мес кот кончаются на 31
    elif date_input <= 30 and month_input >= 8 and month_input <= 12 and month_input % 2 != 0:
        print("Такая дата существует")#от 8 по 12 и ввыод мес. которые конч на 30 исключаем 
    else:
        print("ошибка такой даты не существует!")
    return date_input, month_input, year_input
        

print(chek_date('date', 'month', 'year'))
