# 2.1 Ordenação por Inserção

def insertion_sort(arr):
    comparacoes = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break # Sai quando a condição x < V[j] falha
        arr[j + 1] = key
    return comparacoes