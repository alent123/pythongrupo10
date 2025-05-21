def infix_to_postfix(tokens):
    """Convierte una expresión infija a notación postfija"""
   
    pila = []          # Pila para almacenar operadores
    salida = []        # Lista para la expresión postfija resultante
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}# Definición de precedencia de operadores
    for token in tokens:
        if token.isalnum():# Si el token es un operando (número o variable)
            salida.append(token)
        elif token == '(': # Si es un paréntesis de apertura, se coloca en la pila
            pila.append(token)
        elif token == ')':  # Si es un paréntesis de cierre
            # Sacamos operadores de la pila hasta encontrar el paréntesis de apertura
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar '(' de la pila
        else:  # Si el token es un operador
            # Mientras el operador en la pila tenga mayor o igual precedencia
            while pila and pila[-1] != '(' and precedencia.get(token, 0) <= precedencia.get(pila[-1], 0):
                salida.append(pila.pop())
            pila.append(token)  # Colocamos el operador actual en la pila
    while pila: # Al final, vaciamos los operadores restantes en la pila
        salida.append(pila.pop())
    return salida


# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 📊 Precedence test

# Test 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🔗 Parentheses

# Test 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # 🧮 Complex

# Test 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # 🔤 Variables

