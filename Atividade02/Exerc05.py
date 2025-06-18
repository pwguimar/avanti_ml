from typing import List, Tuple


def ordenar_pessoas_por_nome(pessoas: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Ordena uma lista de tuplas (nome, idade) alfabeticamente pelo *nome*.

    A ordenação é *case-insensitive*, garantindo que nomenclaturas como "ana" e "Ana"
    sejam consideradas equivalentes durante a comparação.

    Args:
        pessoas: Lista contendo tuplas no formato (nome, idade).

    Returns:
        Uma nova lista de tuplas ordenada alfabeticamente pelo nome.
    """
    # Utiliza sorted para manter a imutabilidade da lista original e garante
    # comparação *case-insensitive* convertendo o nome para minúsculas.
    return sorted(pessoas, key=lambda pessoa: pessoa[0].lower())


# -----------------------------------------------------------------------------
# Testes
# -----------------------------------------------------------------------------

def test_ordenar_pessoas_por_nome():
    # Cenário 1: Lista vazia
    assert ordenar_pessoas_por_nome([]) == []

    # Cenário 2: Nomes distintos
    entrada = [("Carlos", 30), ("Ana", 25), ("Bruno", 40)]
    esperado = [("Ana", 25), ("Bruno", 40), ("Carlos", 30)]
    assert ordenar_pessoas_por_nome(entrada) == esperado

    # Cenário 3: Nomes com letras maiúsculas/minúsculas variadas
    entrada = [("ana", 22), ("Bruno", 35), ("carlos", 28), ("Ana", 30)]
    esperado = [("ana", 22), ("Ana", 30), ("Bruno", 35), ("carlos", 28)]
    assert ordenar_pessoas_por_nome(entrada) == esperado

    # Cenário 4: Nomes repetidos (estável e pela ordem original entre repetidos)
    entrada = [("Diana", 27), ("Diana", 32)]
    esperado = [("Diana", 27), ("Diana", 32)]
    assert ordenar_pessoas_por_nome(entrada) == esperado


if __name__ == "__main__":
    try:
        test_ordenar_pessoas_por_nome()
        print("Todos os testes passaram com sucesso!")
    except AssertionError as e:
        print("Algum teste falhou:", e) 