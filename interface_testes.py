import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import matplotlib.pyplot as plt

# Importando os SEUS algoritmos da pasta correta
from algoritmos.bubble import bubble_sort
from algoritmos.insertion import insertion_sort
from algoritmos.merge import merge_sort
from algoritmos.heap import heap_sort
from algoritmos.quick import quick_sort

# =========================
# GERAÇÃO DINÂMICA DE VETORES
# =========================
def gerar_vetor(tamanho, tipo):
    if tipo == "crescente":
        return list(range(tamanho))
    elif tipo == "decrescente":
        return list(range(tamanho, 0, -1))
    else: # Aleatório
        return random.sample(range(tamanho * 2), tamanho)

# =========================
# FUNÇÃO DE EXECUÇÃO
# =========================
def medir_desempenho(algoritmo_nome, vetor):
    vetor_teste = vetor.copy()
    inicio = time.perf_counter()
    
    comparacoes = 0
    if algoritmo_nome == "Bubble Sort":
        comparacoes = bubble_sort(vetor_teste)
    elif algoritmo_nome == "Insertion Sort":
        comparacoes = insertion_sort(vetor_teste)
    elif algoritmo_nome == "Merge Sort":
        comparacoes = merge_sort(vetor_teste, 0, len(vetor_teste) - 1)
    elif algoritmo_nome == "Heap Sort":
        comparacoes = heap_sort(vetor_teste)
    elif algoritmo_nome == "Quick Sort":
        comparacoes = quick_sort(vetor_teste, 0, len(vetor_teste) - 1)
        
    fim = time.perf_counter()
    return (fim - inicio), comparacoes

def gerar_grafico(nomes, tempos):
    plt.figure(figsize=(8, 5))
    plt.bar(nomes, tempos, color='skyblue')
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de Desempenho")
    for i, t in enumerate(tempos):
        plt.text(i, t, f"{t:.4f}s", ha='center', va='bottom')
    plt.show()

def executar_teste():
    try:
        tamanho = int(combo_tamanho.get())
        tipo = combo_tipo.get().lower()
        algoritmo_selecionado = combo_algoritmo.get()

       
        vetor = gerar_vetor(tamanho, tipo)

        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"--- RELATÓRIO DE EXECUÇÃO ---\n")
        resultado_text.insert(tk.END, f"Tamanho: {tamanho} | Tipo: {tipo}\n\n")

        lista_algos = []
        if algoritmo_selecionado == "Comparar Todos":
            lista_algos = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Heap Sort", "Quick Sort"]
        else:
            lista_algos = [algoritmo_selecionado]

        nomes_grafico = []
        tempos_grafico = []

        for algo in lista_algos:
           
            if tamanho > 50000 and algo in ["Bubble Sort", "Insertion Sort"]:
                resultado_text.insert(tk.END, f"{algo}: Pulado (muito lento para este tamanho)\n")
                continue

            tempo, comps = medir_desempenho(algo, vetor)
            nomes_grafico.append(algo)
            tempos_grafico.append(tempo)
            
            resultado_text.insert(tk.END, f"> {algo}:\n")
            resultado_text.insert(tk.END, f"  Tempo: {tempo:.6f}s\n")
            resultado_text.insert(tk.END, f"  Comparações: {int(comps)}\n\n")
        
        if tempos_grafico:
            gerar_grafico(nomes_grafico, tempos_grafico)

    except Exception as e:
        messagebox.showerror("Erro", f"Falha na execução: {e}")

# =========================
# INTERFACE GRÁFICA (Ajustada)
# =========================
janela = tk.Tk()
janela.title("PAA - Ordenação 2026.1")
janela.geometry("600x650")

tk.Label(janela, text="Projeto e Análise de Algoritmos", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(janela)
frame.pack(pady=10)

# Configuração dos campos
tk.Label(frame, text="Tamanho:").grid(row=0, column=0, padx=5)
combo_tamanho = ttk.Combobox(frame, values=[500], state="readonly")
combo_tamanho.grid(row=0, column=1, pady=5)
combo_tamanho.current(0)

tk.Label(frame, text="Entrada:").grid(row=1, column=0, padx=5)
combo_tipo = ttk.Combobox(frame, values=["Aleatorio", "Crescente", "Decrescente"], state="readonly")
combo_tipo.grid(row=1, column=1, pady=5)
combo_tipo.current(0)

tk.Label(frame, text="Algoritmo:").grid(row=2, column=0, padx=5)
combo_algoritmo = ttk.Combobox(frame, values=["Bubble Sort", "Insertion Sort", "Merge Sort", "Heap Sort", "Quick Sort", "Comparar Todos"], state="readonly")
combo_algoritmo.grid(row=2, column=1, pady=5)
combo_algoritmo.current(5)

tk.Button(janela, text="EXECUTAR ORDENAÇÃO", command=executar_teste, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

resultado_text = tk.Text(janela, width=70, height=20, font=("Consolas", 10))
resultado_text.pack(pady=10, padx=10)

janela.mainloop()