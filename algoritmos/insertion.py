# 2.1 Ordenação por Inserção

def insertion_sort(arr):
    comparacoes = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparacoes += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparacoes