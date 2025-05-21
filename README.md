# 🧮 Proyecto: Árboles de Expresiones Matemáticas

## 👥 Integrantes
- BELLIDO CHAMBI, RONY WIDMER
- GARCIA CCENCHO, CRISTIAN RUFINO
- SALAS PEREZ, SANTIAGO AGUSTIN  

## 👨‍🏫 Docente
- Garamendi Sarmiento, Elliot Leo

# Challenge 1: Convert Infix to Postfix

Este código tiene como objetivo construir un árbol de expresión a partir de una expresión en notación postfija (también conocida como notación polaca inversa). El árbol de expresión es una estructura jerárquica que se utiliza para evaluar o manipular expresiones matemáticas.

## Objetivo
El objetivo de este código es procesar una lista de tokens en notación postfija (en la que los operadores siguen a los operandos) y crear un árbol binario que represente la expresión. La raíz del árbol será el operador principal, y sus hijos representarán los operandos.

## Funcionamiento

### Clase Nodo
Se define una clase Nodo que tiene tres atributos: valor (el valor del nodo), izquierda y derecha (referencias a los nodos hijos).

### Función build_expression_tree
- Se utiliza una pila para almacenar temporalmente los nodos.
- A medida que se recorren los tokens, los operandos (números o variables) se almacenan directamente en la pila como nodos.
- Los operadores (+, -, *, /) desencadenan la creación de un nodo operador, tomando los dos nodos previos de la pila (que representan los operandos) y asignándolos como hijos del operador.
- Al final, la pila contendrá un solo nodo: la raíz del árbol de expresión.

## Prueba de los Casos
Se prueban varios casos para asegurar que el árbol se construya correctamente:
- Caso simple de suma (2 + 3).
- Caso con precedencia de operadores (2 + 3 * 4).
- Caso con operaciones anidadas ((1 + 2) * (3 - 4)).
- Caso con variables (a + b * c).

---

# Challenge 2: Build Expression Tree from Postfix

Este código tiene como objetivo convertir una expresión en notación infija (la forma tradicional de escribir expresiones matemáticas, como a + b) a notación postfija (o polaca inversa, como a b +). La notación postfija elimina la necesidad de paréntesis y facilita la evaluación de expresiones utilizando una pila.

## Objetivo
El objetivo es procesar una lista de tokens que representa una expresión infija y devolver una lista de tokens que representa la misma expresión en notación postfija. Este proceso debe respetar la precedencia de los operadores y manejar adecuadamente los paréntesis.

## Funcionamiento

### Pila y Salida
- Se utiliza una pila para almacenar los operadores y paréntesis mientras se procesan los tokens.
- La salida es una lista que almacenará los operandos en el orden correcto para la notación postfija.

### Precedencia de Operadores
Los operadores * y / tienen mayor precedencia que + y -.

### Procesamiento de Tokens
- Los operandos (números y variables) se agregan directamente a la salida.
- Los paréntesis se manejan correctamente:
  - Al encontrar un paréntesis de apertura (, se coloca en la pila.
  - Al encontrar un paréntesis de cierre ), se extraen los operadores de la pila hasta encontrar el paréntesis de apertura correspondiente.
- Los operadores se colocan en la pila, pero primero se sacan los operadores de mayor o igual precedencia.

### Finalización
Una vez procesados todos los tokens, los operadores restantes en la pila se vacían hacia la salida.

## Prueba de los Casos
Se prueban varias expresiones para verificar la conversión correcta:
- Suma simple (2 + 3).
- Precedencia de operadores (2 + 3 * 4).
- Paréntesis que modifican la precedencia ((2 + 3) * 4).
- Expresión compleja ((1 + 2) * (3 - 4)).
- Expresión con múltiples operadores (a + b * c / d).

---

# Challenge 3: Expression Tree Evaluation

## Descripción general
El código implementa un árbol de expresión binario, donde cada nodo representa un operador aritmético (+, -, *, /) o un valor numérico (operandos). Se define una estructura Node para representar cada nodo del árbol, y una función evaluate_expression_tree para calcular el resultado de la expresión representada por dicho árbol.

## Estructura del código

### Clase Node
- Representa un nodo del árbol de expresión.
- Atributos:
  - value: almacena el valor del nodo (operador o número).
  - left: referencia al hijo izquierdo.
  - right: referencia al hijo derecho.
