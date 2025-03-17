# EstruturasDeDados
Repositório para estudo de listas encadeadas, listas ordenadas e árvores binárias em Python

Lista Encadeada
Cada nó contém um valor e um ponteiro para o próximo nó.
📌 Como executar : Salvelista_encadeada.pye cavalgou `python lista_encadeada.py.

Python

Copiar código
class Node:
    def __init__(self, data): self.data, self.next = data, None

class LinkedList:
    def __init__(self): self.head = None
    def insert(self, data):
        new_node = Node(data); new_node.next = self.head; self.head = new_node
    def display(self):
        temp = self.head
        while temp: print(temp.data, end=" -> "); temp = temp.next
        print("None")

lista = LinkedList(); lista.insert(10); lista.insert(20); lista.display()
_______________________________________________________________________________

 Lista Ordenada
Mantenha os elementos sempre organizados.
📌Como executar :lista_ordenada.pyepython lista_ordenada.py.

Python

Copiar código
class Node:
    def __init__(self, data): self.data, self.next = data, None

class OrderedList:
    def __init__(self): self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head or self.head.data >= new_node.data:
            new_node.next, self.head = self.head, new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next, current.next = current.next, new_node
    def display(self):
        temp = self.head
        while temp: print(temp.data, end=" -> "); temp = temp.next
        print("None")

lista = OrderedList(); lista.insert(30); lista.insert(10); lista.insert(20); lista.display()
____________________________________________________________________________________________

Árvore Binária
Cada nó tem no máximo dois filhos (esquerda e direita).
📌Como executar : Salve como arvore_binaria.pye rode python arvore_binaria.py.

Python

Copiar código
class Node:
    def __init__(self, data): self.data, self.left, self.right = data, None, None

class BinaryTree:
    def __init__(self): self.root = None
    def insert(self, data):
        if not self.root: self.root = Node(data)
        else: self._insert_recursive(self.root, data)
    def _insert_recursive(self, node, data):
        if data < node.data:
            if not node.left: node.left = Node(data)
            else: self._insert_recursive(node.left, data)
        else:
            if not node.right: node.right = Node(data)
            else: self._insert_recursive(node.right, data)
    def inorder(self, node):
        if node: self.inorder(node.left); print(node.data, end=" "); self.inorder(node.right)

tree = BinaryTree(); tree.insert(30); tree.insert(10); tree.insert(20); tree.inorder(tree.root)
