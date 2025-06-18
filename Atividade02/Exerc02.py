def numeros_primos(lista):
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return [num for num in lista if eh_primo(num)]

# Testando a função com diferentes conjuntos de dados
teste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
teste2 = [11, 13, 15, 17, 19]
teste3 = [20, 21, 22, 23, 24, 25]
teste4 = [2, 3, 5, 7, 11, 13, 17, 19]
teste5 = [4, 6, 8, 9, 10, 12, 14, 15]

print("Teste 1:", numeros_primos(teste1))  # Deve retornar [2, 3, 5, 7]
print("Teste 2:", numeros_primos(teste2))  # Deve retornar [11, 13, 17, 19]
print("Teste 3:", numeros_primos(teste3))  # Deve retornar [23]
print("Teste 4:", numeros_primos(teste4))  # Deve retornar [2, 3, 5, 7, 11, 13, 17, 19]
print("Teste 5:", numeros_primos(teste5))  # Deve retornar []
