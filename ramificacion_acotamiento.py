from tkinter import messagebox

import copy
from nodo import nodo_class
import general

class algoritmo_ramificacion_acotamiento:

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
                for nodo_su in sucesores:
                    peso = general.calcular_informacion(nodo_su.get_puzzle(), self.fin)
                    nodo_su.set_informacion(peso + nodo.get_informacion())
                if len(sucesores) > 0 and not general.validar_puzzle_en_nodos(sucesores, self.fin.copy()):
                    for nod in sucesores:
                        self.lista_abierto.insert(0, nod)
                    self.lista_abierto = general.ordenamiento_burbuja_asc(self.lista_abierto.copy()).copy()
                elif len(sucesores) == 0:
                    pass
                elif general.validar_puzzle_en_nodos(sucesores, self.fin.copy()):
                    self.nodo_final = general.validar_puzzle_en_nodos(sucesores, self.fin)
                    break
        if self.nodo_final:
            messagebox.showinfo(title="Exito", message="Exito, nodo encontrado")
            return self.get_nodo_final(self.nodo_final), self.get_nodos_generados(self.lista_cerrado), len(self.lista_cerrado)
        else:
            return False, False, False

    def get_nodo_final(self, nodo: nodo_class):
        lista = []
        lista.append(nodo.get_regla_aplicada())
        nodo = copy.deepcopy(nodo)
        while nodo.get_padre():
            nodo = nodo.get_padre()
            lista.append(nodo.get_regla_aplicada())
        return lista

    def get_nodos_generados(self, lista):
        texto = ""
        contador = 0
        for nodo in lista:
            contador = contador + 1
            texto = texto + "Nodo: " + str(contador) + " Información: " + str(nodo.get_informacion()) +"\n"
            texto = texto + general.imprimir_puzzle(nodo.get_puzzle())
            texto = texto + "\n"

        return texto

