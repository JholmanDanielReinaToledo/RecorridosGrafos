from tkinter import messagebox

from nodo import nodo_class
import general

class algoritmo_BPA:

    def __init__(self, puzzle_inicial, puzzle_final):
        self.inicial = nodo_class(None, puzzle_inicial.copy(), "")
        self.fin = puzzle_final.copy()
        self.lista_abierto = [self.inicial]
        self.lista_cerrado = []
        self.iniciar()

    def iniciar(self):
        contador = 0
        while len(self.lista_abierto) > 0:
            #print("primera", contador)
            contador = contador + 1
            nodo = self.lista_abierto[0]
            print(len(self.lista_cerrado))
            self.lista_abierto.pop(0)
            if not general.nodo_en_lista_cerrado(self.lista_cerrado, nodo):
                self.lista_cerrado.append(nodo)
                sucesores = general.obtener_sucesores(nodo)

                print("Nodo")
                general.imprimir_bonito(nodo.get_puzzle())  # esto es un print
                print("")
                print("Sucesores")
                for i in sucesores:
                    print(i.get_regla_aplicada())
                    general.imprimir_bonito(i.get_puzzle())
                    print("")


                if len(sucesores) > 0 and not general.validar_puzzle_en_nodos(sucesores, self.fin.copy()):
                    for nod in sucesores:
                        #if general.validar_puzzle_en_nodos(sucesores)
                        self.lista_abierto.append(nod)
                        #print("metio uno a sucesores")
                elif len(sucesores) == 0:
                    print("No hay sucesores")
                elif general.validar_puzzle_en_nodos(sucesores, self.fin.copy()):
                    self.nodo_final = general.validar_puzzle_en_nodos(sucesores, self.fin)
                    break
        if self.nodo_final:
            messagebox.showinfo(title="Exito", message="Exito, nodo encontrado")
            print(self.nodo_final.get_puzzle())

lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]

lista2 = [
    1, 2, 3, 4, 0, 6, 7, 8, 5
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


algoritmo_BPA(lista1, lista3)

