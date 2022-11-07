"""Комп сам загадывает и отгадывает число"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандом угадайка числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min, max = 1, 100
    
    while True:
        count+=1
        predict_number = (min+max)//2 # преполагаемое число
        if number < predict_number:
            max = predict_number - 1
        elif number > predict_number:
            min = predict_number + 1
        else:
            break # выход из цикла, если угадал
        
    return count


def score_game(random_predict) -> int:
    """Среднее кол-во попыток угадайки за 1000 проходов

    Args:
        random_predict (_type_): функция угадайки

    Returns:
        int: Среднее кол-во попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загад список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == '__main__':
    score_game(random_predict)