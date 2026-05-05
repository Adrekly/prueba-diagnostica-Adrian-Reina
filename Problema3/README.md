# Problema 3: Demostración de la Conjetura de Collatz 🔢

Este módulo contiene un programa desarrollado en **Python 2.7** diseñado para verificar la validez de la Conjetura de Collatz dentro de un intervalo numérico específico, integrando auditoría de reglas de entrada.

## 📝 Descripción del Problema

La Conjetura de Collatz (o problema $3n + 1$) postula que para cualquier entero positivo $n$, la aplicación sucesiva de las siguientes reglas siempre conducirá al número 1:
1. Si $n$ es **par**, se divide por 2 ($n/2$).
2. Si $n$ es **impar**, se multiplica por 3 y se suma 1 ($3n + 1$).

### Regla de Validación
El programa implementa una restricción de seguridad obligatoria: para evaluar un intervalo $[p, q]$, se debe cumplir estrictamente que:
$$q \ge 100p$$

## 💻 Implementación Técnica

El script `main.py` se estructura en dos funciones principales:

*   **`calcular_collatz(n)`**: Implementa el bucle iterativo `while n != 1` para generar la secuencia completa de un número. Retorna una cadena formateada con flechas (`->`) para representar visualmente el camino hacia el 1.
*   **`demostracion_collatz(p, q)`**: Actúa como el controlador de la lógica de negocio. Realiza el cálculo del límite requerido y aborta la ejecución si el intervalo no cumple con la proporción mínima de 100 veces el valor inicial.

## 🚀 Ejecución

Para ejecutar la demostración, asegúrese de estar en el directorio del problema y ejecute:

```bash
python main.py