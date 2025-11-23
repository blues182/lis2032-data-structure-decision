#ifndef DECISION_H
#define DECISION_H

#include "questions.h"

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

DataStructure decideStructure(const Answers *a);
const char *dsName(DataStructure ds);

#endif
