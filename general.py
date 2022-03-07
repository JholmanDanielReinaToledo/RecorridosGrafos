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
                contador = contador + 1
            print("")
    else:
        print("No se puede imprimir")

def imprimir_puzzle(puzzle):
    if puzzle:
        contador = 0
        texto = ""
        for elemnto in range(3):
            for elemnto2 in range(3):
                texto = texto + str(puzzle[contador])
                contador = contador + 1
            texto = texto + "\n"
        return texto
    else:
        return "No se puede imprimir"

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

def calcular_1(posicion1: int, posicion2: int):
    if posicion1 == 0:
        if posicion2 == 0:
            return 0
        if posicion2 == 1:
            return 1.1
        if posicion2 == 2:
            return 2.2
        if posicion2 == 3:
            return 1.1
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 3.3
        if posicion2 == 6:
            return 2.2
        if posicion2 == 7:
            return 3.3
        if posicion2 == 8:
            return 4.4
    if posicion1 == 1:
        if posicion2 == 0:
            return 1.1
        if posicion2 == 1:
            return 0
        if posicion2 == 2:
            return 1.1
        if posicion2 == 3:
            return 2.2
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 2.2
        if posicion2 == 6:
            return 3.3
        if posicion2 == 7:
            return 2.2
        if posicion2 == 8:
            return 3.3
    if posicion1 == 2:
        if posicion2 == 0:
            return 2.2
        if posicion2 == 1:
            return 1.1
        if posicion2 == 2:
            return 0
        if posicion2 == 3:
            return 3.3
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 1.1
        if posicion2 == 6:
            return 4.4
        if posicion2 == 7:
            return 3.3
        if posicion2 == 8:
            return 2.2
    if posicion1 == 3:
        if posicion2 == 0:
            return 1.1
        if posicion2 == 1:
            return 2.2
        if posicion2 == 2:
            return 3.3
        if posicion2 == 3:
            return 0
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 2.2
        if posicion2 == 6:
            return 1.1
        if posicion2 == 7:
            return 2.2
        if posicion2 == 8:
            return 3.3
    if posicion1 == 4:
        if posicion2 == 0:
            return 2.2
        if posicion2 == 1:
            return 1.1
        if posicion2 == 2:
            return 2.2
        if posicion2 == 3:
            return 1.1
        if posicion2 == 4:
            return 0
        if posicion2 == 5:
            return 1.1
        if posicion2 == 6:
            return 2.2
        if posicion2 == 7:
            return 1.1
        if posicion2 == 8:
            return 2.2
    if posicion1 == 5:
        if posicion2 == 0:
            return 3.3
        if posicion2 == 1:
            return 2.2
        if posicion2 == 2:
            return 1.1
        if posicion2 == 3:
            return 2.2
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 0
        if posicion2 == 6:
            return 3.3
        if posicion2 == 7:
            return 2.2
        if posicion2 == 8:
            return 1.1
    if posicion1 == 6:
        if posicion2 == 0:
            return 2.2
        if posicion2 == 1:
            return 3.3
        if posicion2 == 2:
            return 4.4
        if posicion2 == 3:
            return 1.1
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 3.3
        if posicion2 == 6:
            return 0
        if posicion2 == 7:
            return 1.1
        if posicion2 == 8:
            return 2.2
    if posicion1 == 7:
        if posicion2 == 0:
            return 3.3
        if posicion2 == 1:
            return 2.2
        if posicion2 == 2:
            return 3.3
        if posicion2 == 3:
            return 2.2
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 2.2
        if posicion2 == 6:
            return 1.1
        if posicion2 == 7:
            return 0
        if posicion2 == 8:
            return 1.1
    if posicion1 == 8:
        if posicion2 == 0:
            return 4.4
        if posicion2 == 1:
            return 3.3
        if posicion2 == 2:
            return 2.2
        if posicion2 == 3:
            return 3.3
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 1.1
        if posicion2 == 6:
            return 2.2
        if posicion2 == 7:
            return 1.1
        if posicion2 == 8:
            return 0

