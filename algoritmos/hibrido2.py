import random

# ─── Threshold ────────────────────────────────────────────────────────────────
# Subarranjos com tamanho <= THRESHOLD são ordenados com Insertion Sort.
# Valor 16 é padrão da literatura (IntroSort, pdqsort usam entre 8 e 32).
# Justificativa experimental: para n pequeno, o overhead de chamadas recursivas
# do QuickSort supera o custo O(n²) do Insertion Sort.
THRESHOLD = 16


# ─── Insertion Sort (igual ao da Parte 1, adaptado para subarray) ─────────────
def insertion_sort_parcial(arr, esq, dir):
    """
    Insertion Sort aplicado apenas no intervalo [esq, dir] do vetor.
    Igual à lógica do insertion_sort original, mas com índices de início/fim.
    """
    comparacoes = 0
    for i in range(esq + 1, dir + 1):
        key = arr[i]
        j = i - 1
        while j >= esq:
            comparacoes += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparacoes


# ─── Partição com pivô aleatório (igual ao da Parte 1) ───────────────────────
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


# ─── AOH: QuickSort Híbrido ───────────────────────────────────────────────────
def quicksort_hibrido(A, p, r):
    """
    Algoritmo de Ordenação Híbrido (AOH).

    Estratégia:
      - Se o subarray tem tamanho <= THRESHOLD: usa Insertion Sort
        (mais eficiente para subarranjos pequenos e quase-ordenados)
      - Caso contrário: usa QuickSort com pivô aleatório
        (melhor desempenho médio em vetores grandes)

    Justificativa (baseada nos resultados experimentais da Parte 1):
      - QuickSort foi o mais rápido em vetores aleatórios e decrescentes
        em todos os tamanhos testados.
      - Insertion Sort foi até 23x mais rápido que QuickSort em vetores
        crescentes, pois tem complexidade O(n) nesse cenário.
      - Nos estágios finais da recursão do QuickSort, os subarranjos
        pequenos já estão quase ordenados — cenário ideal para Insertion Sort.
    """
    total_comps = 0

    # Subarray pequeno: delegar ao Insertion Sort
    if r - p + 1 <= THRESHOLD:
        if p < r:
            total_comps += insertion_sort_parcial(A, p, r)
        return total_comps

    # Subarray grande: particionar e recursar
    if p < r:
        q, comps = partition_random(A, p, r)
        total_comps += comps
        total_comps += quicksort_hibrido(A, p, q - 1)
        total_comps += quicksort_hibrido(A, q + 1, r)

    return total_comps