# 2.2 Ordenação por Bolha

def bubble_sort(arr):
    comparacoes = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            comparacoes += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return  comparacoes
  