#include <stdio.h>
#include "questions.h"

/* Pregunta al usuario usando 0 = No, 1 = Sí */
static int askYesNo(const char *question) {
    int answer = -1;

    while (answer != 0 && answer != 1) {
        int scanned;
        printf("%s (0 = No, 1 = Si): ", question);
        scanned = scanf("%d", &answer);
        if (scanned != 1) {
            int c;
            while ((c = getchar()) != '\n' && c != EOF);
            answer = -1;
        }
    }
    return answer;
}

/* Lógica del cuestionario */
void askQuestions(Answers *a) {
    printf("Responde las siguientes preguntas sobre tu problema:\n\n");

    a->wantsRandomAccess = askYesNo("1) ¿Necesitas acceso rapido por indice (A[i])?");
    a->needsLIFO = askYesNo("2) ¿Tus operaciones principales son tipo LIFO?");
    a->needsFIFO = askYesNo("3) ¿Tus operaciones principales son tipo FIFO?");
    a->manyMiddleInsertions = askYesNo("4) ¿Habra muchas inserciones/borrados en medio?");
    a->needsOrdering = askYesNo("5) ¿Necesitas estructura siempre ordenada?");
    a->needsPriority = askYesNo("6) ¿Necesitas manejar prioridades?");
    a->hasGraphRelationships = askYesNo("7) ¿Tu informacion se modela como un grafo?");
}
