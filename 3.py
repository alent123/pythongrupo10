class Node:
    def __init__(self, value):         # Constructor para inicializar un nodo del árbol
        self.value = value             # Almacena el valor del nodo (operador o número)
        self.left = None               # Referencia al hijo izquierdo
        self.right = None              # Referencia al hijo derecho

def evaluate_expression_tree(root):    # Función para evaluar un árbol de expresiones
    if root is None:                  # Caso base: si el nodo es None, retorna 0
        return 0

    if root.value.isdigit():          # Si el nodo contiene un número (valor terminal)
        return int(root.value)        # Lo convierte a entero y lo devuelve

    # Postorden: evaluar primero los subárboles izquierdo y derecho
    left_val = evaluate_expression_tree(root.left)    # Evaluar recursivamente el hijo izquierdo
    right_val = evaluate_expression_tree(root.right)  # Evaluar recursivamente el hijo derecho

    # Aplicar la operación del nodo actual a los resultados de sus hijos
    if root.value == '+':             # Si el operador es suma
        return left_val + right_val  # Sumar los valores izquierdo y derecho
    elif root.value == '-':           # Si el operador es resta
        return left_val - right_val  # Restar el derecho al izquierdo
    elif root.value == '*':           # Si el operador es multiplicación
        return left_val * right_val  # Multiplicar los valores
    elif root.value == '/':           # Si el operador es división
        return left_val // right_val # Dividir enteramente (sin decimales)
    else:
        raise ValueError(f"Operador desconocido: {root.value}")  # Manejo de error si el operador no es válido

# Test 1
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(evaluate_expression_tree(node1) == 5)

# Test 2
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
print(evaluate_expression_tree(node2) == 20)

# Test 3
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
print(evaluate_expression_tree(node3) == 14)

# Test 4
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
print(evaluate_expression_tree(node4) == 2)

# Test 5
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
print(evaluate_expression_tree(node5) == 15)

