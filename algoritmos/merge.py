def merge_sort(A, p, r):
    comparacoes_totais = 0
    if p < r:
        q = (p + r) // 2
        comparacoes_totais += merge_sort(A, p, q)
        comparacoes_totais += merge_sort(A, q + 1, r)
        comparacoes_totais += merge(A, p, q, r)
    return comparacoes_totais
        
def merge(A, p, q, r):
    comparacoes_intercalacao = 0
    n1 = q-p + 1
    n2 = r - q
    
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    
    for i in range(n1):
        L[i] = A[p + i]
         
    for j in range(n2):
        R[j] = A[q + 1 + j]
    
    L[n1] = float('inf')
    R[n2] = float('inf')
    
    i = j= 0   
    
    comparacoes_intercalacao = 0
    for k in range(p, r + 1):
        comparacoes_intercalacao +=1
        
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1  
        else:
            A[k] = R[j]
            j += 1
    return comparacoes_intercalacao