import random

# Vetor com 100 elementos
TAMANHO = 100

# Vetor em ordem crescente
vector_crescente = list(range(1, TAMANHO + 1))

# Vetor em ordem decrescente
vector_decrescente = list(range(TAMANHO, 0, -1))

# Vetor aleatório
vector_aleatorio = [random.randint(1, 10000) for _ in range(TAMANHO)]
