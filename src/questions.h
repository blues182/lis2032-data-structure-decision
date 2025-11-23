#ifndef QUESTIONS_H
#define QUESTIONS_H

/* Respuestas del usuario al cuestionario */
typedef struct {
    int wantsRandomAccess;
    int needsLIFO;
    int needsFIFO;
    int manyMiddleInsertions;
    int needsOrdering;
    int needsPriority;
    int hasGraphRelationships;
} Answers;

/* Pregunta al usuario y llena la estructura Answers */
void askQuestions(Answers *a);

#endif
