from random import randint
N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))


def selection_sort(arr):
    i = 0
    while i < N - 1:
        # ПОИСК МИНИМУМА
        # Сначала надо найти минимальное значение
        # на срезе от i до конца списка.
        # Переменная m будет хранить индекс ячейки
        # с минимальным значением.
        # Сначала предполагаем, что
        # в ячейке i содержится минимальный элемент.
        m = i
        # Поиск начинаем с ячейки следующей за i.
        j = i + 1
        # Пока не дойдем конца списка,
        while j < N:
            # будем сравнивать значение ячейки j,
            # со значением ячейки m.
            if arr[j] < arr[m]:
                # Если в j значение меньше, чем в m,
                # сохраним в m номер найденного
                # на данный момент минимума.
                m = j
            # Перейдем к следующей ячейке.
            j += 1

        # ОБМЕН ЗНАЧЕНИЙ
        # В ячейку i записывается найденный минимум,
        # а значение из ячейки i переносится
        # на старое место минимума.
        arr[i], arr[m] = arr[m], arr[i]

        # ПЕРЕХОД К СЛЕДУЮЩЕЙ НЕОБРАБОТАННОЙ ЯЧЕЙКЕ
        i += 1

print(arr)
selection_sort(arr)
print(arr)