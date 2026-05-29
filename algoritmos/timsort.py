"""
timsort.py
==========
TimSort implementado em Python puro, no mesmo estilo dos algoritmos da Parte 1.

O TimSort é o algoritmo padrão do Python (usado em sorted() e .sort()).
Esta implementação manual permite contar comparações e comparar de forma
justa com os outros algoritmos — todos rodando em Python puro.

Funcionamento:
  1. Divide o vetor em "runs" (blocos) de tamanho RUN (32 elementos)
  2. Ordena cada run com Insertion Sort (eficiente para sequências pequenas)
  3. Mescla os runs com Merge — igual ao merge da Parte 1

Justificativa do RUN = 32:
  - O TimSort original usa entre 32 e 64
  - Com RUN=32, cada bloco é pequeno o suficiente para o Insertion Sort
    ser eficiente, e grande o suficiente para reduzir o número de merges
"""

RUN = 32


# ─── Insertion Sort parcial (mesmo do hibrido2.py, para os runs) ──────────────
def insertion_sort_run(arr, esq, dir):
    """
    Ordena arr[esq..dir] com Insertion Sort.
    Igual ao insertion_sort original, adaptado para subvetor.
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


# ─── Merge (mesmo do merge.py da Parte 1) ────────────────────────────────────
def merge(A, p, q, r):
    """
    Intercala A[p..q] e A[q+1..r].
    Código idêntico ao merge.py da Parte 1.
    """
    comparacoes_intercalacao = 0
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + 1 + j]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = j = 0

    for k in range(p, r + 1):
        comparacoes_intercalacao += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return comparacoes_intercalacao


# ─── TimSort ──────────────────────────────────────────────────────────────────
def timsort(arr, p, r):
    """
    TimSort: Insertion Sort nos runs + Merge para combinar.

    Interface igual aos outros algoritmos do trabalho:
        timsort(arr, 0, len(arr) - 1)

    Retorna o total de comparações realizadas.
    """
    total_comps = 0
    n = r - p + 1

    if n <= 1:
        return 0

    # ── Passo 1: ordenar cada run com Insertion Sort ──────────────────────────
    i = p
    while i <= r:
        fim_run = min(i + RUN - 1, r)
        total_comps += insertion_sort_run(arr, i, fim_run)
        i += RUN

    # ── Passo 2: mesclar os runs progressivamente ─────────────────────────────
    tamanho = RUN
    while tamanho < n:
        esq = p
        while esq <= r:
            meio = min(esq + tamanho - 1, r)
            dir  = min(esq + 2 * tamanho - 1, r)

            # Só mescla se existir um segundo run
            if meio < dir:
                total_comps += merge(arr, esq, meio, dir)

            esq += 2 * tamanho
        tamanho *= 2

    return total_comps