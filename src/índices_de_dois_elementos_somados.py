# Dado um vetor desordenado de inteiros, retorne os índices de dois elementos que, somados,
# resultam no valor alvo fornecido. Assuma que cada entrada tem uma e apenas uma solução e que
# não é permitido utilizar o mesmo elemento do vetor mais de uma vez.
# Pode retornar os índices em qualquer ordem.
# Exemplo:
# Vetor: 2, 7, 11, 15, alvo: 9
# Resultado: 0, 1 (ou 1, 0)
# Explicação: os elementos zero e um(2 e 7) são os únicos cuja soma é 9 (o valor alvo).
# Você pode criar uma implementação que tenha complexidade de tempo menor que O(n2)?


class Solution: #O(N)
     def get_indices(self, vetor, target):
        dict_values = dict(zip(vetor,[x for x in range(len(vetor))]))
        for _i, _v in enumerate(vetor):
            complemento = target -_v
            if complemento in dict_values and complemento != _v:
                return [_i, dict_values[complemento]]

        return "Dont have elements with that condition"

if __name__ == "__main__":
    example1 = Solution()
    print(example1.get_indices([2, 5, 15, 11, 7, 4], 19))
    print(example1.get_indices([2, 7, 11, 15], 9))
    print(example1.get_indices([3, 2, 4], 6))
