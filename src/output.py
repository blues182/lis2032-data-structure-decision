
from decision import DataStructure, ds_name
from questions import Answers


def print_rationale(ds: DataStructure, ans: Answers) -> None:
    
    print("=== Rationale ===")
    print(f"Se recomienda: {ds_name(ds)}\n")
    
    reasons = []
    
    if ds == DataStructure.ARRAY:
        if ans.needs_random_access:
            reasons.append("Necesitas acceso por índice → Array ofrece O(1)")
        if not ans.data_size_dynamic:
            reasons.append("Tamaño de datos predecible → Array eficiente en memoria")
        reasons.append("Acceso secuencial eficiente por localidad de caché")
    
    elif ds == DataStructure.LINKED_LIST:
        if ans.insert_delete_middle:
            reasons.append("Muchas inserciones/eliminaciones en medio → O(1) en nodos conocidos")
        if ans.data_size_dynamic:
            reasons.append("Tamaño muy variable → Crecimiento dinámico sin reorganización")
        reasons.append("Inserción/eliminación en extremos: O(1)")
    
    elif ds == DataStructure.STACK:
        if ans.needs_lifo_processing:
            reasons.append("Procesamiento LIFO requerido → Stack ideal para undo/redo")
        reasons.append("Operaciones push/pop: O(1)")
        reasons.append("Estructura fundamental para algoritmos recursivos")
    
    elif ds == DataStructure.QUEUE:
        if ans.needs_fifo_processing:
            reasons.append("Procesamiento FIFO requerido → Queue ideal para scheduling")
        reasons.append("Operaciones enqueue/dequeue: O(1)")
        reasons.append("Perfecta para procesamiento en orden de llegada")
    
    elif ds == DataStructure.BST:
        if ans.needs_ordering:
            reasons.append("Datos deben mantenerse ordenados → BST mantiene orden automático")
        if ans.needs_range_queries:
            reasons.append("Necesitas búsquedas por rango → BST eficiente para range queries")
        reasons.append("Búsqueda, inserción, eliminación: O(log n) en caso promedio")
        reasons.append("In-order traversal produce datos ordenados")
    
    elif ds == DataStructure.HEAP:
        if ans.needs_priority:
            reasons.append("Manejo de prioridades requerido → Heap implementa Priority Queue")
        reasons.append("Acceso al máximo/mínimo: O(1)")
        reasons.append("Inserción y eliminación: O(log n)")
        reasons.append("Ideal para scheduling, algoritmos greedy")
    
    elif ds == DataStructure.HASH_TABLE:
        if ans.needs_fast_search:
            reasons.append("Búsqueda rápida crítica → Hash Table ofrece O(1) promedio")
        if ans.needs_key_value_lookup:
            reasons.append("Asociación clave-valor requerida → Hash Table especializado")
        reasons.append("Inserción y eliminación: O(1) promedio")
        reasons.append("Ideal para diccionarios, cachés, bases de datos")
    
    elif ds == DataStructure.GRAPH:
        if ans.has_relationships:
            reasons.append("Datos representan relaciones/conexiones → Graph modela redes")
        reasons.append("Algoritmos de traversión: BFS/DFS para explorar conexiones")
        reasons.append("Ideal para redes sociales, mapas, dependencias")
    
    elif ds == DataStructure.TRIE:
        if ans.needs_prefix_search:
            reasons.append("Búsqueda por prefijo requerida → Trie especializado en strings")
        reasons.append("Búsqueda de palabras: O(m) donde m es longitud de palabra")
        reasons.append("Ideal para autocompletado, diccionarios, spell checkers")
    
    for i, reason in enumerate(reasons, 1):
        print(f"{i}. {reason}")


