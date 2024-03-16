# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
import random
import time
import threading

my_list = [random.randint(1,101) for _ in range(1,1000001)] #Сгенерировали список общий
COUNT_THREADS = 5 #Будет брать за основу 5 потоков

sublist = [my_list[i::COUNT_THREADS] for i in range(COUNT_THREADS)]
#Разделил наш список на список из 5 списков

def summ_t(t): #Наша основная функция которая возвращает сумму списка
    return sum(t)

result = []# список куда мы будем складывать суммы 5 списков
threads = []# список для потоков

time_start = time.time()

for s in sublist:
    tr = threading.Thread(target=summ_t, args=(s,))
    threads.append(tr)
    result.append(sum(s))
    tr.start()

for th in threads:
    th.join()

end_time = time.time() - time_start
result = sum(result)

print(f'Код выполнен за {end_time:.4f}')
print(f'Сумма элементов массива: {result}')
print(sum(my_list))
print('Все потоки завершили работу')




