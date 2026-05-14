import numpy as np
import random

#Generar matriz aleatoria para el caso
def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = np.random.rand(n)
        fila = fila / fila.sum()  # Normaliza para que sume 1
        matriz.append(fila)
    return np.array(matriz)

# Porcesar la cadena ingresas 
def procesar_cadena(cadena, matrices, P0):
    P = P0.copy()
    
    print("\nProceso paso a paso:")
    
    for simbolo in cadena:
        print(f"\nAplicando '{simbolo}':")
        P = np.dot(P, matrices[simbolo])
        print(np.round(P, 3))
    
    return P

#Input para el usuario
print("AUTÓMATA PROBABILÍSTICO AUTOMÁTICO")

n_estados = int(input("Número de estados: "))

# Estados
estados = []
for i in range(n_estados):
    estados.append(input(f"Nombre estado {i+1}: "))

# Símbolos
simbolos = input("Símbolos (ej: a b): ").split()

# Generar matrices automáticamente
matrices = {}
for s in simbolos:
    matrices[s] = generar_matriz(n_estados)

# Mostrar matrices generadas
print("\nMATRICES GENERADAS:")
for s in simbolos:
    print(f"\nMatriz {s}:")
    print(np.round(matrices[s], 2))

# Vector inicial
P0 = np.array(list(map(float, input("\nVector inicial: ").split())))

# Cadena
cadena = input("Cadena: ")

# Procesar
resultado = procesar_cadena(cadena, matrices, P0)

# Resultado final
print("\n RESULTADO FINAL:")
for i in range(len(estados)):
    print(f"{estados[i]}: {round(resultado[i]*100,2)}%")

# Conclusion del ejercicio dependiento de la probabilidad a analizar
if resultado[-1] < 0.3:
    print("\nSistema estable (baja probabilidad de estado crítico)")
else:
    print("\nSistema crítico (alta probabilidad de estado final)")