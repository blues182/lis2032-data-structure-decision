

"""
SISTEMA GUIADO DE SELECCIÓN DE ESTRUCTURAS DE DATOS
Archivo principal - Punto de entrada del sistema
"""

import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


from questions import ask_questions
from decision import weighted_decision, ds_name
from output import print_all_output


def print_welcome():
    """Imprime el mensaje de bienvenida"""
    print("=" * 70)
    print("        SISTEMA GUIADO DE ESTRUCTURAS DE DATOS")
    print("=" * 70)
    print("\nEste sistema te ayudará a seleccionar la estructura de datos")
    print("más adecuada para tu problema basado en tus necesidades específicas.")
    print("\nResponde las siguientes preguntas (s/n) para obtener una recomendación.")
    print("-" * 70)


def print_recommendation(recommendation):
    """Imprime la recomendación principal y alternativas"""
    print("\n" + "=" * 70)
    print("           RECOMENDACIÓN FINAL")
    print("=" * 70)
    
    print(f"\n🏆 ESTRUCTURA PRINCIPAL: {ds_name(recommendation.primary)}")
    print(f"\n📝 Explicación: {recommendation.rationale}")
    
    if recommendation.alternatives:
        print(f"\n ALTERNATIVAS CONSIDERADAS:")
        for alt in recommendation.alternatives:
            print(f"   • {ds_name(alt)}")
        
        print("\n💡 Puedes considerar las alternativas si tienes requisitos adicionales")


def ask_restart():
    """Pregunta al usuario si quiere realizar otra consulta"""
    while True:
        response = input("\n¿Deseas realizar otra consulta? (s/n): ").lower().strip()
        if response in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Por favor, responde 's' o 'n'.")


def main():
    """Función principal del programa"""
    try:
        while True:
            # Limpiar pantalla (opcional)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Mostrar bienvenida
            print_welcome()
            
            # Obtener respuestas del usuario
            answers = ask_questions()
            
            # Tomar decisión
            print("\n Analizando tus respuestas...")
            recommendation = weighted_decision(answers)
            
            # Mostrar resultados
            print_recommendation(recommendation)
            
            # Mostrar información detallada
            print_all_output(recommendation.primary, answers)
            
            # Preguntar por otra consulta
            if not ask_restart():
                break
        
        print("\n🎯 ¡Gracias por usar el Sistema Guiado de Estructuras de Datos!")
        print("   ¡Buena suerte con tu implementación!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        print("¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, contacta al soporte técnico.")


if __name__ == "__main__":
    main()
