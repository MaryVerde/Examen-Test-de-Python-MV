lista = []
total = int(input("Total de Jugadores: "))
i = 1

while(total > 0):
    puntuación = int(input("Puntuación Jugador  " + str(i) + " : "))
    lista.append(puntuación)
    i = i + 1
    total = total - 1
def maximo(lista):
    ganador = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > ganador:
            ganador = lista[i]
    return ganador
print("Puntuación Maxima: ", maximo(lista))

ultimo = lista[-1]
print('Puntuación del Ultimo Jugador: ', ultimo)
for i in range(1, len(lista)) :
    lista.sort(reverse=True)
print("Puntuación mas Altas:", lista[0:3])