def calcular_1(posicion1: int, posicion2: int):
    if posicion1 == 0:
        if posicion2 == 0:
            return 0
        if posicion2 == 1:
            return 1.1
        if posicion2 == 2:
            return 2.2
        if posicion2 == 3:
            return 1.1
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 3.3
        if posicion2 == 6:
            return 2.2
        if posicion2 == 7:
            return 3.3
        if posicion2 == 8:
            return 4.4
    if posicion1 == 1:
        if posicion2 == 0:
            return 1.1
        if posicion2 == 1:
            return 0
        if posicion2 == 2:
            return 1.1
        if posicion2 == 3:
            return 2.2
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 2.2
        if posicion2 == 6:
            return 3.3
        if posicion2 == 7:
            return 2.2
        if posicion2 == 8:
            return 3.3
    if posicion1 == 2:
        if posicion2 == 0:
            return 2.2
        if posicion2 == 1:
            return 1.1
        if posicion2 == 2:
            return 0
        if posicion2 == 3:
            return 3.3
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 1.1
        if posicion2 == 6:
            return 4.4
        if posicion2 == 7:
            return 3.3
        if posicion2 == 8:
            return 2.2
    if posicion1 == 3:
        if posicion2 == 0:
            return 1.1
        if posicion2 == 1:
            return 2.2
        if posicion2 == 2:
            return 3.3
        if posicion2 == 3:
            return 0
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 2.2
        if posicion2 == 6:
            return 1.1
        if posicion2 == 7:
            return 2.2
        if posicion2 == 8:
            return 3.3
    if posicion1 == 4:
        if posicion2 == 0:
            return 2.2
        if posicion2 == 1:
            return 1.1
        if posicion2 == 2:
            return 2.2
        if posicion2 == 3:
            return 1.1
        if posicion2 == 4:
            return 0
        if posicion2 == 5:
            return 1.1
        if posicion2 == 6:
            return 2.2
        if posicion2 == 7:
            return 1.1
        if posicion2 == 8:
            return 2.2
    if posicion1 == 5:
        if posicion2 == 0:
            return 3.3
        if posicion2 == 1:
            return 2.2
        if posicion2 == 2:
            return 1.1
        if posicion2 == 3:
            return 2.2
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 0
        if posicion2 == 6:
            return 3.3
        if posicion2 == 7:
            return 2.2
        if posicion2 == 8:
            return 1.1
    if posicion1 == 6:
        if posicion2 == 0:
            return 2.2
        if posicion2 == 1:
            return 3.3
        if posicion2 == 2:
            return 4.4
        if posicion2 == 3:
            return 1.1
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 3.3
        if posicion2 == 6:
            return 0
        if posicion2 == 7:
            return 1.1
        if posicion2 == 8:
            return 2.2
    if posicion1 == 7:
        if posicion2 == 0:
            return 3.3
        if posicion2 == 1:
            return 2.2
        if posicion2 == 2:
            return 3.3
        if posicion2 == 3:
            return 2.2
        if posicion2 == 4:
            return 1.1
        if posicion2 == 5:
            return 2.2
        if posicion2 == 6:
            return 1.1
        if posicion2 == 7:
            return 0
        if posicion2 == 8:
            return 1.1
    if posicion1 == 8:
        if posicion2 == 0:
            return 4.4
        if posicion2 == 1:
            return 3.3
        if posicion2 == 2:
            return 2.2
        if posicion2 == 3:
            return 3.3
        if posicion2 == 4:
            return 2.2
        if posicion2 == 5:
            return 1.1
        if posicion2 == 6:
            return 2.2
        if posicion2 == 7:
            return 1.1
        if posicion2 == 8:
            return 0

def calcular_informacion_solop(posicion1: int, posicion2: int):
    if posicion1 == 0:
        if posicion2 == 0:
            return 5
        if posicion2 == 1:
            return 4
        if posicion2 == 2:
            return 3
        if posicion2 == 3:
            return 4
        if posicion2 == 4:
            return 3
        if posicion2 == 5:
            return 2
        if posicion2 == 6:
            return 3
        if posicion2 == 7:
            return 2
        if posicion2 == 8:
            return 1
    if posicion1 == 1:
        if posicion2 == 5:
            return 4
        if posicion2 == 1:
            return 5
        if posicion2 == 2:
            return 4
        if posicion2 == 3:
            return 3
        if posicion2 == 4:
            return 4
        if posicion2 == 5:
            return 3
        if posicion2 == 6:
            return 2
        if posicion2 == 7:
            return 3
        if posicion2 == 8:
            return 2
    if posicion1 == 2:
        if posicion2 == 5:
            return 3
        if posicion2 == 1:
            return 4
        if posicion2 == 2:
            return 5
        if posicion2 == 3:
            return 2
        if posicion2 == 4:
            return 3
        if posicion2 == 5:
            return 4
        if posicion2 == 6:
            return 1
        if posicion2 == 7:
            return 2
        if posicion2 == 8:
            return 3
    if posicion1 == 3:
        if posicion2 == 5:
            return 4
        if posicion2 == 1:
            return 3
        if posicion2 == 2:
            return 2
        if posicion2 == 3:
            return 5
        if posicion2 == 4:
            return 4
        if posicion2 == 5:
            return 3
        if posicion2 == 6:
            return 4
        if posicion2 == 7:
            return 3
        if posicion2 == 8:
            return 2
    if posicion1 == 4:
        if posicion2 == 5:
            return 3
        if posicion2 == 1:
            return 4
        if posicion2 == 2:
            return 3
        if posicion2 == 3:
            return 4
        if posicion2 == 4:
            return 5
        if posicion2 == 5:
            return 4
        if posicion2 == 6:
            return 3
        if posicion2 == 7:
            return 4
        if posicion2 == 8:
            return 3
    if posicion1 == 5:
        if posicion2 == 5:
            return 2
        if posicion2 == 1:
            return 3
        if posicion2 == 2:
            return 4
        if posicion2 == 3:
            return 3
        if posicion2 == 4:
            return 4
        if posicion2 == 5:
            return 5
        if posicion2 == 6:
            return 2
        if posicion2 == 7:
            return 3
        if posicion2 == 8:
            return 4
    if posicion1 == 6:
        if posicion2 == 5:
            return 3
        if posicion2 == 1:
            return 2
        if posicion2 == 2:
            return 1
        if posicion2 == 3:
            return 4
        if posicion2 == 4:
            return 3
        if posicion2 == 5:
            return 2
        if posicion2 == 6:
            return 5
        if posicion2 == 7:
            return 4
        if posicion2 == 8:
            return 3
    if posicion1 == 7:
        if posicion2 == 5:
            return 2
        if posicion2 == 1:
            return 3
        if posicion2 == 2:
            return 2
        if posicion2 == 3:
            return 3
        if posicion2 == 4:
            return 4
        if posicion2 == 5:
            return 3
        if posicion2 == 6:
            return 4
        if posicion2 == 7:
            return 5
        if posicion2 == 8:
            return 4
    if posicion1 == 8:
        if posicion2 == 5:
            return 1
        if posicion2 == 1:
            return 2
        if posicion2 == 2:
            return 3
        if posicion2 == 3:
            return 2
        if posicion2 == 4:
            return 3
        if posicion2 == 5:
            return 4
        if posicion2 == 6:
            return 3
        if posicion2 == 7:
            return 4
        if posicion2 == 8:
            return 5

