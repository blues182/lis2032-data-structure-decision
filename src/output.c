#include <stdio.h>
#include <stdlib.h>  /* malloc, free */
#include "output.h"


typedef struct Node {
    int key;
    struct Node *left;
    struct Node *right;
} Node;

/* crea un nuevo nodo */
static Node *newNode(int key) {
    Node *n = (Node *)malloc(sizeof(Node));
    if (n != NULL) {
        n->key = key;
        n->left = NULL;
        n->right = NULL;
    }
    return n;
}


static Node *bstInsert(Node *root, int key) {
    if (root == NULL) {
        return newNode(key);
    }
    if (key < root->key) {
        root->left = bstInsert(root->left, key);
    } else {
        root->right = bstInsert(root->right, key);
    }
    return root;
}

/* recorrido In-Order */
static void bstInOrder(Node *root) {
    if (root != NULL) {
        bstInOrder(root->left);
        printf("%d ", root->key);
        bstInOrder(root->right);
    }
}

/* liberar memoria del arbol */
static void bstFree(Node *root) {
    if (root != NULL) {
        bstFree(root->left);
        bstFree(root->right);
        free(root);
    }
}

/* ---- Funciones públicas de salida ---- */

void printRationale(DataStructure ds, const Answers *a) {
    (void)a;

    printf(">>> Razonamiento de la recomendacion:\n\n");

    switch (ds) {
        case DS_STACK:
            printf("- Operaciones LIFO -> Pila.\n");
            break;
        case DS_QUEUE:
            printf("- Operaciones FIFO -> Cola.\n");
            break;
        case DS_HEAP:
            printf("- Necesitas manejar prioridades -> Heap.\n");
            break;
        case DS_GRAPH:
            printf("- Tu problema se modela como red/grafo.\n");
            break;
        case DS_BST:
            printf("- Necesitas mantener datos ordenados -> BST.\n");
            break;
        case DS_LINKED_LIST:
            printf("- Muchas inserciones/borrados en medio -> Lista ligada.\n");
            break;
        case DS_ARRAY:
            printf("- Acceso rapido por indice o caso general -> Arreglo.\n");
            break;
        default:
            printf("- No se pudo determinar claramente.\n");
            break;
    }

    printf("\n");
}

void printDiagram(DataStructure ds) {
    printf(">>> Diagrama aproximado de la estructura:\n\n");

    switch (ds) {
        case DS_ARRAY:
            printf("Indices:  0    1    2    3    4\n");
            printf("         [ ]  [ ]  [ ]  [ ]  [ ]\n");
            break;

        case DS_LINKED_LIST:
            printf("[dato|*] -> [dato|*] -> [dato|*] -> NULL\n");
            break;

        case DS_STACK:
            printf("top\n |\n[x3]\n[x2]\n[x1]\n(LIFO)\n");
            break;

        case DS_QUEUE:
            printf("front -> [x1] -> [x2] -> [x3] -> rear\n");
            printf("        (FIFO)\n");
            break;

        case DS_BST:
            printf("    9\n");
            printf("   / \\\n");
            printf("  5   10\n");
            printf(" / \\\n");
            printf("3   7\n");
            printf("BST: izquierda < raiz < derecha.\n");
            break;

        case DS_HEAP:
            printf("   42\n");
            printf("  /  \\\n");
            printf("35   23\n");
            printf("/ \\\n");
            printf("27 21\n");
            printf("Max-heap: padre >= hijos.\n");
            break;

        case DS_GRAPH:
            printf("A -- B\n");
            printf("| \\ |\n");
            printf("C -- D\n");
            break;

        default:
            printf("N/A\n");
            break;
    }

    printf("\n");
}

void printPseudocode(DataStructure ds) {
    printf(">>> Pseudocodigo de operaciones principales:\n\n");

    switch (ds) {
        case DS_STACK:
            printf("PUSH(x):\n");
            printf("  top <- top + 1\n");
            printf("  stack[top] <- x\n\n");
            printf("POP():\n");
            printf("  x <- stack[top]\n");
            printf("  top <- top - 1\n");
            printf("  return x\n");
            break;

        case DS_QUEUE:
            printf("ENQUEUE(x):\n");
            printf("  rear <- (rear + 1) mod MAX\n");
            printf("  queue[rear] <- x\n\n");
            printf("DEQUEUE():\n");
            printf("  front <- (front + 1) mod MAX\n");
            printf("  return queue[front]\n");
            break;

        case DS_HEAP:
            printf("INSERT(x):\n");
            printf("  heap[last] <- x\n");
            printf("  reHeapUp(last)\n");
            break;

        case DS_BST:
            printf("INSERT(node, x):\n");
            printf("  if node == NULL -> nuevo nodo\n");
            printf("  else if x < node.key -> insertar en left\n");
            printf("  else -> insertar en right\n\n");
            printf("INORDER(node):\n");
            printf("  if node != NULL:\n");
            printf("    INORDER(node.left)\n");
            printf("    visitar node.key\n");
            printf("    INORDER(node.right)\n");
            break;

        case DS_ARRAY:
            printf("GET(A, i): return A[i]\n");
            break;

        case DS_LINKED_LIST:
            printf("INSERT_FRONT(head, x):\n");
            printf("  nuevo <- nodo(x)\n");
            printf("  nuevo.next <- head\n");
            printf("  head <- nuevo\n");
            break;

        case DS_GRAPH:
            printf("ADD_EDGE(G, u, v):\n");
            printf("  agregar v a lista G[u]\n");
            printf("  agregar u a lista G[v] si es no dirigido\n");
            break;

        default:
            printf("N/A\n");
            break;
    }

    printf("\n");
}