- Método:
  - __init__(self, value): inicializa el nodo con el valor dado, con hijos None.

### Función evaluate_expression_tree(root)
- Evalúa recursivamente el árbol de expresión.
- Caso base: si el nodo es None, retorna 0.
- Si el nodo es un número (hoja), convierte a entero y retorna.
- Si es un operador, evalúa los subárboles izquierdo y derecho.
- Aplica el operador correspondiente (+, -, *, /).
- En división, usa división entera (//).
- Si el operador es desconocido, lanza un error.

## Pruebas realizadas
- Suma simple: 2 + 3 = 5.
- Multiplicación simple: 4 * 5 = 20.
- Expresión compuesta: 2 + (3 * 4) = 14.
- División entera: 8 / 4 = 2.
- Expresión compleja: (1 + 2) * (8 - 3) = 15.

En cada caso, la función devuelve el resultado correcto.

## Conclusión
La implementación permite evaluar expresiones matemáticas usando árboles binarios y recursión. Es un método claro y efectivo para calcular expresiones compuestas respetando el orden de operaciones.

---

# Challenge 4: Tree Traversal Methods

## Descripción general
El código implementa una estructura para representar árboles binarios de expresión matemática y funciones para recorrer dichos árboles en tres órdenes distintas: inorden, preorden y postorden.

## Estructura del código

### Clase Node
- Representa un nodo del árbol con:
  - value: valor que puede ser un operador (+, -, *, /) o un número.
  - left: hijo izquierdo.
  - right: hijo derecho.
- El constructor inicializa el valor y asigna None a los hijos.

### Funciones de recorrido
- **inorder_traversal(root)**  
  Realiza un recorrido inorden: primero el subárbol izquierdo, luego el nodo actual y finalmente el subárbol derecho.  
  Retorna una lista con los valores visitados en ese orden.

- **preorder_traversal(root)**  
  Recorrido preorden: primero el nodo actual, luego el subárbol izquierdo y después el derecho.  
  Retorna la lista con los valores visitados.

- **postorder_traversal(root)**  
  Recorrido postorden: primero el subárbol izquierdo, luego el derecho y finalmente el nodo actual.  
  Devuelve una lista con los valores visitados.

## Resultados de prueba
Se construyeron dos árboles de expresión y se aplicaron las funciones de recorrido:

Para el primer árbol:
- Inorden: ['2', '+', '3']
- Preorden: ['+', '2', '3']
- Postorden: ['2', '3', '+']

Para el segundo árbol:
- Inorden: ['2', '*', '3', '+', '5']
- Preorden: ['+', '*', '2', '3', '5']
- Postorden: ['2', '3', '*', '5', '+']

## Conclusión
Los recorridos inorden, preorden y postorden permiten explorar un árbol de expresión desde diferentes perspectivas, facilitando la interpretación y evaluación de expresiones matemáticas. Esta implementación es una base útil para aplicaciones que requieran análisis o transformación de expresiones representadas en árboles.

---

# Challenge 5: Expression Tree Simplification

Este código crea un árbol para representar expresiones matemáticas y tiene una función que simplifica ese árbol cuando los valores son números.

## Cómo funciona
- La clase Node crea los nodos del árbol. Cada nodo puede tener un valor (número o símbolo como +, -, *, /) y puede tener hijos a la izquierda y derecha.
- La función simplify_expression_tree revisa el árbol desde abajo hacia arriba. Primero simplifica los hijos, y si ambos hijos son números, hace la operación matemática y reemplaza el nodo con el resultado.
- Si los hijos no son números (por ejemplo, variables o símbolos), la función no cambia ese nodo.
- También revisa si hay división por cero para evitar errores.

## Ejemplo
El árbol representa la expresión (2 + 3) * (4 - 1). Al simplificar, calcula primero 2 + 3 = 5 y 4 - 1 = 3, luego multiplica 5 * 3 = 15. El resultado final del árbol simplificado es un solo nodo con el valor 15.

## Resultado
Al imprimir el valor simplificado, aparece:  
`15`

## Conclusión
La función permite simplificar árboles de expresiones evaluando operaciones con valores numéricos de forma automática. Esto facilita el cálculo y la optimización de expresiones matemáticas, siendo útil en programas que manejan fórmulas o cálculos complejos. Además, maneja errores importantes como la división por cero, lo que hace la función más segura y confiable.
