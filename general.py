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
    iguales = False
    for nod in lista:
        if validar_padres(nod, nodo):
            iguales = True

    return iguales

def nodo_en_lista_cerrado(lista, nodo: nodo_class):
    for i in lista:
        if i.get_puzzle() == nodo.get_puzzle():
            return True
    return False

def validar_puzzle_en_nodos(lista, puzzle):
    for nodo in lista:
        if nodo.get_puzzle() == puzzle:
            return nodo
    return False

def validar_padres(nodo1: nodo_class, nodo2: nodo_class):
    es_igual = False
    if(nodo1.get_puzzle() == nodo2.get_puzzle()):
        nodo_padre1 = nodo1.get_padre()
        nodo_padre2 = nodo2.get_padre()
        if nodo_padre1 and nodo_padre2:
            while nodo_padre1 and nodo_padre2:
                if nodo_padre1.get_puzzle() == nodo_padre2.get_puzzle():
                    if nodo_padre1.get_padre() and nodo_padre2.get_padre():
                        nodo_padre1 = nodo_padre1.get_padre()
                        nodo_padre2 = nodo_padre2.get_padre()
                        if nodo_padre1.get_puzzle() == nodo_padre2.get_puzzle():
                            es_igual = True
                        else:
                            return False
                    else:
                        if nodo_padre1.get_padre() == None and nodo_padre2.get_padre() == None:
                            return True
                        else:
                            return False
                else:
                    return False
        else:
            if nodo_padre1 == None and nodo_padre2 == None:
                return True
            else:
                return False
    else:
        return False

    return es_igual

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
    for i in range(4):
        if i == 0:
            puzzle1 = reglas.mover_0_derecha(nodo.get_puzzle().copy())
            if puzzle1:
                if validar_puzzle(puzzle1):
                    nuevo_nodo = nodo_class(nodo, puzzle1, "mover 0 derecha")
                    sucesores.append(nuevo_nodo)
        if i == 1:
            puzzle2 = reglas.mover_0_abajo(nodo.get_puzzle().copy())
            if puzzle2:
                if validar_puzzle(puzzle2):
                    nuevo_nodo = nodo_class(nodo, puzzle2, "mover 0 abajo")
                    sucesores.append(nuevo_nodo)
        if i == 2:
            puzzle3 = reglas.mover_0_izquierda(nodo.get_puzzle().copy())
            if puzzle3:
                if validar_puzzle(puzzle3):
                    nuevo_nodo = nodo_class(nodo, puzzle3, "mover 0 izquierda")
                    sucesores.append(nuevo_nodo)
        if i == 3:
            puzzle4 = reglas.mover_0_arriba(nodo.get_puzzle().copy())
            if puzzle4:
                if validar_puzzle(puzzle4):
                    nuevo_nodo = nodo_class(nodo, puzzle4, "mover 0 arriba")
                    sucesores.append(nuevo_nodo)
    return sucesores