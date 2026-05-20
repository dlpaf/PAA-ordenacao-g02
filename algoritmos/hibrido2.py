import random

# O Cormen sugere valores pequenos entre 10 e 20 para sistemas reais.
# Faremos o teste com 16 para poupar o Python.
THRESHOLD = 16

def insertion_sort_global(A):
    """
    Insertion Sort clássico do Cormen (Capítulo 2) aplicado ao vetor inteiro.
    Como o vetor já está 'quase ordenado' pelo Quick Sort truncado,
    esta função roda de forma ultra rápida (próxima a O(N)).
    """
    comparacoes = 0
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0:
            comparacoes += 1
            if A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            else:
                break
        A[i + 1] = key
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
    Quick Sort baseado no Cormen, mas com o critério de parada precoce:
    Se o tamanho do bloco for menor que THRESHOLD, ele não gasta tempo dividindo.
    """
    total_comps = 0
    if p < r:
        # Se o subvetor atual for menor que o limite, interrompe a recursão imediatamente
        if (r - p + 1) < THRESHOLD:
            return 0
            
        q, comps = partition_random(A, p, r)
        total_comps += comps
        
        total_comps += quick_sort_truncated(A, p, q - 1)
        total_comps += quick_sort_truncated(A, q + 1, r)
        
    return total_comps

def hybrid_quick_sort(A, p, r):
    """
    Função principal que cumpre a proposta acadêmica inteligente.
    """
    # Passo 1: O Quick Sort organiza apenas os 'grandes blocos' e ignora os menores
    total_comparacoes = quick_sort_truncated(A, p, r)
    
    # Passo 2: Uma única passada linear resolve todas as pendências locais eficientemente
    total_comparacoes += insertion_sort_global(A)
    
    return total_comparacoes