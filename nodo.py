from estructura_puzzle8 import estructura_puzzle

class nodo:

    def __init__(self, padre, puzzle):
        self.set_puzzle(estructura_puzzle(puzzle))
        self.set_padre(padre)
        self.hijos = list

    def set_hijo(self, hijo):
        self.hijos.append(hijo)

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def get_hijos(self):
        return self.hijos

    def set_puzzle(self, puzzle):
        self.puzzle_class = puzzle

    def get_puzzle(self):
        return self.puzzle_class
