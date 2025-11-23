#include <stdio.h>

/*
 * LIS2032 - Data Structure Decision System
 * Author: Alejandro Luis Cisneros Bernal
 *
 * Guided questionnaire that recommends a data structure based on
 * problem requirements. Structures considered:
 *  - Array
 *  - Linked List
 *  - Stack
 *  - Queue
 *  - Binary Search Tree (BST)
 *  - Heap (Priority Queue)
 *  - Graph
 */

/* Enumeración de estructuras de datos posibles */
typedef enum {
    DS_ARRAY,
    DS_LINKED_LIST,
    DS_STACK,
    DS_QUEUE,
    DS_BST,
    DS_HEAP,
    DS_GRAPH,
    DS_UNKNOWN
} DataStructure;

/* Respuestas del usuario al cuestionario */
typedef struct {
    int wantsRandomAccess;      // acceso por índice frecuente
    int needsLIFO;              // patrón LIFO
    int needsFIFO;              // patrón FIFO
    int manyMiddleInsertions;   // muchas inserciones/borrados en medio
    int needsOrdering;          // necesita mantener orden
    int needsPriority;          // prioridad (max/min primero)
    int hasGraphRelationships;  // modelo tipo grafo
} Answers;

/* Prototipos */
void askQuestions(Answers *a);
int  askYesNo(const char *question);
DataStructure decideStructure(const Answers *a);
const char* dsName(DataStructure ds);
void printRationale(DataStructure ds, const Answers *a);
void printDiagram(DataStructure ds);
void printPseudocode(DataStructure ds);
void printCourseExample(DataStructure ds);

int main(void) {
    Answers ans;
    DataStructure ds;

    printf("=============================================\n");
    printf("  LIS2032 - Data Structure Decision System\n");
    printf("=============================================\n\n");

    askQuestions(&ans);
    ds = decideStructure(&ans);

    printf("\n---------------------------------------------\n");
    printf("Estructura recomendada: %s\n", dsName(ds));
    printf("---------------------------------------------\n\n");

    printRationale(ds, &ans);
    printDiagram(ds);
    printPseudocode(ds);
    printCourseExample(ds);

    printf("\nFin del programa.\n");
    return 0;
}

/* Pregunta al usuario usando 0 = No, 1 = Si */
int askYesNo(const char *question) {
    int answer = -1;

    while (answer != 0 && answer != 1) {
        int scanned;
        printf("%s (0 = No, 1 = Si): ", question);
        scanned = scanf("%d", &answer);
        if (scanned != 1) {
            int c;
            /* limpiar entrada si el usuario mete basura */
            while ((c = getchar()) != '\n' && c != EOF);
            answer = -1;
        }
    }
    return answer;
}

/* 1. Cuestionario: llena la estructura Answers */
void askQuestions(Answers *a) {
    printf("Responde las siguientes preguntas sobre tu problema:\n\n");

    a->wantsRandomAccess = askYesNo(
        "1) ¿Necesitas acceso rapido por indice (A[i])?"
    );

    a->needsLIFO = askYesNo(
        "2) ¿Tus operaciones principales son tipo LIFO (ultimo en entrar, primero en salir)?"
    );

    a->needsFIFO = askYesNo(
        "3) ¿Tus operaciones principales son tipo FIFO (primero en entrar, primero en salir)?"
    );

    a->manyMiddleInsertions = askYesNo(
        "4) ¿Habra muchas inserciones y borrados en el medio de la coleccion?"
    );

    a->needsOrdering = askYesNo(
        "5) ¿Necesitas que los datos se mantengan ordenados permanentemente?"
    );

    a->needsPriority = askYesNo(
        "6) ¿Necesitas manejar prioridades (siempre extraer el elemento mas importante primero)?"
    );

    a->hasGraphRelationships = askYesNo(
        "7) ¿Tu informacion se modela como nodos conectados (grafo: ciudades, redes, etc.)?"
    );
}

/* 2. Logica de decision: usa las respuestas para elegir estructura */
DataStructure decideStructure(const Answers *a) {
    /*
     * Reglas (mismo orden que en docs/decision_rules.md):
     * 1. LIFO  -> Stack
     * 2. FIFO  -> Queue
     * 3. Prioridad -> Heap
     * 4. Grafo -> Graph
     * 5. Necesita orden -> BST
     * 6. Acceso por indice -> Array
     * 7. Muchas inserciones en medio -> Linked List
     * 8. Default -> Array
     */

    if (a->needsLIFO) {
        return DS_STACK;
    }
    if (a->needsFIFO) {
        return DS_QUEUE;
    }
    if (a->needsPriority) {
        return DS_HEAP;
    }
    if (a->hasGraphRelationships) {
        return DS_GRAPH;
    }
    if (a->needsOrdering) {
        return DS_BST;
    }
    if (a->wantsRandomAccess) {
        return DS_ARRAY;
    }
    if (a->manyMiddleInsertions) {
        return DS_LINKED_LIST;
    }

    return DS_ARRAY; /* caso por defecto */
}

