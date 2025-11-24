from typing import Optional
from dataclasses import dataclass
from .decision import DataStructure, ds_name
from .questions import Answers


# --------------------------
# 1. RATIONALE
# --------------------------

def print_rationale(ds: DataStructure, ans: Answers) -> None:
    print("=== Rationale ===")
    print(f"Se recomienda: {ds_name(ds)}\n")

    if ds == DataStructure.ARRAY:
        print("- Acceso aleatorio en O(1).")
        print("- Ideal cuando necesitas A[i] constante.")
        return

    if ds == DataStructure.LINKED_LIST:
        print("- Muchas operaciones de inserción/borrado en medio.")
        print("- Estructura dinámica, sin reubicación de memoria.")
        return

    if ds == DataStructure.STACK:
        print("- Operaciones LIFO: push/pop.")
        print("- Relacionado con tareas como Parenthesis Checker.")
        return

    if ds == DataStructure.QUEUE:
        print("- Operaciones FIFO.")
        print("- Relacionado con ‘Queue using arrays/linked list’.")
        return

    if ds == DataStructure.BST:
        print("- Datos ordenados permanentemente.")
        print("- In-order traversal produce lista ordenada.")
        print("- Relacionado con actividades de Binary Tree.")
        return

    if ds == DataStructure.HEAP:
        print("- Necesidad de prioridades.")
        print("- Implementa Priority Queue.")
        return

    if ds == DataStructure.GRAPH:
        print("- Modelo basado en nodos y relaciones.")
        print("- Relacionado con actividad de Graph & Adjacency.")
        return


# --------------------------
# 2. ASCII DIAGRAMS
# --------------------------

def print_diagram(ds: DataStructure) -> None:
    print("\n=== Diagram ===")

    if ds == DataStructure.STACK:
        print("""
   ┌────┐
   │ 10 │ ← top
   ├────┤
   │  7 │
   ├────┤
   │  3 │
   └────┘
(Operaciones: push/pop)
""")
        return

    if ds == DataStructure.QUEUE:
        print("""
front → [ 3 | 5 | 7 | 9 ] ← rear
(Operaciones: enqueue/dequeue)
""")
        return

    if ds == DataStructure.BST:
        print("""
       ( 7 )
      /     \\
    (3)     (9)
           /   \\
         (8)   (10)

In-order: 3, 7, 8, 9, 10
""")
        return

    if ds == DataStructure.LINKED_LIST:
        print("""
[3] → [5] → [7] → [9] → None
""")
        return

    if ds == DataStructure.ARRAY:
        print("""
Index : 0   1   2   3   4
Value : 3 | 5 | 7 | 9 | 10
""")
        return

    if ds == DataStructure.GRAPH:
        print("""
   A —— B
   | \\  |
   C —— D
""")
        return

    if ds == DataStructure.HEAP:
        print("""
        (10)
       /    \\
     (7)    (5)
     / \\
   (3) (1)
""")
        return


# --------------------------
# 3. PSEUDOCODE
# --------------------------

def print_pseudocode(ds: DataStructure) -> None:
    print("\n=== Pseudocode ===")

    if ds == DataStructure.STACK:
        print("""
PUSH(x):
    top = top + 1
    S[top] = x

POP():
    x = S[top]
    top = top - 1
    return x
""")
        return

    if ds == DataStructure.QUEUE:
        print("""
ENQUEUE(x):
    rear = rear + 1
    Q[rear] = x

DEQUEUE():
    x = Q[front]
    front = front + 1
    return x
""")
        return

    if ds == DataStructure.BST:
        print("""
INSERT(node, x):
    if node == NULL:
        return new Node(x)
    if x < node.value:
        node.left = INSERT(node.left, x)
    else:
        node.right = INSERT(node.right, x)
    return node

INORDER(node):
    if node != NULL:
        INORDER(node.left)
        print(node.value)
        INORDER(node.right)
""")
        return

    print("(No pseudocódigo requerido para esta estructura.)")


# --------------------------
# 4. COURSE EXAMPLE
# --------------------------

def print_course_example(ds: DataStructure) -> None:
    print("\n=== Course Example ===")

    if ds == DataStructure.STACK:
        print("Ejemplo basado en: Stack - Parenthesis Checker.")
        return

    if ds == DataStructure.QUEUE:
        print("Ejemplo basado en: Queue using arrays/linked list.")
        return

    if ds == DataStructure.BST:
        print("Ejemplo basado en: Activity - Binary Tree.")
        print("BST ejemplo con valores: 9, 5, 3, 7, 10.")
        return

    if ds == DataStructure.GRAPH:
        print("Ejemplo basado en: Graph - Adjacency activity.")
        return

    if ds == DataStructure.LINKED_LIST:
        print("Ejemplo basado en: Linked List ADT.")
        return

    if ds == DataStructure.ARRAY:
        print("Ejemplo basado en: Arrays in C / Spiral Matrix.")
        return

    if ds == DataStructure.HEAP:
        print("Ejemplo basado en: Priority Queue (Heap).")
        return
