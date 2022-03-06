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

lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]
nodoP1 = nodo_class(None, lista1, "asd")
nodoP2 = nodo_class(None, lista1, "asd")


nodo1 = nodo_class(nodoP1, lista1, "fgh")
nodo2 = nodo_class(nodoP1, lista1, "fgh")

nodoP1.set_hijo(nodo1)



print(nodo1)
print(nodo2)

response = general.validar_nodos_iguales(nodo1, nodo2)
print(response)