import random

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
    user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
    cnt += 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        print('Спасибо за игру')
        break
    elif user_num > x:
        print('Мое число меньше')
    else:
        print('Мое число больше')