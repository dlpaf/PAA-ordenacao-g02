import random

def partition(A, p, r):
    comparacoes_particao = 0
    x = A[r]
    i = p - 1
    for j in range(p, r):
        comparacoes_particao += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1, comparacoes_particao

def partition_random(A, p, r):
    # Escolhe um índice aleatório e troca com o último para usar como pivô
    idx_aleatorio = random.randint(p, r)
    A[r], A[idx_aleatorio] = A[idx_aleatorio], A[r] 
    return partition(A, p, r) 

def quick_sort(A, p, r):
    total_comps = 0
    if p < r:
        # MUDANÇA AQUI: Chame partition_random em vez de partition
        q, comps = partition_random(A, p, r)
        total_comps += comps
        
        total_comps += quick_sort(A, p, q - 1)
        total_comps += quick_sort(A, q + 1, r)
        
    return total_comps