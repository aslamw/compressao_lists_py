forma1 = []
for x in range(10):
    forma1.append(x**2)
    
forma2 = list(map(lambda x: x**2, range(10)))

forma3 = [x**2 for x in range(10)]

print(f'Todos dão o mesmo resultado \n forma1: {forma1} \n forma2: {forma2} \n forma3: {forma3} \n')


# Bonus

menos_linha = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

mais_linha = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            mais_linha.append((x, y))
            
print(f'\n Bonus.: \n menos_linha: {menos_linha} é igual a \n mais_linha: {mais_linha} \n')

#Compreensões de lista aninhadas
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("Compreensões de lista aninhadas:" , [[row[i] for row in matrix] for i in range(4)], ' Extra: ', list(zip(*matrix)))

