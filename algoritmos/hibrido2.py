comparacoes = 0

def insertion_sort_sub(A, p, r):
    """
    Insertion Sort que ordena apenas o subvetor de p até r (inclusive).
    """
    comp_insertion = 0
    for j in range(p + 1, r + 1):
        key = A[j]
        i = j - 1
        # Move os elementos de A[p..j-1] que são maiores que a key
        # para uma posição à frente da sua posição atual
        while i >= p and A[i] > key:
            comp_insertion += 1
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return comp_insertion

def partition(A, p, r):
    # O partition retorna dois valores: a posição do pivô (q) e as comparações feitas (comp)
    comp_partition = 0
    x = A[r]
    i = p - 1
    for j in range(p, r):
        comp_partition += 1
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1, comp_partition

def quicksort_hibrido(A, p, r):
    total_comparacoes = 0
    
    while p < r:
        if (r - p + 1) < 16:
            # Soma as comparações do Insertion Sort e encerra o laço
            total_comparacoes += insertion_sort_sub(A, p, r)
            break
        else:
            # Recebe o índice do pivô e as comparações feitas no particionamento
            q, comp_p = partition(A, p, r)
            total_comparacoes += comp_p
            
            # Otimização da pilha de recursão somando os retornos das chamadas
            if (q - p) < (r - q):
                total_comparacoes += quicksort_hibrido(A, p, q - 1)  # Soma chamadas recursivas
                p = q + 1
            else:
                total_comparacoes += quicksort_hibrido(A, q + 1, r)  # Soma chamadas recursivas
                r = q - 1
                
    return total_comparacoes  # Retorna o total acumulado para a main