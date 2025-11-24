Responde las siguientes preguntas (s/n) para obtener una recomendación.
----------------------------------------------------------------------
=== Sistema de Recomendación de Estructuras de Datos ===

Responde las siguientes preguntas sobre tu problema:

1) ¿Necesitas acceder a elementos por su posición/índice frecuentemente? (s/n): s

2) ¿La búsqueda rápida de elementos es una operación crítica? (s/n): s

3) ¿Necesitas asociar claves con valores (como un diccionario)? (s/n): s

4) ¿Requieres buscar elementos dentro de un rango específico? (s/n): n

5) ¿Necesitas buscar palabras por su prefijo? (s/n): s

6) ¿Se insertan nuevos elementos frecuentemente? (s/n): s

7) ¿Se eliminan elementos frecuentemente? (s/n): s

8) ¿Las inserciones/eliminaciones ocurren principalmente en el medio de los datos? (s/n): n

9) ¿El tamaño de los datos cambia constantemente? (s/n): n

10) ¿Los datos deben mantenerse ordenados automáticamente? (s/n): n

11) ¿Necesitas procesar elementos por prioridad (el más importante primero)? (s/n): s

12) ¿Procesas datos en orden de llegada (primero en entrar, primero en salir)? (s/n): s

13) ¿Procesas datos en orden inverso (último en entrar, primero en salir)? (s/n): s

14) ¿Tus datos representan relaciones o conexiones entre elementos? (s/n): n


 Analizando tus respuestas...

======================================================================
           RECOMENDACIÓN FINAL
======================================================================

🏆 ESTRUCTURA PRINCIPAL: Hash Table

📝 Explicación: Hash Table ofrece operaciones O(1) promedio para búsquedas rápidas. Especialmente adecuado porque: requieres búsquedas ultrarrápidas.

 ALTERNATIVAS CONSIDERADAS:
   • Balanced BST (AVL/Red-Black)
   • Linked List (Singly)

💡 Puedes considerar las alternativas si tienes requisitos adicionales

============================================================
=== Rationale ===
Se recomienda: Hash Table

1. Búsqueda rápida crítica → Hash Table ofrece O(1) promedio
2. Asociación clave-valor requerida → Hash Table especializado
3. Inserción y eliminación: O(1) promedio
4. Ideal para diccionarios, cachés, bases de datos

=== Diagrama Visual ===

        Buckets:
        0: [ ]
        1: [("key1", value1)]
        2: [("key2", value2)]
        3: [ ]
        
        Hash function: h(key) → bucket_index
        Lookup promedio: O(1)


=== Pseudocódigo (con Complejidad Temporal) ===

// HASH TABLE OPERATIONS
PUT(key, value):            // O(1) promedio
    index = hash(key) % table_size
    bucket = table[index]
    append((key, value) to bucket)

GET(key):                   // O(1) promedio
    index = hash(key) % table_size
    bucket = table[index]
    for each (k, v) in bucket:
        if k == key:
            return v
    return NULL


=== Ejemplo Basado en Actividad del Curso ===

ACTIVIDAD: Dictionary Implementation
INPUT: Pares: {"name": "Alice", "age": "25", "course": "DS"}

OPERACIONES HASH TABLE:
1. put("name", "Alice") → Bucket[h("name")] = ("name", "Alice")
2. put("age", "25")     → Bucket[h("age")] = ("age", "25")
3. get("name") → "Alice" (O(1) promedio)

OUTPUT: Diccionario eficiente para lookup rápido

POR QUÉ HASH TABLE ES ADECUADA:
- Lookup O(1) promedio para búsquedas rápidas
- Ideal para asociaciones clave-valor

============================================================

¿Deseas realizar otra consulta? (s/n): 
