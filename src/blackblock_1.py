# Entrada: 3,1,4,6,2,5
# Saida: 5,2,7,14,3,10

# 1 2 3 4  5    6
# 2 3 5 7 10   14

# 1 1 2 3 5 8

import numpy as np


class BlackBlock:  # O(N)

    def fibo(self, n):
        if n==0:
            return 0
        
        if n==1:
            return 1
        prev = 0 
        actual = 1
        fib_num = 0
        for _ in range(1, n):
            fib_num = prev + actual
            prev = actual
            actual = fib_num
            
        return fib_num

    def mask(self, vetor):
        fibonacci_serie = []
        for i, value in enumerate(vetor):
            fibonacci_serie.append(value + self.fibo(vetor[i]))
        return fibonacci_serie


class Fibonacci:  # O(N)
    def get_results(self, vetor):
        vetor = np.array(vetor)
        vetor_or = np.sort(vetor)
        fibonacci_serie = []
        fibonacci_serie.append(1)
        fibonacci_serie.append(1)
        for x in range(0, 4):
            fibonacci_serie.append(fibonacci_serie[x] + fibonacci_serie[x+1])
        fibonacci_serie = np.array(fibonacci_serie)
        result = vetor_or + fibonacci_serie
        return result


if __name__ == "__main__":
    # example1 = Fibonacci()
    # print(example1.get_results([3, 1, 4, 6, 2, 5]))
    example1 = BlackBlock()
    print(example1.fibo(1))
    print(example1.mask([3, 1, 4, 6, 2, 5]))
