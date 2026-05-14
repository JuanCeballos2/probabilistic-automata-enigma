import numpy as np

#Crear las matrices
def crear_matriz(nombre, n_estados):
    print(f"\nIngrese la matriz para símbolo '{nombre}':")
    matriz = []
    
    for i in range(n_estados):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        
        # Validación
        if round(sum(fila), 5) != 1.0:
            print("La suma de la fila debe ser 1")
            return crear_matriz(nombre, n_estados)
        
        matriz.append(fila)
    
    return np.array(matriz)

#Procesar la cadena ingresada
def procesar_cadena(cadena, matrices, P0):
    P = P0.copy()
    
    print("\nProceso paso a paso:")
    
    for simbolo in cadena:
        if simbolo not in matrices:
            print(f"Símbolo '{simbolo}' no definido")
            return
        
        print(f"\nAplicando '{simbolo}':")
        P = np.dot(P, matrices[simbolo])
        print(P)
    
    return P

#input para el usuario
print("AUTÓMATA PROBABILÍSTICO MANUAL")

# Estados
n_estados = int(input("Número de estados: "))

# Nombres de estados (opcional)
estados = []
for i in range(n_estados):
    nombre = input(f"Nombre del estado {i+1}: ")
    estados.append(nombre)

# Símbolos
simbolos = input("Ingrese símbolos (ej: a b): ").split()

# Crear matrices
matrices = {}
for s in simbolos:
    matrices[s] = crear_matriz(s, n_estados)

# Vector inicial
print("\nVector inicial (ej: 1 0 0 0):")
P0 = np.array(list(map(float, input().split())))

# Cadena
cadena = input("\nIngrese la cadena: ")

# Procesar
resultado = procesar_cadena(cadena, matrices, P0)

# Resultado final
print("\nRESULTADO FINAL:")
for i in range(len(estados)):
    print(f"{estados[i]}: {round(resultado[i]*100,2)}%")

# Verificar estado final (último estado)
if resultado[-1] < 0.3:
    print("\nCumple condición (< 0.3)")
else:
    print("\nNo cumple condición (>= 0.3)")