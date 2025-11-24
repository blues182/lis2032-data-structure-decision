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
    printf(">>> Ejemplo basado en el curso LIS2032:\n\n");

    if (ds == DS_BST) {
        /* Ejemplo REAL de lo visto en clase: arbol binario y recorridos */
        int values[] = {9, 5, 3, 7, 10};
        int n = sizeof(values) / sizeof(values[0]);
        Node *root = NULL;

        printf("Construyendo un BST con los valores: ");
        for (int i = 0; i < n; ++i) {
            printf("%d ", values[i]);
            root = bstInsert(root, values[i]);
        }
        printf("\n\nRecorrido In-Order del arbol:\n  ");

        bstInOrder(root);   /* imprime en orden: 3 5 7 9 10 */
        printf("\n\nObservacion: el recorrido In-Order imprime los elementos ordenados.\n");

        bstFree(root);      /* liberar memoria */
    } else {
        /* Para las otras estructuras dejamos ejemplos explicativos simples */
        switch (ds) {
            case DS_STACK:
                printf("Stack: pila de operaciones 'undo' en un editor de texto.\n");
                printf("Cada accion se guarda con PUSH y se revierte con POP.\n");
                break;
            case DS_QUEUE:
                printf("Queue: cola de impresion.\n");
                printf("Los trabajos se encolan en orden de llegada y se atienden FIFO.\n");
                break;
            case DS_ARRAY:
                printf("Array: arreglo de calificaciones A[i] donde cada posicion es un alumno.\n");
                break;
            case DS_LINKED_LIST:
                printf("Linked List: lista de tareas donde insertas y borras elementos en medio.\n");
                break;
            case DS_HEAP:
                printf("Heap: cola de prioridad de procesos del sistema operativo.\n");
                break;
            case DS_GRAPH:
                printf("Graph: mapa de ciudades conectadas por carreteras.\n");
                break;
            default:
                printf("Ejemplo generico: coleccion de datos con inserciones y busquedas.\n");
                break;
        }
    }

    printf("\n");
}

