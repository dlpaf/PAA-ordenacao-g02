def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, heap_size, i):
    comparacoes = 0
    l = left(i)
    r = right(i)
    largest = i

    # Comparação 1: Pai com o filho esquerdo
    if l < heap_size:
        comparacoes += 1 # Contabiliza a comparação de chaves: A[l] > A[i]
        if A[l] > A[i]:
            largest = l
    
    # Comparação 2: O maior atual com o filho direito
    if r < heap_size:
        comparacoes += 1 # Contabiliza a comparação de chaves: A[r] > A[largest]
        if A[r] > A[largest]:
            largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # Acumula comparações da chamada recursiva
        comparacoes += max_heapify(A, heap_size, largest)
        
    return comparacoes

def build_max_heap(A):
    total_comps = 0
    heap_size = len(A)
    # Constrói o heap de baixo para cima
    for i in range((heap_size // 2) - 1, -1, -1):
        total_comps += max_heapify(A, heap_size, i)
    return heap_size, total_comps

def heap_sort(A):
    # Parte I: Construção do Heap
    heap_size, total_comps = build_max_heap(A)
    
    # Parte II: Ordenação propriamente dita
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0] # Troca a raiz (maior) com o último elemento
        heap_size -= 1
        # Restaura a propriedade de heap e soma as comparações
        total_comps += max_heapify(A, heap_size, 0)
        
    return total_comps # Retorna o total para o seu main.py