void printCourseExample(DataStructure ds) {
    printf(">>> Ejemplo basado en actividades del curso LIS2032:\n\n");

    if (ds == DS_BST) {
        /* Actividades: Trees, Binary Tree, Red-Black Tree Search Structure */
        int values[] = {9, 5, 3, 7, 10};
        int n = (int)(sizeof(values) / sizeof(values[0]));
        Node *root = NULL;

        printf("Actividades relacionadas: Activity - Trees, Activity - Binary Tree,\n");
        printf("                          Activity - Red-Black Tree Search Structure.\n\n");

        printf("Construyendo un Binary Search Tree (BST) con los valores: ");
        for (int i = 0; i < n; ++i) {
            printf("%d ", values[i]);
            root = bstInsert(root, values[i]);
        }

        printf("\n\nRecorrido In-Order del arbol:\n  ");
        bstInOrder(root);   /* imprime: 3 5 7 9 10 */
        printf("\n\nObservacion: el recorrido In-Order visita los nodos en orden ascendente,\n");
        printf("igual que en las actividades de arboles binarias del curso.\n");

        bstFree(root);      /* liberar memoria */
    } else {
        switch (ds) {
            case DS_ARRAY:
                printf("Actividades relacionadas:\n");
                printf("- Activity 03 - Arrays in C\n");
                printf("- Activity 04 - Arrays and Dynamic Memory\n");
                printf("- Activity 07 - Spiral Matrix\n");
                printf("- 2D Matrix Exercise 01 y 02\n");
                printf("- Activity - File reading\n\n");
                printf("Ejemplo: usar un arreglo o matriz para almacenar datos leidos de un archivo\n");
                printf("y procesarlos por indice (A[i][j]) o en forma de matriz espiral.\n");
                break;

            case DS_LINKED_LIST:
                printf("Actividades relacionadas:\n");
                printf("- Activity 01 - Linked List ADT\n");
                printf("- Activity - Circular Linked List\n");
                printf("- Activity - Queue using Linked List\n\n");
                printf("Ejemplo: lista de nodos donde puedes insertar y eliminar elementos en medio\n");
                printf("sin mover el resto, como en las actividades de listas enlazadas.\n");
                break;

            case DS_STACK:
                printf("Actividades relacionadas:\n");
                printf("- Activity - Stack: Trace the Stack\n");
                printf("- Activity - Stack: Fixing the Bug\n");
                printf("- Activity - Stack - Improving parenthesis checker\n\n");
                printf("Ejemplo: usar una pila para revisar balance de parentesis o para 'undo'.\n");
                printf("Cada simbolo se hace PUSH y se valida la estructura con POP.\n");
                break;

            case DS_QUEUE:
                printf("Actividades relacionadas:\n");
                printf("- Activity - Queues using arrays\n");
                printf("- Activity - Queue using Linked List\n\n");
                printf("Ejemplo: cola de impresion donde los trabajos entran con ENQUEUE y\n");
                printf("se atienden en orden FIFO con DEQUEUE.\n");
                break;

            case DS_HEAP:
                printf("No hubo una actividad de Heap directa, pero se relaciona con:\n");
                printf("- Colas y scheduling de procesos (extension de Queue).\n\n");
                printf("Ejemplo: cola de prioridad donde siempre sale primero el proceso con\n");
                printf("mayor prioridad (como en sistemas operativos).\n");
                break;

            case DS_GRAPH:
                printf("Actividades relacionadas:\n");
                printf("- Activity - Graph - Paper and Pencil\n");
                printf("- Activity - Adjacency\n\n");
                printf("Ejemplo: representar un mapa de ciudades usando lista de adyacencia,\n");
                printf("tal como en los ejercicios de grafos en papel y de matrices/listas\n");
                printf("de adyacencia.\n");
                break;

            default:
                printf("Ejemplo generico: coleccion de datos con inserciones, borrados\n");
                printf("y busquedas segun la estructura seleccionada.\n");
                break;
        }
    }

    printf("\n");
}
