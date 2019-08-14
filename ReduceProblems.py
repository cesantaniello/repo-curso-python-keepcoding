from functools import reduce

def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    resultado
    
def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
        
    return resultado

def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado
    

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)
#creo una copia de la lista
l = lista[:]
#agrego el neutro para la suma en la posicion cero
l.insert(0, 0)
sumatorioDobles = reduce(lambda x, y: x + y*2, 1)

print(sumatorio)
print(sumatorioDobles)