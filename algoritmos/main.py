import random
import time
import pandas as pd # Sugestão para facilitar a criação de tabelas e gráficos depois
import sys

from bubble import bubble_sort
from heap import heap_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort

sys.setrecursionlimit(210000)


TAMANHOS = [100, 1000, 5000, 30000, 50000, 100000, 150000, 200000]
#TAMANHOS = [1, 10, 50, 300, 50, 100, 150, 200]
CONDICOES = ["Crescente", "Decrescente", "Aleatorio"]

def testar_algoritmo(funcao, vetor):
    comparações = 0
    inicio = time.time()
    # Idealmente, sua função deve retornar o contador de comparações
    # ex: comparacoes = funcao(copia)
    funcao(vetor.copy()) 
    fim = time.time()
    return (fim - inicio), comparações

def main():
    resultados = []

    for tamanho in TAMANHOS:
        print(f"Testando tamanho: {tamanho}...")
        for condicao in CONDICOES:
            # Gerar vetor conforme a condição [cite: 22, 23, 24]
            if condicao == "Crescente": v = list(range(tamanho))
            elif condicao == "Decrescente": v = list(range(tamanho, 0, -1))
            else: v = random.sample(range(tamanho * 2), tamanho)

            algoritmos = [
                ("Bubble Sort", lambda v: bubble_sort(v)),
                ("Insertion Sort", lambda v: insertion_sort(v)),
                ("Merge Sort", lambda v: merge_sort(v, 0, len(v) - 1)),
                ("Heap Sort", lambda v: heap_sort(v)),
                ("Quick Sort", lambda v: quick_sort(v, 0, len(v) - 1))
            ]
          


            for nome, func in algoritmos:
                print(f"    -> Iniciando: {nome} | Condição: {condicao}")
                tempos = []
                comps = []
                for _ in range(3):
                    t, c = testar_algoritmo(func, v)
                    tempos.append(t)
                    comps.append(c)
                print(f"    -> Finalizado: {nome}")
                
                media_tempo = sum(tempos) / 3
                media_comp = sum(comps) / 3
                
                resultados.append({
                    "Algoritmo": nome,
                    "Tamanho": tamanho,
                    "Condição": condicao,
                    "Tempo Médio": media_tempo,
                    "Comparações Médias": media_comp
                })

    # Salvar em CSV facilita muito a criação dos gráficos para o relatório SBC [cite: 59, 60]
    df = pd.DataFrame(resultados)
    df.to_csv("resultados_ordenacao.csv", index=False)
    print("\nTestes concluídos! Resultados salvos em 'resultados_ordenacao.csv'.")

if __name__ == "__main__":
    main()