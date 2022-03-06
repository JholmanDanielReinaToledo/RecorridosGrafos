import pydash as py
from nodo import nodo_class

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

