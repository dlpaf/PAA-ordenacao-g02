def insertion_sort_sub(A, p, r):
    """
    Insertion Sort que ordena apenas o subvetor de p até r (inclusive).
    """
    for j in range(p + 1, r + 1):
        key = A[j]
        i = j - 1
        # Move os elementos de A[p..j-1] que são maiores que a key
        # para uma posição à frente da sua posição atual
        while i >= p and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def partition(A, p, r):
    """
    Particionamento clássico do livro do Cormen (pivô é o último elemento).
    """
    x = A[r]  # Pivô
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort_hibrido(A, p, r):
    """
    Quick Sort Híbrido com Otimização de Recursão de Cauda 
    e corte para Insertion Sort se o tamanho for menor que k (16).
    """
    while p < r:
        # Se o tamanho do subvetor for menor que 16 (k = 16)
        if (r - p + 1) < 16:
            insertion_sort_sub(A, p, r)
            break
        else:
            # Particiona o vetor
            q = partition(A, p, r)
            
            # Otimização da pilha: faz a recursão na MENOR partição primeiro
            # e atualiza os limites do laço while para a MAIOR partição.
            if (q - p) < (r - q):
                quicksort_hibrido(A, p, q - 1) # Menor partição à esquerda
                p = q + 1                      # Transforma a recursão da direita em iteração
            else:
                quicksort_hibrido(A, q + 1, r) # Menor partição à direita
                r = q - 1                      # Transforma a recursão da esquerda em iteração