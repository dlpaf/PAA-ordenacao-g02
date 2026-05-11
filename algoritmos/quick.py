# Ordenação por Quicksort

def partition(A, p, r):
    """Particiona o array A[p..r] usando o último elemento como pivô."""
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    """Ordena o array A[p..r] usando quicksort."""
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def quicksort_inplace(A):
    """Ordena o array A completamente usando quicksort."""
    if A:
        quicksort(A, 0, len(A) - 1)
    return A
