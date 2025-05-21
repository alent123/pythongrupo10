class Node:
    # Clase que representa un nodo del árbol de expresiones
    def __init__(self, value):
        self.value = value      # Valor del nodo: puede ser operador o número
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho

def inorder_traversal(root):
    # Recorrido inorden: izquierda, raíz, derecha
    if root is None:
        return []               # Si el nodo está vacío, se devuelve una lista vacía
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)
    # Llamadas recursivas a izquierda, nodo, y derecha (en ese orden)

def preorder_traversal(root):
    # Recorrido preorden: raíz, izquierda, derecha
    if root is None:
        return []               # Caso base: nodo vacío
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)
    # Primero el nodo, luego izquierda, luego derecha

def postorder_traversal(root):
    # Recorrido postorden: izquierda, derecha, raíz
    if root is None:
        return []               # Caso base: nodo vacío
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]
    # Primero izquierda, luego derecha, y luego el nodo

# Creamos un árbol de expresión simple:
#       +
#      / \
#     2   3
tree1 = Node('+')               # Nodo raíz con el operador '+'
tree1.left = Node('2')          # Nodo izquierdo con valor '2'
tree1.right = Node('3')         # Nodo derecho con valor '3'

print(inorder_traversal(tree1))     # ['2', '+', '3'] -> izquierda, raíz, derecha
print(preorder_traversal(tree1))    # ['+', '2', '3'] -> raíz, izquierda, derecha
print(postorder_traversal(tree1))   # ['2', '3', '+'] -> izquierda, derecha, raíz

# Creamos un árbol más complejo:
#         +
#        / \
#       *   5
#      / \
#     2   3
tree2 = Node('+')               # Nodo raíz con '+'
tree2.left = Node('*')          # Hijo izquierdo con '*'
tree2.left.left = Node('2')     # Hijo izquierdo de '*' con '2'
tree2.left.right = Node('3')    # Hijo derecho de '*' con '3'
tree2.right = Node('5')         # Hijo derecho del '+' con '5'

print(inorder_traversal(tree2))     # ['2', '*', '3', '+', '5']
print(preorder_traversal(tree2))    # ['+', '*', '2', '3', '5']
print(postorder_traversal(tree2))   # ['2', '3', '*', '5', '+']

