import random

def insertion_sort_sub(A, p, r):
    comp_insertion = 0
    for j in range(p + 1, r + 1):
        key = A[j]
        i = j - 1
        
        while i >= p:
            comp_insertion += 1  # Conta a comparação que será feita no if
            if A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            else:
                break
        A[i + 1] = key
        
    return comp_insertion


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


def quicksort_hibrido(A, p, r):
    total_comparacoes = 0
    
    while p < r:
        # Se o tamanho do subvetor atual for menor que k (k = 16)
        if (r - p + 1) < 16:
            total_comparacoes += insertion_sort_sub(A, p, r)
            break
        else:
            # Chama a partição randomizada idêntica à do seu quick puro
            q, comps = partition_random(A, p, r)
            total_comparacoes += comps
            
            # Otimização da pilha de recursão (trata a menor partição primeiro)
            if (q - p) < (r - q):
                total_comparacoes += quicksort_hibrido(A, p, q - 1)
                p = q + 1
            else:
                total_comparacoes += quicksort_hibrido(A, q + 1, r)
                r = q - 1
                
    return total_comparacoes