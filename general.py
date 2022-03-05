import pydash as py

def validar_puzzle(puzzle):
    duplicados = py.duplicates(puzzle)
    if len(puzzle) != 9:
        return False
    else:
        if len(duplicados) == 0:
            return True
        else:
            return False

lista1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0
]

print(validar_puzzle(lista1))
