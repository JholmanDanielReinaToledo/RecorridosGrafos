class nodo_class:

    def __init__(self, padre, puzzle, regla):
        self.set_puzzle(puzzle)
        self.heuristica = 0
        self.informacion = 0
        self.set_padre(padre)
        self.hijos = list()
        self.set_regla_aplicada(regla)

    def set_regla_aplicada(self, regla):
        self.regla = regla

    def get_regla_aplicada(self):
        return self.regla

    def set_hijo(self, hijo):
        self.hijos.append(hijo)

    def set_padre(self, padre):
        self.padre: nodo_class = padre

    def get_padre(self):
        return self.padre

    def get_hijos(self):
        return self.hijos

    def set_puzzle(self, puzzle):
        self.puzzle = puzzle

    def get_puzzle(self):
        return self.puzzle

    def set_profundidad(self, profundidad):
        self.profundidad = profundidad

    def get_profundidad(self):
        return self.profundidad

    def set_heuristica(self, heuristica):
        self.heuristica = heuristica

    def get_heuristica(self):
        return self.heuristica

    def set_informacion(self, informacion):
        self.informacion = informacion

    def get_informacion(self):
        return self.informacion