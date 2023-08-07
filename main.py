
 # Crea una función que sea capaz de leer el número representado por el ábaco.
 # - El ábaco se representa por un array con 7 elementos.
 # - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 #   para las cuentas y una secuencia de "---" para el alambre.
 # - El primer elemento del array representa los millones, y el último las unidades.
 # - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 #
 # Ejemplo de array y resultado:
 # ["O---OOOOOOOO",
 #  "OOO---OOOOOO",
 #  "---OOOOOOOOO",
 #  "OO---OOOOOOO",
 #  "OOOOOOO---OO",
 #  "OOOOOOOOO---",
 #  "---OOOOOOOOO"]
 #  
 # Resultado: 1.302.790

numero = int(input('Escribe un número de máximo 7 cifras: '))
if numero < 10000000:
    numero = str(numero)
    abaco = [0] * 7
    rec = 6
    abacoDib = [""] * 7

    # Asignar el número introducido en la lista para definir el ábaco
    for x in range(len(numero)-1, -1, -1):
        abaco[rec] = int(numero[x])
        rec -= 1

    # Guardamos los strings para dibujar el ábaco
    for i in range(7):
        if abaco[i] > 0:
            for j in range(abaco[i]):
                abacoDib[i] += "0"
            abacoDib[i] += "---"
            for j in range(9-abaco[i]):
                abacoDib[i] += "0"
        else:
            abacoDib[i] = "---000000000"

    # Imprimimos el ábaco
    for i in range(7):
        print(abacoDib[i])