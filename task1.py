natural_num = input('Введите натурально число: ')
def last_num ():
    if len(natural_num) >= 1:
        return natural_num[len(natural_num)-1]
        
    else:
        print('error')

print(last_num())

# n = "152"
# n = n[1]
# print(n)
