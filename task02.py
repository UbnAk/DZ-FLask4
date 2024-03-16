
# многопроцессорность и асинхронность.

import random
import time
import multiprocessing

my_list = [random.randint(1,101) for _ in range(1,1000001)] #Сгенерировали список общий
COUNT_THREADS = 5 #Будет брать за основу 5 потоков

sublist = [my_list[i::COUNT_THREADS] for i in range(COUNT_THREADS)]
#Разделил наш список на список из 5 списков

def summ_t(t): #Наша основная функция которая возвращает сумму списка
    return sum(t)

if __name__ == '__main__':
    processes = [] #список для процессов
    result = []

    time_start = time.time()

    for s in sublist:
        proc = multiprocessing.Process(target=summ_t, args=(s,))
        processes.append(proc)
        result.append(sum(s))
        proc.start()

    for p in processes:
        p.join()

    end_time = time.time() - time_start
    result = sum(result)

    print(f'Код выполнен за {end_time:.4f}')
    print(f'Сумма элементов массива: {result}')
    print(sum(my_list))
    print('Все потоки завершили работу')

