import asyncio
import random
import time

async def summ_t(my_list):
    return sum(my_list)

async def main():
    my_list = [random.randint(1, 101) for _ in range(1000001)]
    time_start = time.time()
    result = await summ_t(my_list)
    end_time = time.time() - time_start

    print(f'Код выполнен за {end_time:.4f} секунд')
    print(f'Сумма элементов массива: {result}')

asyncio.run(main())# запускаем ансихронную команду.
