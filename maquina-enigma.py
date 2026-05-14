import string

# Nos retorna el alfabeto por defecto
alfabeto = string.ascii_uppercase

#Rotor que nos permitira cifrar nuestro mensaje
rotor = "BCDEFGHIJKLMNOPQRSTUVWXYZA"

def cifrar_letra(letra, posicion, clave, operacion):
    if letra not in alfabeto:
        return letra

    idx = alfabeto.index(letra)

    # aplicar operación con la clave
    if operacion == "+":
        idx = idx + posicion + clave
    elif operacion == "-":
        idx = idx + posicion - clave
    elif operacion == "*":
        idx = (idx + posicion) * clave
    else:
        idx = idx + posicion  # sin clave

    idx = idx % 26  # mantener dentro del alfabeto

    return rotor[idx]


def enigma(mensaje, clave, operacion):
    resultado = ""
    posicion = 0

    for letra in mensaje.upper():
        cifrada = cifrar_letra(letra, posicion, clave, operacion)
        resultado += cifrada

        # girar el rotor +1 posicion para generar el cifrado
        posicion = (posicion + 1) % 26

    return resultado


mensaje = input("Escribe el mensaje a cifrar: ")
usar_clave = input("¿Quieres usar clave secreta? (si/no): ")

if usar_clave.lower() == "si":
    clave = int(input("Ingresa un número como clave secreta: "))
    operacion = input("Elige operación (+, -, *): ")
else:
    clave = 0
    operacion = "+"


# Retornar el mensaje ya correctamente cifrado
cifrado = enigma(mensaje, clave, operacion)

print("Mensaje cifrado:", cifrado)