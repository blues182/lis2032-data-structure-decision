#include <stdio.h>
#include "output.h"

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
            printf("- Manejo de prioridades -> Heap.\n");
            break;
        case DS_GRAPH:
            printf("- Modelo tipo red/grafo.\n");
            break;
        case DS_BST:
            printf("- Datos ordenados -> Árbol BST.\n");
            break;
        case DS_LINKED_LIST:
            printf("- Muchas inserciones en medio -> Lista ligada.\n");
            break;
        case DS_ARRAY:
            printf("- Acceso por indice o caso general -> Arreglo.\n");
            break;
        default:
            printf("- No se pudo determinar claramente.\n");
            break;
    }

    printf("\n");
}

void printDiagram(DataStructure ds) {
    printf(">>> Diagrama aproximado:\n\n");

    switch (ds) {
        case DS_ARRAY:
            printf("[ ] [ ] [ ] [ ] [ ]\n");
            break;
        case DS_LINKED_LIST:
            printf("[dato|*] -> [dato|*] -> [dato|*] -> NULL\n");
            break;
        case DS_STACK:
            printf("top\n |\n[x3]\n[x2]\n[x1]\n(LIFO)\n");
            break;
        case DS_QUEUE:
            printf("front -> [x1] -> [x2] -> [x3] -> rear\n");
            break;
        case DS_BST:
            printf("   9\n  / \\\n 5  10\n/ \\\n3  7\n");
            break;
        case DS_HEAP:
            printf("   42\n  /  \\\n35   23\n/ \\\n27 21\n");
            break;
        case DS_GRAPH:
            printf("A -- B\n| \\ |\nC -- D\n");
            break;
        default:
            printf("N/A\n");
            break;
    }

    printf("\n");
}

void printPseudocode(DataStructure ds) {
    printf(">>> Pseudocodigo:\n\n");

    switch (ds) {
        case DS_STACK:
            printf("PUSH(x): top++; stack[top]=x\nPOP(): x=stack[top]; top--;\n");
            break;
        case DS_QUEUE:
            printf("ENQUEUE(x): rear++\nDEQUEUE(): front++\n");
            break;
        case DS_HEAP:
            printf("INSERT(x):\n  heap[last]=x\n  reHeapUp(last)\n");
            break;
        case DS_BST:
            printf("INSERT(node,x):\n  if x<node.key -> left\n  else -> right\n");
            break;
        case DS_ARRAY:
            printf("A[i] retorna en O(1)\n");
            break;
        case DS_LINKED_LIST:
            printf("insertFront(x): new->next=head\n");
            break;
        case DS_GRAPH:
            printf("addEdge(u,v): lista[u]+=v\n");
            break;
        default:
            printf("N/A\n");
            break;
    }

    printf("\n");
}

void printCourseExample(DataStructure ds) {
    printf(">>> Ejemplo basado en el curso:\n\n");

    switch (ds) {
        case DS_BST:
            printf("BST con recorrido In-Order: 3,5,7,9,10\n");
            break;
        case DS_STACK:
            printf("Stack -> sistema de 'undo'.\n");
            break;
        case DS_QUEUE:
            printf("Queue -> cola de impresion.\n");
            break;
        case DS_ARRAY:
            printf("Array -> calificaciones A[i].\n");
            break;
        case DS_LINKED_LIST:
            printf("Linked List -> lista de tareas.\n");
            break;
        case DS_HEAP:
            printf("Heap -> procesos con prioridad.\n");
            break;
        case DS_GRAPH:
            printf("Graph -> mapa de ciudades.\n");
            break;
        default:
            printf("Ejemplo generico.\n");
            break;
    }

    printf("\n");
}
