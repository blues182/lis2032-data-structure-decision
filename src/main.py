"""
Entry point for the LIS2032 Data Structure Decision System.

Se corre con:
    python3 -m src.main
"""

from .questions import ask_questions, Answers
from .decision import decide_structure, DataStructure

# Intentamos usar una función "bonita" del módulo output.
# Si cambia el nombre, solo ajusta aquí.
try:
    from .output import print_full_report as _printer
except ImportError:
    # Fallback: tal vez la función se llama print_recommendation
    try:
        from .output import print_recommendation as _printer
    except ImportError:
        # Último recurso: imprimimos algo sencillo sin formato especial.
        _printer = None


def main() -> None:
    print("=============================================")
    print("   LIS2032 - Data Structure Decision System")
    print("=============================================\n")

    # 1) Preguntar al usuario
    answers: Answers = ask_questions()

    # 2) Aplicar reglas de decisión
    ds: DataStructure = decide_structure(answers)

    # 3) Mostrar resultado
    if _printer is not None:
        # Usar la función de output.py (rationale, diagrama, etc.)
        _printer(ds, answers)
    else:
        # Versión simple si no existe función en output.py
        print("---------------------------------------------")
        print("Estructura recomendada:", ds.value)
        print("---------------------------------------------")
        print("(Nota: no se encontró función detallada en output.py)")
    print("\nFin del programa.")


if __name__ == "__main__":
    main()
