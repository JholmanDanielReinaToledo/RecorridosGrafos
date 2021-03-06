from tkinter import messagebox

import copy
from nodo import nodo_class
import general

class algoritmo_BPA:

    def __init__(self, puzzle_inicial, puzzle_final):
        self.inicial = nodo_class(None, puzzle_inicial.copy(), "")
        self.fin = puzzle_final.copy()
        self.lista_abierto = [self.inicial]
        self.lista_cerrado = []

    def iniciar(self):
        contador = 0
        while len(self.lista_abierto) > 0:
            contador = contador + 1
            nodo = self.lista_abierto[0]
            self.lista_abierto.pop(0)
            if not general.nodo_en_lista_cerrado(self.lista_cerrado, nodo):
                self.lista_cerrado.append(nodo)
                sucesores = general.obtener_sucesores(nodo)
                if len(sucesores) > 0 and not general.validar_puzzle_en_nodos(sucesores, self.fin.copy()):
                    for nod in sucesores:
                        self.lista_abierto.append(nod)
                elif len(sucesores) == 0:
                    pass
                elif general.validar_puzzle_en_nodos(sucesores, self.fin.copy()):
                    self.nodo_final = general.validar_puzzle_en_nodos(sucesores, self.fin)
                    break
        if self.nodo_final:
            messagebox.showinfo(title="Exito", message="Exito, nodo encontrado")
            return self.get_nodo_final(self.nodo_final), self.get_nodos_generados(self.lista_cerrado), len(self.lista_cerrado)
        else:
            return False

    def get_nodo_final(self, nodo: nodo_class):
        lista = []
        lista.append(nodo.get_regla_aplicada())
        nodo = copy.deepcopy(nodo)
        while nodo.get_padre():
            nodo = copy.deepcopy(nodo.get_padre())
            lista.append(nodo.get_regla_aplicada())
        return lista

    def get_nodos_generados(self, lista):
        texto = ""
        contador = 0
        for nodo in lista:
            contador = contador + 1
            texto = texto + "Nodo: " + str(contador) + "\n"
            texto = texto + general.imprimir_puzzle(nodo.get_puzzle())
            texto = texto + "\n"

        return texto


'''lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]

lista2 = [
    1, 2, 3, 4, 5, 0, 7, 8, 6
]

lista3 = [
    6, 2, 5, 4, 3, 0, 1, 7, 8
]


nodoP1A = nodo_class(None, lista1.copy(), "asd")
nodoP1B = nodo_class(None, lista1.copy(), "asd")

nodoP2A = nodo_class(nodoP1A, lista2.copy(), "asd")
nodoP2B = nodo_class(nodoP1B, lista2.copy(), "asd")

nodoP3A = nodo_class(nodoP2A, lista3.copy(), "asd")
nodoP3B = nodo_class(nodoP2B, lista3.copy(), "asd")

nodoP4A = nodo_class(nodoP3A, lista2.copy(), "asd")
nodoP4B = nodo_class(nodoP3B, lista2.copy(), "asd")

#respose = general.validar_padres(nodoP4A, nodoP4B)
#print(respose)


algoritmo_BPA(lista1, lista2)
'''
