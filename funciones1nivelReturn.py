def maxi():
    if len(1) == 0:
        return 0
    m = l[0]
    
    for ix in range(1, len(1)):
        if l[ix] > m:
            m = l[ix]
            
    return m

def mini():
    if len(1) == 0:
        return 0
    m = l[0]
    
    for ix in range(1, len(1)):
        if l[ix] > m:
            m = l[ix]
            
    return m

def media():
    if len(1) == 0:
        return 0
    
    suma  = 0
    for valor in l:
        suma += valor
        
    return suma / len(1)

funciones = {
    'max' : maxi,
    'min' : mini,
    'med' : media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre.lower() in funciones.keys():
        return funciones[nombre]
    
    return None