"""
Módulo de preguntas - Maneja la interacción con el usuario y recopila respuestas
"""

from dataclasses import dataclass


@dataclass
class Answers:
    # Acceso y búsqueda
    needs_random_access: bool
    needs_fast_search: bool
    needs_key_value_lookup: bool
    needs_range_queries: bool
    needs_prefix_search: bool
    
    # Operaciones de modificación
    frequent_insertions: bool
    frequent_deletions: bool
    insert_delete_middle: bool
    data_size_dynamic: bool
    
    # Comportamiento específico
    needs_ordering: bool
    needs_priority: bool
    needs_fifo_processing: bool
    needs_lifo_processing: bool
    has_relationships: bool


def ask_questions() -> Answers:
    """
    Presenta las preguntas al usuario y recopila las respuestas.
    
    Returns:
        Answers: Objeto con todas las respuestas del usuario
    """
    print("=== Sistema de Recomendación de Estructuras de Datos ===\n")
    print("Responde las siguientes preguntas sobre tu problema:\n")

    def ask_bool(prompt: str) -> bool:
        """Función helper para preguntas sí/no con validación"""
        while True:
            val = input(prompt + " (s/n): ").lower().strip()
            if val in ('s', 'si', 'sí', 'y', 'yes', '1'):
                return True
            elif val in ('n', 'no', '0'):
                return False
            print("Por favor, responde 's' o 'n'.\n")

    questions = [
        "1) ¿Necesitas acceder a elementos por su posición/índice frecuentemente?",
        "2) ¿La búsqueda rápida de elementos es una operación crítica?",
        "3) ¿Necesitas asociar claves con valores (como un diccionario)?",
        "4) ¿Requieres buscar elementos dentro de un rango específico?",
        "5) ¿Necesitas buscar palabras por su prefijo?",
        "6) ¿Se insertan nuevos elementos frecuentemente?",
        "7) ¿Se eliminan elementos frecuentemente?",
        "8) ¿Las inserciones/eliminaciones ocurren principalmente en el medio de los datos?",
        "9) ¿El tamaño de los datos cambia constantemente?",
        "10) ¿Los datos deben mantenerse ordenados automáticamente?",
        "11) ¿Necesitas procesar elementos por prioridad (el más importante primero)?",
        "12) ¿Procesas datos en orden de llegada (primero en entrar, primero en salir)?",
        "13) ¿Procesas datos en orden inverso (último en entrar, primero en salir)?",
        "14) ¿Tus datos representan relaciones o conexiones entre elementos?"
    ]

    answers = []
    for question in questions:
        answers.append(ask_bool(question))
        print()

    return Answers(*answers)
