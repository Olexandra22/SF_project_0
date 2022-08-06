import numpy as np

def random_predict(num: int = 1) -> int:
    '''Игра "компьютер угадает число меньше чем за 20 попыток"'''
    
    count = 0
    
    min_value = 1
    
    max_value = 101
    
    while True:
        count += 1

        mid_value = (min_value+max_value) // 2 
        
        if mid_value > num:
            max_value = mid_value
        elif mid_value < num:
            min_value = mid_value
        else:
            break # конец игры, выход из цикла
        
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    
    np.random.seed(1) # фиксируем сид для воcпроизводимости
    
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')

score_game(random_predict) 
    