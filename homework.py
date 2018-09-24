#task1
import random


def task1(n, k):
    number = random.randint(1, n)
    while k > 0:
        try:
            answer = int(input('Введите число'))
        except ValueError:
            print('Неправильный ввод')
        else:
            if answer > number:
                print('Меньше')
                k -= 1
            if answer < number:
                print('Больше')
                k -= 1
            if answer == number:
                print('Вы угадали')
                k = 0
    if k == 0 and answer != number:
        print('Попытки закончились')


#task2
def task2(mass):
    mass2 = []
    for el in mass:
        if el not in mass2:
            mass2.append(el)
    return len(mass2)


#task3
def task3(sent):
    return ' '.join(sent.strip().title().split())


#task4
def decor(str1, str2):
    def inner(func):
        print(str1)
        func()
        print(str2)
    return inner