def print_diagram(ds: DataStructure) -> None:
    """Imprime diagramas ASCII visuales para cada estructura de datos"""
    print("\n=== Diagrama Visual ===")

    if ds == DataStructure.ARRAY:
        print("""
Índice:   0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
        │  3  │  5  │  7  │  9  │  10 │
        └─────┴─────┴─────┴─────┴─────┘
        ↗
    Acceso directo A[i] en O(1)
""")

    elif ds == DataStructure.LINKED_LIST:
        print("""
        HEAD
          ↓
        [3|•] → [5|•] → [7|•] → [9|•] → NULL
          ↗         ↗
    Inserción rápida en medio: O(1)
""")

    elif ds == DataStructure.STACK:
        print("""
        Operaciones LIFO
        ┌─────┐  ↑
        │  10 │  │ PUSH
        ├─────┤  │
        │  7  │  │
        ├─────┤  │
        │  3  │  ↓ POP
        └─────┘
        TOP
""")

    elif ds == DataStructure.QUEUE:
        print("""
        Operaciones FIFO
        ENQUEUE → ┌─────┬─────┬─────┬─────┐ ← ENQUEUE
                  │  3  │  5  │  7  │  9  │
        DEQUEUE ← └─────┴─────┴─────┴─────┘ → DEQUEUE
                  FRONT                    REAR
""")

    elif ds == DataStructure.BST:
        print("""
            ( 7 )
           /     \\
        (3)       (9)
                /    \\
              (8)    (10)

        In-order traversal: 3, 7, 8, 9, 10
        Búsqueda: O(log n)
""")

    elif ds == DataStructure.HEAP:
        print("""
        Max-Heap:
              (10)
             /    \\
           (7)     (5)
           / \\
         (3) (1)

        Propiedad: Padre ≥ Hijos
        Root siempre es máximo: O(1)
""")

    elif ds == DataStructure.HASH_TABLE:
        print("""
        Buckets:
        0: [ ]
        1: [("key1", value1)]
        2: [("key2", value2)]
        3: [ ]
        
        Hash function: h(key) → bucket_index
        Lookup promedio: O(1)
""")

    elif ds == DataStructure.GRAPH:
        print("""
        Graph no dirigido:
           A —— B
           | \\  |
           C —— D

        Adjacency List:
        A: [B, C, D]
        B: [A, D]
        C: [A, D]
        D: [A, B, C]
""")

    elif ds == DataStructure.TRIE:
        print("""
            (root)
           /    \\
          C      B
         /        \\
        A          A
       /            \\
      T              T
     /
    Strings: "CAT", "BAT"
    Prefix search: "CA" → "CAT"
""")


def print_pseudocode(ds: DataStructure) -> None:
    """Imprime pseudocódigo con complejidades temporales para operaciones principales"""
    print("\n=== Pseudocódigo (con Complejidad Temporal) ===")

    if ds == DataStructure.ARRAY:
        print("""
// ARRAY OPERATIONS
ACCESS(index):              // O(1)
    Pre: 0 ≤ index < length
    return A[index]

INSERT(index, value):       // O(n)
    Pre: 0 ≤ index ≤ length
    for i from length down to index+1:
        A[i] = A[i-1]
    A[index] = value
    length = length + 1
""")

    elif ds == DataStructure.LINKED_LIST:
        print("""
// LINKED LIST OPERATIONS
INSERT_AFTER(node, value):  // O(1)
    Pre: node ≠ NULL
    new_node = Node(value)
    new_node.next = node.next
    node.next = new_node

SEARCH(value):              // O(n)
    current = head
    while current ≠ NULL:
        if current.value == value:
            return current
        current = current.next
    return NULL
""")

    elif ds == DataStructure.STACK:
        print("""
// STACK OPERATIONS
PUSH(value):                // O(1)
    Pre: !isFull()
    top = top + 1
    S[top] = value

POP():                      // O(1)
    Pre: !isEmpty()
    value = S[top]
    top = top - 1
    return value
""")

    elif ds == DataStructure.QUEUE:
        print("""
// QUEUE OPERATIONS
ENQUEUE(value):             // O(1)
    Pre: !isFull()
    rear = (rear + 1) % capacity
    Q[rear] = value

DEQUEUE():                  // O(1)
    Pre: !isEmpty()
    value = Q[front]
    front = (front + 1) % capacity
    return value
""")

    elif ds == DataStructure.BST:
        print("""
// BINARY SEARCH TREE OPERATIONS
INSERT(root, value):        // O(h)
    if root == NULL:
        return new Node(value)
    if value < root.value:
        root.left = INSERT(root.left, value)
    else:
        root.right = INSERT(root.right, value)
    return root

SEARCH(root, value):        // O(h)
    if root == NULL OR root.value == value:
        return root
    if value < root.value:
        return SEARCH(root.left, value)
    else:
        return SEARCH(root.right, value)
""")

    elif ds == DataStructure.HEAP:
        print("""
// HEAP OPERATIONS (Max-Heap)
INSERT(heap, value):        // O(log n)
    heap.append(value)
    i = heap.size - 1
    while i > 0 AND heap[parent(i)] < heap[i]:
        swap(heap[parent(i)], heap[i])
        i = parent(i)

EXTRACT_MAX(heap):          // O(log n)
    Pre: heap ≠ empty
    max = heap[0]
    heap[0] = heap[heap.size-1]
    heap.size = heap.size - 1
    MAX_HEAPIFY(heap, 0)
    return max
""")

    elif ds == DataStructure.HASH_TABLE:
        print("""
// HASH TABLE OPERATIONS
PUT(key, value):            // O(1) promedio
    index = hash(key) % table_size
    bucket = table[index]
    append((key, value) to bucket)

GET(key):                   // O(1) promedio
    index = hash(key) % table_size
    bucket = table[index]
    for each (k, v) in bucket:
        if k == key:
            return v
    return NULL
""")

    elif ds == DataStructure.GRAPH:
        print("""
// GRAPH OPERATIONS (BFS)
BFS(start):                 // O(V + E)
    queue = Queue()
    visited = Set()
    queue.enqueue(start)
    visited.add(start)
    
    while not queue.empty():
        current = queue.dequeue()
        for neighbor in graph.adjacency[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
""")

    elif ds == DataStructure.TRIE:
        print("""
// TRIE OPERATIONS
INSERT(root, word):         // O(m)
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end = True

SEARCH(root, word):         // O(m)
    node = root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end
""")


