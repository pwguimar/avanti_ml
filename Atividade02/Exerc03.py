def elementos_unicos(lista1, lista2):
    """
    Retorna uma lista com elementos que estão presentes em apenas uma das listas.
    
    Args:
        lista1: Primeira lista de entrada
        lista2: Segunda lista de entrada
        
    Returns:
        Lista contendo elementos únicos
    """
    # Converte as listas para conjuntos
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Usa operação de diferença simétrica para encontrar elementos únicos
    elementos_unicos = list(set1 ^ set2)
    
    return elementos_unicos

# Testes
def test_elementos_unicos():
    # Teste 1: Listas com elementos diferentes
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]
    assert sorted(elementos_unicos(lista1, lista2)) == [1, 2, 5, 6]
    
    # Teste 2: Listas com elementos repetidos
    lista1 = [1, 1, 2, 2, 3]
    lista2 = [2, 2, 3, 4, 4]
    assert sorted(elementos_unicos(lista1, lista2)) == [1, 4]
    
    # Teste 3: Listas vazias
    lista1 = []
    lista2 = []
    assert elementos_unicos(lista1, lista2) == []
    
    # Teste 4: Listas com tipos diferentes
    lista1 = [1, "a", 3.14]
    lista2 = ["a", 2, 3.14]
    assert sorted(elementos_unicos(lista1, lista2)) == [1, 2]

# Executa os testes
if __name__ == "__main__":
    test_elementos_unicos()
    print("Todos os testes passaram!")
