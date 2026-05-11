# interface_testes.py

import tkinter as tk
from tkinter import ttk, messagebox
import time
import copy
import matplotlib.pyplot as plt

from algoritmos.quick import quicksort_inplace
from algoritmos.heap import heap_sort

# =========================
# IMPORTAÇÃO DOS VETORES
# =========================

from vectors.vector_100 import (
    vector_crescente as vc_100,
    vector_decrescente as vd_100,
    vector_aleatorio as va_100
)

from vectors.vector_1000 import (
    vector_crescente as vc_1000,
    vector_decrescente as vd_1000,
    vector_aleatorio as va_1000
)

from vectors.vector_5000 import (
    vector_crescente as vc_5000,
    vector_decrescente as vd_5000,
    vector_aleatorio as va_5000
)

from vectors.vector_30000 import (
    vector_crescente as vc_30000,
    vector_decrescente as vd_30000,
    vector_aleatorio as va_30000
)

from vectors.vector_50000 import (
    vector_crescente as vc_50000,
    vector_decrescente as vd_50000,
    vector_aleatorio as va_50000
)

from vectors.vector_100000 import (
    vector_crescente as vc_100000,
    vector_decrescente as vd_100000,
    vector_aleatorio as va_100000
)

from vectors.vector_150000 import (
    vector_crescente as vc_150000,
    vector_decrescente as vd_150000,
    vector_aleatorio as va_150000
)

from vectors.vector_200000 import (
    vector_crescente as vc_200000,
    vector_decrescente as vd_200000,
    vector_aleatorio as va_200000
)

# =========================
# DICIONÁRIO DOS VETORES
# =========================

vetores = {
    100: {
        "crescente": vc_100,
        "decrescente": vd_100,
        "aleatorio": va_100
    },

    1000: {
        "crescente": vc_1000,
        "decrescente": vd_1000,
        "aleatorio": va_1000
    },

    5000: {
        "crescente": vc_5000,
        "decrescente": vd_5000,
        "aleatorio": va_5000
    },

    30000: {
        "crescente": vc_30000,
        "decrescente": vd_30000,
        "aleatorio": va_30000
    },

    50000: {
        "crescente": vc_50000,
        "decrescente": vd_50000,
        "aleatorio": va_50000
    },

    100000: {
        "crescente": vc_100000,
        "decrescente": vd_100000,
        "aleatorio": va_100000
    },

    150000: {
        "crescente": vc_150000,
        "decrescente": vd_150000,
        "aleatorio": va_150000
    },

    200000: {
        "crescente": vc_200000,
        "decrescente": vd_200000,
        "aleatorio": va_200000
    }
}

# =========================
# FUNÇÃO DE TEMPO
# =========================

def medir_tempo(funcao, vetor):

    vetor_teste = copy.deepcopy(vetor)

    inicio = time.perf_counter()

    funcao(vetor_teste)

    fim = time.perf_counter()

    return fim - inicio

# =========================
# GERAR GRÁFICO
# =========================

def gerar_grafico(nomes, tempos):

    plt.figure(figsize=(8, 5))

    plt.bar(nomes, tempos)

    plt.xlabel("Algoritmos")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de Desempenho")

    for i, tempo in enumerate(tempos):

        plt.text(
            i,
            tempo,
            f"{tempo:.6f}s",
            ha='center',
            va='bottom'
        )

    plt.show()

# =========================
# EXECUTAR TESTE
# =========================

def executar_teste():

    try:

        tamanho = int(combo_tamanho.get())
        tipo = combo_tipo.get().lower()
        algoritmo = combo_algoritmo.get()

        vetor = vetores[tamanho][tipo]

        resultado_text.delete(1.0, tk.END)

        resultado_text.insert(tk.END, "========== RESULTADO ==========\n\n")
        resultado_text.insert(tk.END, f"Tamanho: {tamanho}\n")
        resultado_text.insert(tk.END, f"Entrada: {tipo}\n\n")

        nomes = []
        tempos = []

        # QUICK SORT
        if algoritmo == "Quick Sort":

            tempo = medir_tempo(quicksort_inplace, vetor)

            nomes.append("Quick Sort")
            tempos.append(tempo)

            resultado_text.insert(
                tk.END,
                f"Quick Sort: {tempo:.6f} segundos\n"
            )

        # HEAP SORT
        elif algoritmo == "Heap Sort":

            tempo = medir_tempo(heap_sort, vetor)

            nomes.append("Heap Sort")
            tempos.append(tempo)

            resultado_text.insert(
                tk.END,
                f"Heap Sort: {tempo:.6f} segundos\n"
            )

        # COMPARAÇÃO
        elif algoritmo == "Comparar Ambos":

            tempo_quick = medir_tempo(quicksort_inplace, vetor)
            tempo_heap = medir_tempo(heap_sort, vetor)

            nomes.extend(["Quick Sort", "Heap Sort"])
            tempos.extend([tempo_quick, tempo_heap])

            resultado_text.insert(
                tk.END,
                f"Quick Sort: {tempo_quick:.6f} segundos\n"
            )

            resultado_text.insert(
                tk.END,
                f"Heap Sort: {tempo_heap:.6f} segundos\n\n"
            )

            if tempo_quick < tempo_heap:

                resultado_text.insert(
                    tk.END,
                    "Quick Sort foi mais rápido.\n"
                )

            else:

                resultado_text.insert(
                    tk.END,
                    "Heap Sort foi mais rápido.\n"
                )

        # GERA O GRÁFICO
        gerar_grafico(nomes, tempos)

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Ocorreu um erro:\n{erro}"
        )

# =========================
# INTERFACE
# =========================

janela = tk.Tk()

janela.title("Comparador de Algoritmos")
janela.geometry("700x500")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Comparador de Algoritmos de Ordenação",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=20)

frame = tk.Frame(janela)
frame.pack(pady=10)

# =========================
# TAMANHO
# =========================

tk.Label(
    frame,
    text="Tamanho do Vetor:"
).grid(row=0, column=0, padx=10, pady=10)

combo_tamanho = ttk.Combobox(
    frame,
    values=[
        100,
        1000,
        5000,
        30000,
        50000,
        100000,
        150000,
        200000
    ],
    state="readonly"
)

combo_tamanho.grid(row=0, column=1)
combo_tamanho.current(0)

# =========================
# TIPO
# =========================

tk.Label(
    frame,
    text="Tipo da Entrada:"
).grid(row=1, column=0, padx=10, pady=10)

combo_tipo = ttk.Combobox(
    frame,
    values=[
        "Crescente",
        "Decrescente",
        "Aleatorio"
    ],
    state="readonly"
)

combo_tipo.grid(row=1, column=1)
combo_tipo.current(0)

# =========================
# ALGORITMO
# =========================

tk.Label(
    frame,
    text="Algoritmo:"
).grid(row=2, column=0, padx=10, pady=10)

combo_algoritmo = ttk.Combobox(
    frame,
    values=[
        "Quick Sort",
        "Heap Sort",
        "Comparar Ambos"
    ],
    state="readonly"
)

combo_algoritmo.grid(row=2, column=1)
combo_algoritmo.current(2)

# =========================
# BOTÃO
# =========================

botao = tk.Button(
    janela,
    text="Executar Teste",
    command=executar_teste,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
)

botao.pack(pady=20)

# =========================
# RESULTADO
# =========================

resultado_text = tk.Text(
    janela,
    width=80,
    height=15,
    font=("Consolas", 11)
)

resultado_text.pack(pady=10)

# =========================
# INICIAR
# =========================

janela.mainloop()