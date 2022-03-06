import pydash as py
from nodo import nodo_class
import reglas

def validar_puzzle(puzzle):
    duplicados = py.duplicates(puzzle)
    if len(puzzle) != 9:
        return False
    else:
        for i in puzzle:
            if i > 8 or i < 0:
                return False
        if len(duplicados) == 0:
            return True
        else:
            return False

def validar_nodos_iguales(nodo1: nodo_class, nodo2: nodo_class):
    if nodo1.get_padre() == nodo2.get_padre() and nodo1.get_puzzle() == nodo2.get_puzzle():
        return True
    else:
        return False

def nodo_en_lista(lista, nodo: nodo_class):
    for nod in lista:
        if validar_nodos_iguales(nod, nodo):
            return True
    return False

def validar_puzzle_en_nodos(lista, puzzle):
    for nodo in lista:
        if nodo.get_puzzle() == puzzle:
            return nodo
    return False

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

def obtener_sucesores(nodo: nodo_class):
    sucesores = list()
    responses = list()
    for i in range(4):

        if i == 0:
            puzzle1 = reglas.mover_0_derecha(nodo.get_puzzle().copy())
            #print(puzzle1)
            if puzzle1:
                if validar_puzzle(puzzle1):
                    responses.append(puzzle1)
                    #print(i)
                    #imprimir_bonito(puzzle)
                    nuevo_nodo = nodo_class(nodo, puzzle1, "mover 0 derecha")
                    sucesores.append(nuevo_nodo)
                    #print(nuevo_nodo.get_puzzle())
        if i == 1:
            puzzle2 = reglas.mover_0_abajo(nodo.get_puzzle().copy())
            #print(puzzle2)
            if puzzle2:
                if validar_puzzle(puzzle2):
                    responses.append(puzzle2)
                    #print(i)
                    #imprimir_bonito(puzzle)
                    nuevo_nodo = nodo_class(nodo, puzzle2, "mover 0 abajo")
                    sucesores.append(nuevo_nodo)
                    #print(nuevo_nodo.get_puzzle())
        if i == 2:
            puzzle3 = reglas.mover_0_izquierda(nodo.get_puzzle().copy())
            #print(puzzle3)
            if puzzle3:
                if validar_puzzle(puzzle3):
                    responses.append(puzzle3)
                    #print(i)
                    #imprimir_bonito(puzzle)
                    nuevo_nodo = nodo_class(nodo, puzzle3, "mover 0 izquierda")
                    sucesores.append(nuevo_nodo)
                    #print(nuevo_nodo.get_puzzle())
        if i == 3:
            puzzle4 = reglas.mover_0_arriba(nodo.get_puzzle().copy())
            #print(puzzle4, "Entro")
            if puzzle4:
                if validar_puzzle(puzzle4):
                    responses.append(puzzle4)
                    #print(i)
                    #imprimir_bonito(puzzle)
                    nuevo_nodo = nodo_class(nodo, puzzle4, "mover 0 arriba")
                    sucesores.append(nuevo_nodo)
                    #print(nuevo_nodo.get_puzzle(), "Entro 2")

    #print(responses)


    return sucesores