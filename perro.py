class Perro():
    #creo la funcion constructora
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
     
    #creo la funcion ladrar 
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("Guau, guau")
            
salchicho = Perro("Salchicho", 3, 12)
lola = Perro("Lola", 8, 1.5)
miko = Perro("Miko", 8, 3)

salchicho.ladrar()
lola.ladrar()
        
        