# -*- coding: utf-8 -*-

def calcular_collatz(n):
    secuencia = [str(n)]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
        secuencia.append(str(n))
        
    return " -> ".join(secuencia)

def demostracion_collatz(p, q):
    print("Intervalo a evaluar: [{0}, {1}]".format(p, q))
    
    limite_requerido = 100 * p
    if q < limite_requerido:
        print("ERROR: No se puede aplicar la demostracion.")
        print("La regla exige q >= 100p (En este caso: {0} no es mayor o igual a {1})\n".format(q, limite_requerido))
        return
        
    print("Regla q >= 100p CUMPLIDA ({0} >= {1}). Iniciando demostracion...\n".format(q, limite_requerido))
    
    for i in range(p, q + 1):
        resultado = calcular_collatz(i)
        print("n={0}: {1}".format(i, resultado))
        
    print("Demostrado...\n")

# ==========================================
# Zona de Pruebas y Demostracion (Ejecucion directa)
# ==========================================

print("--- PRUEBA: Demostracion aplicando la regla (p=1, q=100) ---")
demostracion_collatz(1, 100)