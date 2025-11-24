"""
Módulo de decisión - Contiene la lógica para recomendar estructuras de datos
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List
from questions import Answers


class DataStructure(Enum):
    
    ARRAY = auto()
    DYNAMIC_ARRAY = auto()
    LINKED_LIST = auto()
    DOUBLY_LINKED_LIST = auto()
    STACK = auto()
    QUEUE = auto()
    BST = auto()
    BALANCED_BST = auto()
    HEAP = auto()
    HASH_TABLE = auto()
    GRAPH = auto()
    TRIE = auto()


def ds_name(ds: DataStructure) -> str:
    
    names = {
        DataStructure.ARRAY: "Array (Estático)",
        DataStructure.DYNAMIC_ARRAY: "Dynamic Array",
        DataStructure.LINKED_LIST: "Linked List (Singly)",
        DataStructure.DOUBLY_LINKED_LIST: "Doubly Linked List",
        DataStructure.STACK: "Stack",
        DataStructure.QUEUE: "Queue",
        DataStructure.BST: "Binary Search Tree (BST)",
        DataStructure.BALANCED_BST: "Balanced BST (AVL/Red-Black)",
        DataStructure.HEAP: "Heap / Priority Queue",
        DataStructure.HASH_TABLE: "Hash Table",
        DataStructure.GRAPH: "Graph",
        DataStructure.TRIE: "Trie",
    }
    return names[ds]


@dataclass
class Recommendation:
    
    primary: DataStructure
    alternatives: List[DataStructure]
    rationale: str


def weighted_decision(ans: Answers) -> Recommendation:
    """
    Toma decisiones basadas en un sistema de puntuación ponderada.
    
    Args:
        ans: Respuestas del usuario
        
    Returns:
        Recommendation: Recomendación completa con estructura principal y alternativas
    """
    scores = {
        DataStructure.ARRAY: 0,
        DataStructure.DYNAMIC_ARRAY: 0,
        DataStructure.LINKED_LIST: 0,
        DataStructure.DOUBLY_LINKED_LIST: 0,
        DataStructure.STACK: 0,
        DataStructure.QUEUE: 0,
        DataStructure.BST: 0,
        DataStructure.BALANCED_BST: 0,
        DataStructure.HEAP: 0,
        DataStructure.HASH_TABLE: 0,
        DataStructure.GRAPH: 0,
        DataStructure.TRIE: 0,
    }
    
    # ===== REGLAS DE DECISIÓN =====
    
    # 1. ACCESO Y BÚSQUEDA
    if ans.needs_random_access:
        scores[DataStructure.ARRAY] += 4
        scores[DataStructure.DYNAMIC_ARRAY] += 3
        scores[DataStructure.HASH_TABLE] += 2
    
    if ans.needs_fast_search:
        scores[DataStructure.HASH_TABLE] += 5
        scores[DataStructure.BALANCED_BST] += 4
        scores[DataStructure.BST] += 3
    
    if ans.needs_key_value_lookup:
        scores[DataStructure.HASH_TABLE] += 5
        scores[DataStructure.BALANCED_BST] += 3
        scores[DataStructure.BST] += 2
    
    if ans.needs_range_queries:
        scores[DataStructure.BALANCED_BST] += 5
        scores[DataStructure.BST] += 4
        scores[DataStructure.ARRAY] += 2
    
    if ans.needs_prefix_search:
        scores[DataStructure.TRIE] += 5
        scores[DataStructure.BALANCED_BST] += 2
    
    # 2. OPERACIONES DE MODIFICACIÓN
    if ans.frequent_insertions:
        scores[DataStructure.LINKED_LIST] += 3
        scores[DataStructure.DOUBLY_LINKED_LIST] += 3
        scores[DataStructure.HASH_TABLE] += 2
    
    if ans.frequent_deletions:
        scores[DataStructure.LINKED_LIST] += 3
        scores[DataStructure.DOUBLY_LINKED_LIST] += 3
        scores[DataStructure.HASH_TABLE] += 2
    
    if ans.insert_delete_middle:
        scores[DataStructure.LINKED_LIST] += 4
        scores[DataStructure.DOUBLY_LINKED_LIST] += 5
        scores[DataStructure.ARRAY] -= 3
    
    if ans.data_size_dynamic:
        scores[DataStructure.DYNAMIC_ARRAY] += 3
        scores[DataStructure.LINKED_LIST] += 3
        scores[DataStructure.DOUBLY_LINKED_LIST] += 3
        scores[DataStructure.HASH_TABLE] += 2
    
    # 3. COMPORTAMIENTO ESPECÍFICO
    if ans.needs_ordering:
        scores[DataStructure.BALANCED_BST] += 5
        scores[DataStructure.BST] += 4
        scores[DataStructure.HEAP] += 2
    
    if ans.needs_priority:
        scores[DataStructure.HEAP] += 5
        scores[DataStructure.BALANCED_BST] += 3
    
    if ans.needs_fifo_processing:
        scores[DataStructure.QUEUE] += 5
        scores[DataStructure.DOUBLY_LINKED_LIST] += 3
    
    if ans.needs_lifo_processing:
        scores[DataStructure.STACK] += 5
        scores[DataStructure.LINKED_LIST] += 3
    
    if ans.has_relationships:
        scores[DataStructure.GRAPH] += 5
        scores[DataStructure.HASH_TABLE] += 2
    
    # ===== SELECCIÓN FINAL =====
    
    valid_structures = [(ds, score) for ds, score in scores.items() if score > 0]
    
    if not valid_structures:
        # Fallback por defecto
        primary = DataStructure.ARRAY
        alternatives = [DataStructure.DYNAMIC_ARRAY, DataStructure.LINKED_LIST]
    else:
        # Ordenar por puntuación descendente
        valid_structures.sort(key=lambda x: x[1], reverse=True)
        primary = valid_structures[0][0]
        
        # Seleccionar alternativas (máximo 2)
        alternatives = []
        for ds, score in valid_structures[1:]:
            if len(alternatives) < 2 and score > 0:
                alternatives.append(ds)
    
    # Generar rationale
    rationale = generate_rationale(primary, ans)
    
    return Recommendation(primary, alternatives, rationale)


def generate_rationale(primary: DataStructure, ans: Answers) -> str:
    
    base_rationale = {
        DataStructure.ARRAY: 
            "Array es ideal cuando necesitas acceso rápido por índice y el tamaño de datos es predecible.",
        DataStructure.DYNAMIC_ARRAY:
            "Dynamic Array combina acceso rápido por índice con crecimiento dinámico cuando el tamaño es variable.",
        DataStructure.LINKED_LIST:
            "Linked List es perfecta para inserciones y eliminaciones frecuentes, especialmente en el medio.",
        DataStructure.DOUBLY_LINKED_LIST:
            "Doubly Linked List ofrece operaciones eficientes en ambas direcciones.",
        DataStructure.STACK:
            "Stack es la elección natural para procesamiento LIFO (Last-In-First-Out).",
        DataStructure.QUEUE:
            "Queue es esencial para procesamiento FIFO (First-In-First-Out) como scheduling.",
        DataStructure.BST:
            "Binary Search Tree mantiene los datos ordenados automáticamente con búsquedas eficientes.",
        DataStructure.BALANCED_BST:
            "Balanced BST garantiza operaciones O(log n) incluso en el peor caso.",
        DataStructure.HEAP:
            "Heap implementa colas de prioridad eficientes con acceso O(1) al elemento más importante.",
        DataStructure.HASH_TABLE:
            "Hash Table ofrece operaciones O(1) promedio para búsquedas rápidas.",
        DataStructure.GRAPH:
            "Graph modela relaciones complejas entre elementos, esencial para redes.",
        DataStructure.TRIE:
            "Trie es especializado en búsqueda por prefijo y operaciones con strings.",
    }
    
    rationale = base_rationale.get(primary, "Estructura seleccionada basada en tus necesidades.")
    
    # Añadir razones específicas basadas en respuestas
    specific_reasons = []
    
    if ans.needs_random_access and primary in [DataStructure.ARRAY, DataStructure.DYNAMIC_ARRAY]:
        specific_reasons.append("necesitas acceso por índice constante")
    
    if ans.insert_delete_middle and primary in [DataStructure.LINKED_LIST, DataStructure.DOUBLY_LINKED_LIST]:
        specific_reasons.append("realizas muchas operaciones en el medio")
    
    if ans.needs_fast_search and primary == DataStructure.HASH_TABLE:
        specific_reasons.append("requieres búsquedas ultrarrápidas")
    
    if ans.needs_ordering and primary in [DataStructure.BST, DataStructure.BALANCED_BST]:
        specific_reasons.append("necesitas mantener datos ordenados")
    
    if ans.needs_priority and primary == DataStructure.HEAP:
        specific_reasons.append("manejas elementos por prioridad")
    
    if ans.has_relationships and primary == DataStructure.GRAPH:
        specific_reasons.append("tus datos representan relaciones")
    
    if ans.needs_prefix_search and primary == DataStructure.TRIE:
        specific_reasons.append("realizas búsquedas por prefijo")
    
    if specific_reasons:
        rationale += f" Especialmente adecuado porque: {', '.join(specific_reasons)}."
    
    return rationale
