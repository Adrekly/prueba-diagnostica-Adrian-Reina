# -*- coding: utf-8 -*-
import re

def validar_fen(cadena):
    # El estandar FEN siempre se compone de 6 campos separados por un espacio
    campos = cadena.split(' ')
    if len(campos) != 6:
        return False, "Estructura invalida: FEN debe tener exactamente 6 campos."
        
    tablero, turno, enroque, peon_paso, medio_mov, mov_completo = campos
    
    # 1. Validar Tablero (Piece placement)
    filas = tablero.split('/')
    if len(filas) != 8:
        return False, "Tablero invalido: Deben existir exactamente 8 filas separadas por '/'."
        
    for fila in filas:
        # Validar caracteres permitidos (Piezas blancas/negras y numeros del 1 al 8)
        if not re.match(r'^[pnbrqkPNBRQK1-8]+$', fila):
            return False, "Tablero invalido: Caracteres no permitidos en la fila '{0}'.".format(fila)
            
        # Validar semantica: la suma de piezas y espacios vacios (numeros) debe ser 8
        suma_casillas = 0
        for caracter in fila:
            if caracter.isdigit():
                suma_casillas += int(caracter) # Si es numero, representa N casillas vacias
            else:
                suma_casillas += 1             # Si es letra, representa 1 pieza
                
        if suma_casillas != 8:
            return False, "Tablero invalido: La fila '{0}' suma {1} casillas en lugar de 8.".format(fila, suma_casillas)
            
    # 2. Validar Turno (Active color)
    if not re.match(r'^[wb]$', turno):
        return False, "Turno invalido: Debe ser 'w' (blancas) o 'b' (negras)."
        
    # 3. Validar Enroque (Castling availability)
    # Puede ser '-' (ninguno) o una combinacion de KQkq
    if not re.match(r'^(-|[KQkq]{1,4})$', enroque):
        return False, "Enroque invalido: Debe ser '-' o combinaciones de 'KQkq'."
        
    # 4. Validar Peon al paso (En passant target square)
    # Puede ser '-' o una coordenada (letra a-h seguida del numero 3 o 6)
    if not re.match(r'^(-|[a-h][36])$', peon_paso):
        return False, "Peon al paso invalido: Debe ser '-' o una coordenada valida (ej. e3, c6)."
        
    # 5. Validar Medio Movimiento (Halfmove clock)
    # Debe ser un numero entero no negativo
    if not re.match(r'^\d+$', medio_mov):
        return False, "Medio movimiento invalido: Debe ser un numero entero positivo."
        
    # 6. Validar Movimiento Completo (Fullmove number)
    # Debe ser un numero entero mayor o igual a 1
    if not re.match(r'^[1-9]\d*$', mov_completo):
        return False, "Mov_completo invalido: Debe ser un numero entero iniciando en 1."
        
    return True, "Cadena valida: Cumple con todos los estandares de la notacion FEN."

# ==========================================
# Zona de Pruebas
# ==========================================
if __name__ == "__main__":
    pruebas = [
        # Posicion inicial valida del ajedrez
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        # FEN Valido despues de e4
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
        # Error: Fila que suma 9 casillas en lugar de 8 (8 + p = 9)
        "rnbqkbnr/pppppppp/8p/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        # Error: Turno invalido ('x')
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR x KQkq - 0 1",
        # Error: Faltan campos (solo hay 5)
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0"
    ]
    
    for i, p in enumerate(pruebas):
        es_valido, mensaje = validar_fen(p)
        print("Prueba {0}:".format(i + 1))
        print("FEN   : {0}".format(p))
        print("Estado: {0} -> {1}\n".format("VALIDO" if es_valido else "INVALIDO", mensaje))