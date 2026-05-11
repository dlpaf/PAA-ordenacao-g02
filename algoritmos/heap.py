# Ordenação por Heap Sort

def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, heap_size, i):
    """Mantém a propriedade de max-heap para o nó i."""
    l = left(i)
    r = right(i)
    largest = i

    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)


def build_max_heap(A):
    """Constrói um max heap a partir de um array não ordenado."""
    heap_size = len(A)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(A, heap_size, i)
    return heap_size


def heap_sort(A):
    """Ordena A em ordem crescente usando heap sort."""
    heap_size = build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, heap_size, 0)
    return A
