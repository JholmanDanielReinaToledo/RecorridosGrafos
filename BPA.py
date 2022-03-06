import reglas
from nodo import nodo_class
import general

class algoritmo_BPA:

    def __init__(self, puzzle_inicial, puzzle_final):
        self.inicial = nodo_class(None, puzzle_inicial, "")
        self.fin = puzzle_final
        self.lista_abierto = [self.inicial]
        self.lista_cerrado = []
        self.iniciar()

    def iniciar(self):
        while len(self.lista_abierto) > 0:
            nodo = self.lista_abierto[0]
            self.lista_abierto.pop(0)
            if not general.nodo_en_lista(self.lista_cerrado, nodo):
                self.lista_cerrado.append(nodo)
                self.obtener_sucesores(nodo)


    def obtener_sucesores(self, nodo: nodo_class):
        sucesores = list()

        for i in range(4):
            if i == 0:
                puzzle = reglas.mover_0_derecha(nodo.get_puzzle())
                if puzzle:
                    if general.validar_puzzle(puzzle):
                        nuevo_nodo = nodo_class(nodo, puzzle, "mover 0 derecha")
                        sucesores.append(nuevo_nodo)
            if i == 1:
                puzzle = reglas.mover_0_abajo(nodo.get_puzzle())
                if puzzle:
                    if general.validar_puzzle(puzzle):
                        nuevo_nodo = nodo_class(nodo, puzzle, "mover 0 abajo")
                        sucesores.append(nuevo_nodo)
            if i == 2:
                puzzle = reglas.mover_0_izquierda(nodo.get_puzzle())
                if puzzle:
                    if general.validar_puzzle(puzzle):
                        nuevo_nodo = nodo_class(nodo, puzzle, "mover 0 izquierda")
                        sucesores.append(nuevo_nodo)
            if i == 3:
                puzzle = reglas.mover_0_arriba(nodo.get_puzzle())
                if puzzle:
                    if general.validar_puzzle(puzzle):
                        nuevo_nodo = nodo_class(nodo, puzzle, "mover 0 arriba")
                        sucesores.append(nuevo_nodo)

        print(sucesores)


lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]
nodoP1 = nodo_class(None, lista1, "asd")

algoritmo_BPA(lista1, lista1)




#nodoP2 = nodo_class(None, lista1, "asd")


#nodo1 = nodo_class(nodoP1, lista1, "fgh")
#nodo2 = nodo_class(nodoP1, lista1, "fgh")

#nodoP1.set_hijo(nodo1)



#print(nodo1)
#print(nodo2)

#response = general.validar_nodos_iguales(nodo1, nodo2)
#print(response)