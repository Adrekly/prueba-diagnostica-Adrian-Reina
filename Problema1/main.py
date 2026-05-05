# -*- coding: utf-8 -*-
import re

def analizar_expresion(expresion):
    # 1. Definimos las reglas lexicas (Expresiones Regulares)
    reglas = [
        ('NUMERO',      r'\d+(\.\d+)?'),             # Digitos, opcionalmente seguidos de un punto y mas digitos
        ('OPERANDO',    r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Inicia con letra/guion bajo, seguido de alfanumericos
        ('OPERADOR',    r'[\+\-\*/]'),               # Operadores matematicos basicos
        ('PAREN_IZQ',   r'\('),                      # Parentesis de apertura
        ('PAREN_DER',   r'\)'),                      # Parentesis de cierre
        ('ESPACIO',     r'[ \t]+'),                  # Espacios y tabulaciones (para ignorarlos)
        ('ERROR',       r'.'),                       # Cualquier otro caracter no reconocido
    ]
    
    # Unimos todas las reglas en una unica expresion regular
    regex_tokens = '|'.join('(?P<%s>%s)' % par for par in reglas)
    
    # 2. Variables de control
    resultado = []
    balance_parentesis = 0
    parentesis_ok = True
    
    # 3. Escaneo de la expresion
    for coincidencia in re.finditer(regex_tokens, expresion):
        tipo_token = coincidencia.lastgroup
        valor_token = coincidencia.group(tipo_token)
        
        # Ignoramos los espacios
        if tipo_token == 'ESPACIO':
            continue
            
        # Logica de balance de parentesis
        elif tipo_token == 'PAREN_IZQ':
            balance_parentesis += 1
            resultado.append("{0} {1}".format(tipo_token, valor_token))
            
        elif tipo_token == 'PAREN_DER':
            balance_parentesis -= 1
            if balance_parentesis < 0:
                parentesis_ok = False
            resultado.append("{0} {1}".format(tipo_token, valor_token))
            
        # Para NUMERO, OPERANDO, OPERADOR y ERROR
        else:
            resultado.append("{0} {1}".format(tipo_token, valor_token))
            
    # Validacion final del balance
    if balance_parentesis != 0:
        parentesis_ok = False
        
    mensaje_balance = "PARENTESIS BALANCEADOS." if parentesis_ok else "PARENTESIS DESBALANCEADOS."
    resultado.append(mensaje_balance)
    
    # 4. Retornamos el resultado formateado
    return " ".join(resultado)

# ==========================================
# Zona de Pruebas
# ==========================================
if __name__ == "__main__":
    # Prueba del ejemplo solicitado
    entrada_ejemplo = "12+ 3 * (4)"
    print("Entrada: {0}".format(entrada_ejemplo))
    print("Salida : {0}\n".format(analizar_expresion(entrada_ejemplo)))
    
    # Pruebas extra
    print("Otras pruebas:")
    print(analizar_expresion("VALOR * 3.14 - (A + 2)"))
    print(analizar_expresion("( 5 + 5 ) )"))