def calcular_informacion(puzzle, puzzle_meta):
    index_0 = puzzle.index(0)
    index_1 = puzzle.index(1)
    index_2 = puzzle.index(2)
    index_3 = puzzle.index(3)
    index_4 = puzzle.index(4)
    index_5 = puzzle.index(5)
    index_6 = puzzle.index(6)
    index_7 = puzzle.index(7)
    index_8 = puzzle.index(8)

    final_0 = puzzle_meta.index(0)
    final_1 = puzzle_meta.index(1)
    final_2 = puzzle_meta.index(2)
    final_3 = puzzle_meta.index(3)
    final_4 = puzzle_meta.index(4)
    final_5 = puzzle_meta.index(5)
    final_6 = puzzle_meta.index(6)
    final_7 = puzzle_meta.index(7)
    final_8 = puzzle_meta.index(8)

    peso = 0.0
    peso = peso + calcular_informacion_solop(index_0, final_0)
    peso = peso + calcular_informacion_solop(index_1, final_1)
    peso = peso + calcular_informacion_solop(index_2, final_2)
    peso = peso + calcular_informacion_solop(index_3, final_3)
    peso = peso + calcular_informacion_solop(index_4, final_4)
    peso = peso + calcular_informacion_solop(index_5, final_5)
    peso = peso + calcular_informacion_solop(index_6, final_6)
    peso = peso + calcular_informacion_solop(index_7, final_7)
    peso = peso + calcular_informacion_solop(index_8, final_8)

    return peso

def calcular_heuristica(puzzle, puzzle_meta):
    index_0 = puzzle.index(0)
    index_1 = puzzle.index(1)
    index_2 = puzzle.index(2)
    index_3 = puzzle.index(3)
    index_4 = puzzle.index(4)
    index_5 = puzzle.index(5)
    index_6 = puzzle.index(6)
    index_7 = puzzle.index(7)
    index_8 = puzzle.index(8)

    final_0 = puzzle_meta.index(0)
    final_1 = puzzle_meta.index(1)
    final_2 = puzzle_meta.index(2)
    final_3 = puzzle_meta.index(3)
    final_4 = puzzle_meta.index(4)
    final_5 = puzzle_meta.index(5)
    final_6 = puzzle_meta.index(6)
    final_7 = puzzle_meta.index(7)
    final_8 = puzzle_meta.index(8)

    peso = 0.0
    peso = peso + calcular_1(index_0, final_0)
    peso = peso + calcular_1(index_1, final_1)
    peso = peso + calcular_1(index_2, final_2)
    peso = peso + calcular_1(index_3, final_3)
    peso = peso + calcular_1(index_4, final_4)
    peso = peso + calcular_1(index_5, final_5)
    peso = peso + calcular_1(index_6, final_6)
    peso = peso + calcular_1(index_7, final_7)
    peso = peso + calcular_1(index_8, final_8)

    return peso




'''lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]

lista2 = [
    1, 2, 3, 4, 5, 0, 7, 8, 6
]

lista3 = [
    6, 2, 5, 4, 3, 0, 1, 7, 8
]

print(calcular_heuristica(lista3, lista1))

print(calcular_1(1,2))'''

def ordenamiento_burbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            print("En burbuja")
            if unaLista[i].get_heuristica() < unaLista[i+1].get_heuristica():
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

    return unaLista



