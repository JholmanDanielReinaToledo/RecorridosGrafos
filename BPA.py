from tkinter import messagebox

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
        contador = 0
        while len(self.lista_abierto) > 0:
            print(contador)
            contador = contador + 1
            nodo = self.lista_abierto[0]
            self.lista_abierto.pop(0)
            if not general.nodo_en_lista(self.lista_cerrado, nodo): #Verificar toda la rama hacia el padre que no este repetido
                self.lista_cerrado.append(nodo)
                sucesores = general.obtener_sucesores(nodo)
                if len(sucesores) > 0 and not general.validar_puzzle_en_nodos(sucesores, self.fin):
                    for nod in sucesores:
                        self.lista_abierto.append(nod)
                if general.validar_puzzle_en_nodos(sucesores, self.fin):
                    self.nodo_final = general.validar_puzzle_en_nodos(sucesores, self.fin)
                    break
        if self.nodo_final:
            messagebox.showinfo(title="Exito")
            print(self.nodo_final.get_puzzle())

lista1 = [
    1, 2, 3, 4, 5, 6, 7, 0, 8
]

lista2 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]
#nodoP1 = nodo_class(None, lista1, "asd")

#sucesores = general.obtener_sucesores(nodoP1)

#for i in sucesores:
#    general.imprimir_bonito(i.get_puzzle())
#    print("")

#response = general.validar_puzzle_en_nodos([nodoP1], lista1)

#print(response)

algoritmo_BPA(lista1, lista2)


#nodoP2 = nodo_class(None, lista1, "asd")


#nodo1 = nodo_class(nodoP1, lista1, "fgh")
#nodo2 = nodo_class(nodoP1, lista1, "fgh")

#nodoP1.set_hijo(nodo1)



#print(nodo1)
#print(nodo2)

#response = general.validar_nodos_iguales(nodo1, nodo2)
#print(response)