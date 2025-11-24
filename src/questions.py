from dataclasses import dataclass


@dataclass
class Answers:
    wants_random_access: bool
    needs_lifo: bool
    needs_fifo: bool
    many_middle_insertions: bool
    needs_ordering: bool
    needs_priority: bool
    has_graph_relationships: bool


def ask_questions() -> Answers:
    print("Responde las siguientes preguntas sobre tu problema:\n")

    def ask_bool(prompt: str) -> bool:
        while True:
            val = input(prompt + " (0 = No, 1 = Sí): ")
            if val in ("0", "1"):
                return val == "1"
            print("Entrada inválida. Usa 0 o 1.\n")

    return Answers(
        wants_random_access=ask_bool("1) ¿Necesitas acceso rápido por índice (A[i])?"),
        needs_lifo=ask_bool("2) ¿Tus operaciones principales son tipo LIFO (Stack)?"),
        needs_fifo=ask_bool("3) ¿Tus operaciones principales son tipo FIFO (Queue)?"),
        many_middle_insertions=ask_bool("4) ¿Realizas muchas inserciones/borrados en medio?"),
        needs_ordering=ask_bool("5) ¿Requieres mantener los datos ordenados permanentemente?"),
        needs_priority=ask_bool("6) ¿Debes manejar prioridades? (Heap)"),
        has_graph_relationships=ask_bool("7) ¿Tu modelo requiere relaciones tipo grafo?"),
    )
