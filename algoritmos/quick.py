# Ordenação por Quicksort

def partition(A, p, r):
    comparacoes_particao = 0
    """Particiona o array A[p..r] usando o último elemento como pivô."""
    x = A[r]
    i = p - 1
    for j in range(p, r):
        comparacoes_particao += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1, comparacoes_particao


def quick_sort(A, p, r):
    """Ordena o array A[p..r] usando quicksort."""
    total_comps = 0
    if p < r:
        q, comps = partition(A, p, r)
        total_comps += comps
        
        # Acumula as comparações das chamadas recursivas
        total_comps += quick_sort(A, p, q - 1)
        total_comps += quick_sort(A, q + 1, r)
        
    return total_comps



def quicksort_inplace(A):
    """Ordena o array A completamente usando quicksort."""
    if A:
        quick_sort(A, 0, len(A) - 1)
    return A