from typing import Optional
from dataclasses import dataclass
from .decision import DataStructure, ds_name
from .questions import Answers


# --------------------------
# 1. RATIONALE
# --------------------------

def print_rationale(ds: DataStructure, ans: Answers) -> None:
    print("=== Rationale ===")
    print(f"Se recomienda: {ds_name(ds)}\n")

    if ds == DataStructure.ARRAY:
        print("- Acceso aleatorio en O(1).")
        print("- Ideal cuando necesitas A[i] constante.")
        return

    if ds == DataStructure.LINKED_LIST:
        print("- Muchas operaciones de inserción/borrado en medio.")
        print("- Estructura dinámica, sin reubicación de memoria.")
        return

    if ds == DataStructure.STACK:
        print("- Operaciones LIFO: push/pop.")
        print("- Relacionado con tareas como Parenthesis Checker.")
        return

    if ds == DataStructure.QUEUE:
        print("- Operaciones FIFO.")
        print("- Relacionado con ‘Queue using arrays/linked list’.")
        return

    if ds == DataStructure.BST:
        print("- Datos ordenados permanentemente.")
        print("- In-order traversal produce lista ordenada.")
        print("- Relacionado con actividades de Binary Tree.")
        return

    if ds == DataStructure.HEAP:
        print("- Necesidad de prioridades.")
        print("- Implementa Priority Queue.")
        return

    if ds == DataStructure.GRAPH:
        print("- Modelo basado en nodos y relaciones.")
        print("- Relacionado con actividad de Graph & Adjacency.")
        return


# --------------------------
# 2. ASCII DIAGRAMS
# --------------------------

def print_diagram(ds: DataStructure) -> None:
    print("\n=== Diagram ===")

    if ds == DataStructure.STACK:
        print("""
   ┌────┐
   │ 10 │ ← top
   ├────┤
   │  7 │
   ├────┤
   │  3 │
   └────┘
(Operaciones: push/pop)
""")
        return

    if ds == DataStructure.QUEUE:
        print("""
front → [ 3 | 5 | 7 | 9 ] ← rear
(Operaciones: enqueue/dequeue)
""")
        return

    if ds == DataStructure.BST:
        print("""
       ( 7 )
      /     \\
    (3)     (9)
           /   \\
         (8)   (10)

In-order: 3, 7, 8, 9, 10
""")
        return

    if ds == DataStructure.LINKED_LIST:
        print("""
[3] → [5] → [7] → [9] → None
""")
        return

    if ds == DataStructure.ARRAY:
        print("""
Index : 0   1   2   3   4
Value : 3 | 5 | 7 | 9 | 10
""")
        return

    if ds == DataStructure.GRAPH:
        print("""
   A —— B
   | \\  |
   C —— D
""")
        return

    if ds == DataStructure.HEAP:
        print("""
        (10)
       /    \\
     (7)    (5)
     / \\
   (3) (1)
""")
        return


# --------------------------
# 3. PSEUDOCODE
# --------------------------

def print_pseudocode(ds: DataStructure) -> None:
    print("\n=== Pseudocode ===")

    if ds == DataStructure.STACK:
        print("""
PUSH(x):
    top = top + 1
    S[top] = x

POP():
    x = S[top]
    top = top - 1
    return x
""")
        return

    if ds == DataStructure.QUEUE:
        print("""
ENQUEUE(x):
    rear = rear + 1
    Q[rear] = x

DEQUEUE():
    x = Q[front]
    front = front + 1
    return x
""")
        return

    if ds == DataStructure.BST:
        print("""
INSERT(node, x):
    if node == NULL:
        return new Node(x)
    if x < node.value:
        node.left = INSERT(node.left, x)
    else:
        node.right = INSERT(node.right, x)
    return node

INORDER(node):
    if node != NULL:
        INORDER(node.left)
        print(node.value)
        INORDER(node.right)
""")
        return

    print("(No pseudocódigo requerido para esta estructura.)")


# --------------------------
# 4. COURSE EXAMPLE
# --------------------------

def print_course_example(ds: DataStructure) -> None:
    print("\n=== Course Example ===")

    if ds == DataStructure.STACK:
        print("Ejemplo basado en: Stack - Parenthesis Checker.")
        return

    if ds == DataStructure.QUEUE:
        print("Ejemplo basado en: Queue using arrays/linked list.")
        return

    if ds == DataStructure.BST:
        print("Ejemplo basado en: Activity - Binary Tree.")
        print("BST ejemplo con valores: 9, 5, 3, 7, 10.")
        return

    if ds == DataStructure.GRAPH:
        print("Ejemplo basado en: Graph - Adjacency activity.")
        return

    if ds == DataStructure.LINKED_LIST:
        print("Ejemplo basado en: Linked List ADT.")
        return

    if ds == DataStructure.ARRAY:
        print("Ejemplo basado en: Arrays in C / Spiral Matrix.")
        return

    if ds == DataStructure.HEAP:
        print("Ejemplo basado en: Priority Queue (Heap).")
        return
