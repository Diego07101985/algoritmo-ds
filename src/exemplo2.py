#
from bisect import bisect_left

class Binary: #O(log(n))
     def search(self, vetor,valor):
         
        indice = round(len(vetor)/2)
        
        if vetor[indice] == valor:
            return indice
        
        if valor > vetor[indice]:
            return self.get_position(vetor[indice:], valor)
        return self.get_position(vetor[:indice], valor)
    
     def search_bisect(self, vetor, valor):
         
        indice = bisect_left(vetor,valor)
        
        if indice!=len(vetor) and vetor[indice]==valor:
            return indice
     

if __name__ == "__main__":
    example1 = Binary()
    
    vetor = [2, 5, 10, 11, 15, 20]
    print(example1.search(vetor,11))
    print(example1.search_bisect(vetor,11))