/* 3. Nombre legible de la estructura */
const char* dsName(DataStructure ds) {
    switch (ds) {
        case DS_ARRAY:
            return "Array (arreglo)";
        case DS_LINKED_LIST:
            return "Linked List (lista ligada)";
        case DS_STACK:
            return "Stack (pila)";
        case DS_QUEUE:
            return "Queue (cola)";
        case DS_BST:
            return "Binary Search Tree (BST)";
        case DS_HEAP:
            return "Heap (priority queue)";
        case DS_GRAPH:
            return "Graph (grafo)";
        default:
            return "Desconocida";
    }
}

/* 4. Explicacion basada en las respuestas */
void printRationale(DataStructure ds, const Answers *a) {
    (void)a; /* evitar warning si no usamos todas las respuestas */

    printf(">>> Razonamiento de la recomendacion:\n\n");

    switch (ds) {
        case DS_STACK:
            printf("- Tus operaciones principales son tipo LIFO.\n");
            printf("- Una pila es ideal para deshacer operaciones, manejo de llamadas, etc.\n");
            break;

        case DS_QUEUE:
            printf("- Tus operaciones principales son tipo FIFO.\n");
            printf("- Una cola modela procesos en orden de llegada, colas de impresion, etc.\n");
            break;

        case DS_HEAP:
            printf("- Necesitas manejar prioridades (max/min primero).\n");
            printf("- Un heap permite insertar y obtener el elemento de mayor prioridad en O(log n).\n");
            break;

        case DS_GRAPH:
            printf("- Tu informacion se modela como nodos conectados.\n");
            printf("- Un grafo representa rutas, mapas, redes sociales, etc.\n");
            break;

        case DS_BST:
            printf("- Necesitas que los datos se mantengan ordenados.\n");
            printf("- Un BST permite busqueda e insercion eficientes y recorridos en orden.\n");
            break;

        case DS_ARRAY:
            printf("- Valoraste el acceso rapido por indice o no hay requisitos especiales.\n");
            printf("- Un array es simple, eficiente en memoria contigua y rapido para A[i].\n");
            break;

        case DS_LINKED_LIST:
            printf("- Tienes muchas inserciones y borrados en medio.\n");
            printf("- Una lista ligada permite insertar y eliminar nodos sin mover el resto de elementos.\n");
            break;

        default:
            printf("- No fue posible determinar una estructura clara.\n");
            break;
    }

    printf("\n");
}

/* 5. Diagrama simple en ASCII */
void printDiagram(DataStructure ds) {
    printf(">>> Diagrama aproximado de la estructura:\n\n");

    switch (ds) {
        case DS_ARRAY:
            printf("Indices:  0    1    2    3    4\n");
            printf("         [ ]  [ ]  [ ]  [ ]  [ ]\n");
            printf("Memoria contigua, acceso A[i].\n");
            break;

        case DS_LINKED_LIST:
            printf("[dato|*] -> [dato|*] -> [dato|*] -> NULL\n");
            printf("Cada nodo apunta al siguiente.\n");
            break;

        case DS_STACK:
            printf("   +-------+\n");
            printf("top|  x3   |\n");
            printf("   +-------+\n");
            printf("   |  x2   |\n");
            printf("   +-------+\n");
            printf("   |  x1   |\n");
            printf("   +-------+\n");
            printf("     (LIFO)\n");
            break;

        case DS_QUEUE:
            printf("front -> [x1] -> [x2] -> [x3] -> rear\n");
            printf("        (FIFO)\n");
            break;

        case DS_BST:
            printf("        [ 9 ]\n");
            printf("       /     \\\n");
            printf("    [ 5 ]   [ 10 ]\n");
            printf("    /   \\\n");
            printf(" [ 3 ] [ 7 ]\n");
            printf("Propiedad: izquierda < raiz < derecha.\n");
            break;

        case DS_HEAP:
            printf("       [ 42 ]\n");
            printf("      /      \\\n");
            printf("   [ 35 ]   [ 23 ]\n");
            printf("   /   \\\n");
            printf(" [27] [21]\n");
            printf("Max-heap: cada padre >= hijos.\n");
            break;

        case DS_GRAPH:
            printf("  (A) ---- (B)\n");
            printf("   | \\      |\n");
            printf("   |  \\     |\n");
            printf("  (C) ---- (D)\n");
            printf("Nodos conectados por aristas.\n");
            break;

        default:
            printf("(Sin diagrama disponible).\n");
            break;
    }

    printf("\n");
}

