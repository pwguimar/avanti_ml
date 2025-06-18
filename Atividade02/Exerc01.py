def numeros_impares(lista):
    return [num for num in lista if num % 2 != 0]

# Testando a função com diferentes conjuntos de dados
teste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
teste2 = [2, 4, 6, 8, 10]
teste3 = [1, 3, 5, 7, 9]
teste4 = [0, 1, 2, 3, 4, 5]

print("Teste 1:", numeros_impares(teste1))  # Deve retornar [1, 3, 5, 7, 9]
print("Teste 2:", numeros_impares(teste2))  # Deve retornar []
print("Teste 3:", numeros_impares(teste3))  # Deve retornar [1, 3, 5, 7, 9]
print("Teste 4:", numeros_impares(teste4))  # Deve retornar [1, 3, 5]

