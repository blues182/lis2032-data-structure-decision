# Cuestionario del Sistema de Recomendación

## Preguntas de Evaluación

### 1. Acceso y Búsqueda

1. **¿Necesitas acceder a elementos por su posición/índice frecuentemente?**
   - *Propósito:* Identificar necesidad de acceso aleatorio O(1)
   - *Estructuras relevantes:* Array, Dynamic Array

2. **¿La búsqueda rápida de elementos es una operación crítica?**
   - *Propósito:* Evaluar importancia de operaciones de búsqueda
   - *Estructuras relevantes:* Hash Table, Balanced BST

3. **¿Necesitas asociar claves con valores (como un diccionario)?**
   - *Propósito:* Detectar necesidad de mapeo clave-valor
   - *Estructuras relevantes:* Hash Table, BST

4. **¿Requieres buscar elementos dentro de un rango específico?**
   - *Propósito:* Identificar necesidad de range queries
   - *Estructuras relevantes:* BST, Balanced BST, Array ordenado

5. **¿Necesitas buscar palabras por su prefijo?**
   - *Propósito:* Detectar operaciones de búsqueda por prefijo
   - *Estructuras relevantes:* Trie, Balanced BST

### 2. Operaciones de Modificación

6. **¿Se insertan nuevos elementos frecuentemente?**
   - *Propósito:* Evaluar frecuencia de operaciones de inserción
   - *Estructuras relevantes:* Linked List, Hash Table, Dynamic Array

7. **¿Se eliminan elementos frecuentemente?**
   - *Propósito:* Evaluar frecuencia de operaciones de eliminación
   - *Estructuras relevantes:* Linked List, Hash Table

8. **¿Las inserciones/eliminaciones ocurren principalmente en el medio de los datos?**
   - *Propósito:* Identificar operaciones en posiciones intermedias
   - *Estructuras relevantes:* Linked List, Doubly Linked List

9. **¿El tamaño de los datos cambia constantemente?**
   - *Propósito:* Evaluar dinamicidad del conjunto de datos
   - *Estructuras relevantes:* Linked List, Dynamic Array, Hash Table

### 3. Comportamiento Específico

10. **¿Los datos deben mantenerse ordenados automáticamente?**
    - *Propósito:* Detectar necesidad de ordenamiento automático
    - *Estructuras relevantes:* BST, Balanced BST

11. **¿Necesitas procesar elementos por prioridad (el más importante primero)?**
    - *Propósito:* Identificar manejo de prioridades
    - *Estructuras relevantes:* Heap, Priority Queue

12. **¿Procesas datos en orden de llegada (primero en entrar, primero en salir)?**
    - *Propósito:* Detectar procesamiento FIFO
    - *Estructuras relevantes:* Queue, Doubly Linked List

13. **¿Procesas datos en orden inverso (último en entrar, primero en salir)?**
    - *Propósito:* Detectar procesamiento LIFO
    - *Estructuras relevantes:* Stack, Linked List

14. **¿Tus datos representan relaciones o conexiones entre elementos?**
    - *Propósito:* Identificar modelado de relaciones
    - *Estructuras relevantes:* Graph, Hash Table (para adjacency list)

## Justificación del Diseño del Cuestionario

### Cobertura Comprehensiva
El cuestionario de 14 preguntas cubre todos los aspectos críticos para la selección de estructuras de datos:

- **Criterios de acceso** (5 preguntas)
- **Patrones de modificación** (4 preguntas)  
- **Comportamientos específicos** (5 preguntas)

### Preguntas Discriminativas
Cada pregunta está diseñada para:
- **Distinguir** entre estructuras con características opuestas
- **Capturar** requisitos fundamentales de rendimiento
- **Identificar** patrones de uso específicos

### Alineación con Objetivos de Aprendizaje
Las preguntas refuerzan conceptos clave del curso:
- Complejidades temporales Big-O
- Trade-offs entre estructuras
- Casos de uso apropiados para cada estructura

