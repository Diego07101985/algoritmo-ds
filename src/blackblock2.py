# Dada uma entrada (vetor de inteiros) implemente um algoritmo que produza a saída (um vetor de
# vetor de inteiros).
# Entrada: 126,15,28,17
# Saída: [[2, 3, 3, 7], [3, 5], [2, 2, 7], [17]]
# • Há uma lógica baseada em algoritmo clássico;
# • Note que é um vetor dentro de um vetor;
# • Veja se consegue entender a lógica da transformação. Cada elemento gerou um vetor; 

#Crivo Eratóstenes
import numpy as np


class BlackBlock:
    
    def _sequencia_primos(self, limite):
        print(limite)
        lista_numeros = [x for x in range(2,limite+1)]
        for x in range(len(lista_numeros)):
            if lista_numeros[x] != 0:
                for y in range(x,len(lista_numeros)):
                    if lista_numeros[x] != lista_numeros[y] and \
                        lista_numeros[y] != 0:
                        print(f" x {lista_numeros[x]}  {lista_numeros[y]} ")
                        if lista_numeros[y]%lista_numeros[x] == 0:
                            print(f" y {lista_numeros[y]}")
                            lista_numeros[y] = 0

        lista = []
        for x in range(len(lista_numeros)):
            if lista_numeros[x]>0:
                lista.append(lista_numeros[x])
        return lista
    
    def fatorar(self, v):
        f = []
        seq = self._sequencia_primos(max(v))
        for numero in v: 
            fatores = []
            i = 0
            while numero > 1:
                if numero % seq[i] == 0:
                    numero = numero / seq[i]
                    fatores.append(seq[i])
                else:
                    i += 1
            f.append(fatores)
        return f

if __name__ == "__main__":
    example1 = BlackBlock()
    print(example1.fatorar([126]))
