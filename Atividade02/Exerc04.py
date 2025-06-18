def encontrar_segundo_maior(lista_numeros):
    """
    Encontra o segundo maior valor em uma lista de números inteiros.
    
    Args:
        lista_numeros (list): Lista de números inteiros
        
    Returns:
        int: O segundo maior valor da lista
        
    Raises:
        ValueError: Se a lista tiver menos de 2 elementos ou estiver vazia
    """
    if not lista_numeros or len(lista_numeros) < 2:
        raise ValueError("A lista deve conter pelo menos 2 elementos")
    
    # Remove duplicatas e ordena em ordem decrescente
    numeros_unicos = sorted(set(lista_numeros), reverse=True)
    
    return numeros_unicos[1]


def testar_encontrar_segundo_maior():
    """
    Função de teste para verificar o funcionamento correto do algoritmo.
    """
    # Teste 1: Lista com números positivos
    try:
        resultado = encontrar_segundo_maior([10, 5, 8, 12, 3])
        print(f"Teste 1 - Lista [10, 5, 8, 12, 3]: Segundo maior = {resultado}")
        assert resultado == 10
    except Exception as e:
        print(f"Teste 1 falhou: {e}")
    
    # Teste 2: Lista com números negativos
    try:
        resultado = encontrar_segundo_maior([-5, -10, -3, -8, -1])
        print(f"Teste 2 - Lista [-5, -10, -3, -8, -1]: Segundo maior = {resultado}")
        assert resultado == -3
    except Exception as e:
        print(f"Teste 2 falhou: {e}")
    
    # Teste 3: Lista com números repetidos
    try:
        resultado = encontrar_segundo_maior([7, 7, 7, 5, 9, 9, 3])
        print(f"Teste 3 - Lista [7, 7, 7, 5, 9, 9, 3]: Segundo maior = {resultado}")
        assert resultado == 7
    except Exception as e:
        print(f"Teste 3 falhou: {e}")
    
    # Teste 4: Lista com números mistos (positivos e negativos)
    try:
        resultado = encontrar_segundo_maior([-2, 0, 15, -8, 7, -1])
        print(f"Teste 4 - Lista [-2, 0, 15, -8, 7, -1]: Segundo maior = {resultado}")
        assert resultado == 7
    except Exception as e:
        print(f"Teste 4 falhou: {e}")
    
    # Teste 5: Verificar tratamento de erro para lista com menos de 2 elementos
    try:
        resultado = encontrar_segundo_maior([5])
        print("Teste 5 falhou: Deveria ter levantado ValueError")
    except ValueError as e:
        print(f"Teste 5 - Lista com 1 elemento: {e}")
    except Exception as e:
        print(f"Teste 5 falhou com erro inesperado: {e}")
    
    print("\nTodos os testes foram executados!")


# Executar os testes
if __name__ == "__main__":
    testar_encontrar_segundo_maior()
