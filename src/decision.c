#include "decision.h"

DataStructure decideStructure(const Answers *a) {
    if (a->needsLIFO) return DS_STACK;
    if (a->needsFIFO) return DS_QUEUE;
    if (a->needsPriority) return DS_HEAP;
    if (a->hasGraphRelationships) return DS_GRAPH;
    if (a->needsOrdering) return DS_BST;
    if (a->wantsRandomAccess) return DS_ARRAY;
    if (a->manyMiddleInsertions) return DS_LINKED_LIST;
    return DS_ARRAY;
}

const char *dsName(DataStructure ds) {
    switch (ds) {
        case DS_ARRAY: return "Array (arreglo)";
        case DS_LINKED_LIST: return "Linked List (lista ligada)";
        case DS_STACK: return "Stack (pila)";
        case DS_QUEUE: return "Queue (cola)";
        case DS_BST: return "Binary Search Tree (BST)";
        case DS_HEAP: return "Heap (priority queue)";
        case DS_GRAPH: return "Graph (grafo)";
        default: return "Desconocida";
    }
}