def print_course_example(ds: DataStructure) -> None:
    """Imprime ejemplos concretos basados en actividades del curso"""
    print("\n=== Ejemplo Basado en Actividad del Curso ===")

    if ds == DataStructure.ARRAY:
        print("""
ACTIVIDAD: Spiral Matrix Problem
INPUT: Matrix 3x3
[1, 2, 3]
[4, 5, 6] 
[7, 8, 9]

OPERACIONES:
• Acceso A[0][0] → 1 (O(1))
• Recorrido en espiral

OUTPUT: [1, 2, 3, 6, 9, 8, 7, 4, 5]

POR QUÉ ARRAY ES ADECUADO:
- Acceso directo a elementos por coordenadas
- Algoritmo eficiente para patrones de recorrido
""")

    elif ds == DataStructure.LINKED_LIST:
        print("""
ACTIVIDAD: Linked List ADT Implementation
INPUT: Valores: 3, 5, 7, 9

OPERACIONES:
• Insertar 1 al inicio: [1]→[3]→[5]→[7]→[9] (O(1))
• Insertar 6 después de 5: [1]→[3]→[5]→[6]→[7]→[9] (O(1))

OUTPUT: Lista final: 1→3→5→6→9

POR QUÉ LINKED LIST ES ADECUADA:
- Inserción/eliminación eficiente en cualquier posición
- Tamaño dinámico sin reorganización
""")

    elif ds == DataStructure.STACK:
        print("""
ACTIVIDAD: Parenthesis Checker
INPUT: Expresión "((a+b)*c)"

OPERACIONES STACK:
1. push('(')  → Stack: ['(']
2. push('(')  → Stack: ['(', '(']  
3. pop()      → Stack: ['(']
4. pop()      → Stack: []

OUTPUT: ✅ BALANCED

POR QUÉ STACK ES ADECUADO:
- Naturaleza LIFO coincide con anidamiento
- Complejidad O(n) para expresiones largas
""")

    elif ds == DataStructure.QUEUE:
        print("""
ACTIVIDAD: Queue using Arrays
INPUT: Procesos: ["P1", "P2", "P3", "P4"]

OPERACIONES QUEUE:
1. enqueue("P1") → Queue: ["P1"]
2. enqueue("P2") → Queue: ["P1", "P2"]  
3. dequeue() → "P1" | Queue: ["P2", "P3"]

OUTPUT: Procesados en orden: P1, P2, P3, P4

POR QUÉ QUEUE ES ADECUADA:
- Procesamiento FIFO garantiza orden de llegada
- Operaciones O(1) para enqueue/dequeue
""")

    elif ds == DataStructure.BST:
        print("""
ACTIVIDAD: Binary Search Tree  
INPUT: Valores: 9, 5, 3, 7, 10

OPERACIONES BST:
1. insert(9) → Root: 9
2. insert(5) → 9.left: 5
3. insert(3) → 5.left: 3
4. insert(7) → 5.right: 7
5. insert(10) → 9.right: 10

ESTRUCTURA FINAL:
      9
     / \\
    5   10
   / \\
  3   7

IN-ORDER TRAVERSAL: 3, 5, 7, 9, 10 (ORDENADO)

POR QUÉ BST ES ADECUADO:
- Mantiene datos automáticamente ordenados
- Búsqueda eficiente O(log n)
""")

    elif ds == DataStructure.HEAP:
        print("""
ACTIVIDAD: Priority Queue using Heap
INPUT: Tareas: [(3, "Low"), (7, "Medium"), (10, "High")]

OPERACIONES HEAP:
1. insert(3, "Low")    → Heap: [3]
2. insert(7, "Medium") → Heap: [7, 3]
3. insert(10, "High")  → Heap: [10, 3, 7]

PROCESAMIENTO:
1. extract_max() → "High" (10) | Heap: [7, 3]
2. extract_max() → "Medium" (7) | Heap: [3]

OUTPUT: Procesado por prioridad: High, Medium, Low

POR QUÉ HEAP ES ADECUADO:
- Acceso O(1) al elemento de mayor prioridad
- Inserción y eliminación O(log n)
""")

    elif ds == DataStructure.HASH_TABLE:
        print("""
ACTIVIDAD: Dictionary Implementation
INPUT: Pares: {"name": "Alice", "age": "25", "course": "DS"}

OPERACIONES HASH TABLE:
1. put("name", "Alice") → Bucket[h("name")] = ("name", "Alice")
2. put("age", "25")     → Bucket[h("age")] = ("age", "25")
3. get("name") → "Alice" (O(1) promedio)

OUTPUT: Diccionario eficiente para lookup rápido

POR QUÉ HASH TABLE ES ADECUADA:
- Lookup O(1) promedio para búsquedas rápidas
- Ideal para asociaciones clave-valor
""")

    elif ds == DataStructure.GRAPH:
        print("""
ACTIVIDAD: Graph Traversal - Social Network
INPUT: Red social:
  Alice → Bob, Carol
  Bob → Alice, David  
  Carol → Alice, David

OPERACIONES GRAPH (BFS desde Alice):
1. Visit Alice → Queue: [Alice]
2. Dequeue Alice → Visit Bob, Carol → Queue: [Bob, Carol]
3. Dequeue Bob → Visit David → Queue: [Carol, David]  

BFS TRAVERSAL: Alice, Bob, Carol, David

POR QUÉ GRAPH ES ADECUADO:
- Modela relaciones complejas entre entidades
- Algoritmos para análisis de redes
""")

    elif ds == DataStructure.TRIE:
        print("""
ACTIVIDAD: Autocomplete System
INPUT: Diccionario: ["cat", "car", "cart", "bat", "bar"]

OPERACIONES TRIE:
1. insert("cat")   → c→a→t (end)
2. insert("car")   → c→a→r (end)  
3. insert("cart")  → c→a→r→t (end)

BÚSQUEDA POR PREFIJO "ca":
1. search("ca") → Encuentra nodo "a"
2. Encuentra palabras: "cat", "car", "cart"

AUTOCOMPLETE PARA "ca": ["cat", "car", "cart"]

POR QUÉ TRIE ES ADECUADO:
- Búsqueda por prefijo O(m)
- Ideal para sistemas de autocompletado
""")


def print_all_output(ds: DataStructure, ans: Answers) -> None:
    """
    Función principal de output que coordina la visualización de toda la información
    """
    print("\n" + "="*60)
    print_rationale(ds, ans)
    print_diagram(ds)
    print_pseudocode(ds)
    print_course_example(ds)
    print("="*60)
