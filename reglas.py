import numpy as np
import pydash as py

def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def mover_0_derecha_generic(puzzle, posicion):
    return swap_positions(puzzle, posicion, posicion + 1)

def mover_0_derecha(puzzle):
    posicion = puzzle.index(0)

    if posicion == 2 or posicion == 5 or posicion == 8:
        return False

    return mover_0_derecha_generic(puzzle, posicion)

def mover_0_izq_generic(puzzle, posicion):
    return swap_positions(puzzle, posicion, posicion - 1)

def mover_0_izquierda(puzzle):
    posicion = puzzle.index(0)

    if posicion == 0 or posicion == 3 or posicion == 6:
        return False

    return mover_0_izq_generic(puzzle, posicion)

def mover_arriba_generic(puzzle, posicion):
    return swap_positions(puzzle, posicion, posicion - 3)

def mover_0_arriba(puzzle):
    posicion = puzzle.index(0)
    if posicion == 0 or posicion == 1 or posicion == 2:
        return False

    return mover_arriba_generic(puzzle, posicion)

def mover_abajo_generic(puzzle, posicion):
    return swap_positions(puzzle, posicion, posicion + 3)

def mover_0_abajo(puzzle):
    posicion = puzzle.index(0)
    if posicion == 6 or posicion == 7 or posicion == 8:
        return False

    return mover_arriba_generic(puzzle, posicion)

def imprimir_bonito(puzzle):
    if puzzle:
        contador = 0
        for elemnto in range(3):
            for elemnto2 in range(3):
                print(str(puzzle[contador]) + " ", end="")
                contador = contador+1
            print("")
    else:
        print("No se puede imprimir")

#lista1 = [
#    1, 0, 2, 2, 5, 1, 1, 8, 9
#]

#imprimir_bonito(lista1)
#imprimir_bonito(mover_0_abajo(lista1))
# print(mover_0_derecha(lista1))
# print(mover_0_izquierda(lista1))

