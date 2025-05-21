# Challenge 2: Build Expression Tree from Postfix

class Node:
    """Clase que representa un nodo en el árbol de expresiones"""
    def __init__(self, value):
        self.value = value  # Valor del nodo (operador u operando)
        self.left = None     # Hijo izquierdo
        self.right = None    # Hijo derecho
def build_expression_tree(postfix):
    """Construye un árbol de expresiones desde notación postfix"""
    stack = []  # Pila para nodos temporales
    for token in postfix:
        if token in '+-*/':  # Si es un operador
            right = stack.pop()  # Extrae el operando derecho
            left = stack.pop()   # Extrae el operando izquierdo
            node = Node(token)   # Crea un nodo operador
            node.left = left     # Asigna hijo izquierdo
            node.right = right   # Asigna hijo derecho
            stack.append(node)   # Coloca el nodo de vuelta en la pila
        else:
            stack.append(Node(token))  # Si es un operando, crea nodo hoja
    return stack[0] if stack else None  # El último nodo es la raíz





# ✅ Test cases
tokens1 = ['2', '3', '+']
tree1 = build_expression_tree(tokens1)
print(tree1.value == '+' and tree1.left.value == '2' and tree1.right.value == '3')

tokens2 = ['2', '3', '4', '*', '+']
tree2 = build_expression_tree(tokens2)
print(tree2.value == '+' and tree2.left.value == '2' and tree2.right.value == '*')

tokens3 = ['1', '2', '+', '3', '4', '-', '*']
tree3 = build_expression_tree(tokens3)
print(tree3.value == '*' and tree3.left.value == '+' and tree3.right.value == '-')

tokens4 = ['a', 'b', 'c', '*', '+']
tree4 = build_expression_tree(tokens4)
print(tree4.value == '+' and tree4.left.value == 'a' and tree4.right.value == '*')

tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
tree5 = build_expression_tree(tokens5)
print(tree5.value == '/' and tree5.left.value == '+' and tree5.right.value == '-')
