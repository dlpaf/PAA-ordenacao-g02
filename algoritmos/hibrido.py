import random

THRESHOLD = 16

def insertion_sort_global(A):
    """
    Insertion Sort clássico do Cormen aplicado ao vetor inteiro
    depois que o Quick Sort já organizou as grandes partições.
    """
    comparacoes = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if A[j] > key:
                A[j + 1] = A[j]
                j -= 1
            else:
                break
        A[j + 1] = key
    return comparacoes

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
    idx_aleatorio = random.randint(p, r)
    A[r], A[idx_aleatorio] = A[idx_aleatorio], A[r]
    return partition(A, p, r)

def quick_sort_truncated(A, p, r):
    """
    Executa o Quick Sort, mas ignora subvetores menores que o THRESHOLD.
    """
    total_comps = 0
    if p < r:
        # Se a partição atual já for menor que o limite, não subdivide mais
        if (r - p + 1) < THRESHOLD:
            return 0
            
        q, comps = partition_random(A, p, r)
        total_comps += comps
        
        total_comps += quick_sort_truncated(A, p, q - 1)
        total_comps += quick_sort_truncated(A, q + 1, r)
        
    return total_comps

def hybrid_quick_sort3(A, p, r):
    """
    Função principal que cumpre a proposta acadêmica.
    """
    # Passo 1: Quick Sort trunca a árvore de recursão antes do fim
    total_comparacoes = quick_sort_truncated(A, p, r)
    
    # Passo 2: Uma única passada linear resolve todos os pequenos blocos de uma vez
    total_comparacoes += insertion_sort_global(A)
    
    return total_comparacoes