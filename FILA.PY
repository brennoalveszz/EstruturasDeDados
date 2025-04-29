# Inicializando a pilha como uma lista vazia
topo = None  # O topo da pilha começa como None (vazio)

# Função para verificar se a pilha está vazia
def esta_vazia() -> bool:
    """Verifica se a pilha está vazia."""
    return topo is None  # Se topo for None, a pilha está vazia

# Função para empilhar (adicionar) um item ao topo da pilha
def empilhar(item: any) -> None:
    """Adiciona um novo item ao topo da pilha."""
    global topo  # Usando a variável global topo
    novo_item = [item, topo]  # Cria um novo nó [item, topo_anterior]
    topo = novo_item  # Atualiza o topo para o novo item

# Função para desempilhar (remover) o item do topo da pilha
def desempilhar() -> any:
    """Remove e retorna o item do topo da pilha."""
    global topo  # Usando a variável global topo
    if esta_vazia():  # Verifica se a pilha está vazia antes de tentar remover
        raise Exception("Pilha vazia!")  # Lança uma exceção se a pilha estiver vazia
    item_removido = topo[0]  # O item removido é o que está no topo
    topo = topo[1]  # Atualiza o topo para o próximo item
    return item_removido  # Retorna o item removido

# Função para espiar (ver o item do topo sem remover)
def espiar() -> any:
    """Retorna o item do topo da pilha sem removê-lo."""
    if esta_vazia():  # Verifica se a pilha está vazia
        raise Exception("Pilha vazia!")  # Lança uma exceção se a pilha estiver vazia
    return topo[0]  # Retorna o item do topo sem removê-lo

# Função para retornar o tamanho da pilha
def tamanho() -> int:
    """Retorna o número de itens na pilha."""
    atual = topo  # Começa a contagem a partir do topo
    contador = 0  # Contador para o número de itens
    while atual:  # Percorre a pilha enquanto houver itens
        contador += 1  # Incrementa o contador
        atual = atual[1]  # Vai para o próximo item (referência ao próximo item)
    return contador  # Retorna o número total de itens

# Função para imprimir a pilha (do topo para a base)
def imprime_pilha() -> None:
    """Imprime os itens da pilha do topo para a base."""
    atual = topo  # Começa a impressão do topo
    elementos = []  # Lista para armazenar os itens a serem impressos
    while atual:  # Percorre a pilha até o fim
        elementos.append(str(atual[0]))  # Adiciona o item atual à lista de elementos
        atual = atual[1]  # Vai para o próximo item
    print("Topo -> " + " -> ".join(elementos) + " -> Base")  # Imprime a pilha do topo à base
