"""Guess Number Game"""

import numpy as np

number = np.random.randint(1, 101) # случайное число

count = 0 # кол-во попыток

while True:
    count+=1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print('Чило должно быть меньше!')
        
    elif predict_number < number:
        print('Чило должно быть больше!')
        
    else:
        print(f'Вы угадали число {number} за {count} попыток!')
        break # выход из бесконечного цикла while