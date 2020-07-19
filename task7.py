number = int(input())
def numbers (num):
    i = 0
    while num > 0:
        num = num // 10
        i = 1 + i
    return i

print(numbers(number))