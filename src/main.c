#include <stdio.h>
#include "questions.h"
#include "decision.h"
#include "output.h"

/*
 * LIS2032 - Data Structure Decision System
 * Main module: coordina cuestionario, decision y salida.
 */

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

    printf("Fin del programa.\n");
    return 0;
}

