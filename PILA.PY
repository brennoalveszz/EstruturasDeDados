from collections import deque  # Importa a biblioteca deque para trabalhar com pilhas e filas

# Inicializando a pilha como uma deque vazia
pilha = deque()  # Cria uma pilha vazia usando deque

# Função para verificar se a pilha está vazia
def esta_vazia() -> bool:
    """Verifica se a pilha está vazia."""
    return len(pilha) == 0  # Retorna True se a pilha não tiver itens (tamanho 0)

# Função para empilhar (adicionar) um item ao topo da pilha
def empilhar(item: any) -> None:
    """Adiciona um novo item ao topo da pilha."""
    pilha.append(item)  # Adiciona o item no final da deque, que é o topo da pilha

# Função para desempilhar (remover) o item do topo da pilha
def desempilhar() -> any:
    """Remove e retorna o item do topo da pilha."""
    if esta_vazia():  # Verifica se a pilha está vazia antes de tentar remover
        raise Exception("Pilha vazia!")  # Lança uma exceção se a pilha estiver vazia
    return pilha.pop()  # Remove e retorna o item do topo (final da deque)

# Função para espiar (ver o item do topo sem remover)
def espiar() -> any:
    """Retorna o item do topo da pilha sem removê-lo."""
    if esta_vazia():  # Verifica se a pilha está vazia
        raise Exception("Pilha vazia!")  # Lança uma exceção se a pilha estiver vazia
    return pilha[-1]  # Retorna o item do topo sem removê-lo (último item da deque)

# Função para retornar o tamanho da pilha
def tamanho() -> int:
    """Retorna o número de itens na pilha."""
    return len(pilha)  # Retorna o número de itens na pilha (tamanho da deque)

# Função para imprimir a pilha (do topo para a base)
def imprime_pilha() -> None:
    """Imprime os itens da pilha do topo para a base."""
    print("Topo -> " + " -> ".join(map(str, reversed(pilha))) + " -> Base")  
    # Imprime a pilha do topo à base, invertendo a ordem dos itens com reversed
