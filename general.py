
def validar_puzzle(puzzle):

    print(puzzle)

    flat_list = []
    original_list = [[1, 2], [3, 4]]
    for l in puzzle:
        for item in l:
            flat_list.append(item)
    print(flat_list)



lista1 = [[
    1,2,3
],[
    4,5,6
],[
    7,8,0
]]

validar_puzzle(lista1)