/* 6. Pseudocodigo principal de la estructura recomendada */
void printPseudocode(DataStructure ds) {
    printf(">>> Pseudocodigo de operaciones principales:\n\n");

    switch (ds) {
        case DS_STACK:
            printf("PUSH(stack, x):\n");
            printf("    top <- top + 1\n");
            printf("    stack[top] <- x\n\n");
            printf("POP(stack):\n");
            printf("    x <- stack[top]\n");
            printf("    top <- top - 1\n");
            printf("    return x\n");
            break;

        case DS_QUEUE:
            printf("ENQUEUE(queue, x):\n");
            printf("    rear <- (rear + 1) mod MAX\n");
            printf("    queue[rear] <- x\n\n");
            printf("DEQUEUE(queue):\n");
            printf("    front <- (front + 1) mod MAX\n");
            printf("    return queue[front]\n");
            break;

        case DS_HEAP:
            printf("INSERT(heap, item):\n");
            printf("    heap[last] <- item\n");
            printf("    reHeapUp(heap, last)\n");
            printf("    last <- last + 1\n\n");
            printf("reHeapUp(heap, i):\n");
            printf("    while i > 0 and heap[i] > heap[parent(i)]:\n");
            printf("        swap(heap[i], heap[parent(i)])\n");
            printf("        i <- parent(i)\n");
            break;

        case DS_BST:
            printf("INSERT(root, key):\n");
            printf("    if root == NULL:\n");
            printf("        root <- nuevoNodo(key)\n");
            printf("    else if key < root.key:\n");
            printf("        root.left <- INSERT(root.left, key)\n");
            printf("    else:\n");
            printf("        root.right <- INSERT(root.right, key)\n\n");
            printf("INORDER(node):\n");
            printf("    if node != NULL:\n");
            printf("        INORDER(node.left)\n");
            printf("        print node.key\n");
            printf("        INORDER(node.right)\n");
            break;

        case DS_ARRAY:
            printf("GET(A, i):\n");
            printf("    return A[i]\n\n");
            printf("SET(A, i, x):\n");
            printf("    A[i] <- x\n");
            break;

        case DS_LINKED_LIST:
            printf("INSERT_FRONT(head, x):\n");
            printf("    nuevo <- nodo(x)\n");
            printf("    nuevo.next <- head\n");
            printf("    head <- nuevo\n");
            break;

        case DS_GRAPH:
            printf("ADD_EDGE(G, u, v):\n");
            printf("    agregar v a lista G[u]\n");
            printf("    agregar u a lista G[v]  // si es no dirigido\n");
            break;

        default:
            printf("(Sin pseudocodigo disponible).\n");
            break;
    }

    printf("\n");
}

/* 7. Ejemplo basado en actividades del curso */
void printCourseExample(DataStructure ds) {
    printf(">>> Ejemplo basado en el curso LIS2032:\n\n");

    if (ds == DS_BST) {
        printf("Ejemplo de BST con recorrido In-Order:\n\n");
        printf("Insertar: 9, 5, 3, 7, 10\n");
        printf("Arbol (forma conceptual):\n\n");
        printf("        9\n");
        printf("      /   \\\n");
        printf("     5    10\n");
        printf("    / \\\n");
        printf("   3   7\n\n");
        printf("INORDER imprime: 3, 5, 7, 9, 10 (ordenados).\n");
    } else if (ds == DS_STACK) {
        printf("Ejemplo de pila: sistema de deshacer (undo).\n");
        printf("Cada accion se guarda con PUSH().\n");
        printf("Al presionar 'Undo' se hace POP() y se revierte la ultima accion.\n");
    } else if (ds == DS_QUEUE) {
        printf("Ejemplo de cola: trabajos de impresion.\n");
        printf("Los trabajos llegan y se encolan con ENQUEUE().\n");
        printf("La impresora usa DEQUEUE() para tomar el siguiente.\n");
    } else if (ds == DS_ARRAY) {
        printf("Ejemplo de array: lista fija de calificaciones.\n");
        printf("Puedes acceder rapido a la calificacion del alumno i con A[i].\n");
    } else if (ds == DS_LINKED_LIST) {
        printf("Ejemplo de lista ligada: lista de tareas con inserciones en medio.\n");
        printf("Puedes insertar un nuevo nodo entre otros dos sin mover todos los elementos.\n");
    } else if (ds == DS_HEAP) {
        printf("Ejemplo de heap: cola de prioridad de procesos.\n");
        printf("Cada proceso tiene prioridad, y siempre se ejecuta el de mayor prioridad primero.\n");
    } else if (ds == DS_GRAPH) {
        printf("Ejemplo de grafo: mapa de ciudades conectadas por carreteras.\n");
        printf("Cada ciudad es un nodo y cada carretera es una arista.\n");
        printf("Puedes aplicar BFS/DFS para buscar rutas.\n");
    } else {
        printf("Ejemplo generico: coleccion de datos con operaciones basicas.\n");
    }

    printf("\n");
}
