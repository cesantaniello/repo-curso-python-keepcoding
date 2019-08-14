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
            
    #creo el metodo estandar
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}.\n".format(self.nombre, self.edad, self.peso)
    
#Creo la subclase PerroAsistencia que hereda de la clase Padre Perro
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    
    #creo el metodo pasear
    def pasear(self):
        print("Soy {} y ayudo a mi amo, {} a pasear".format(self.nombre, self.amo))
            
salchicho = Perro("Salchicho", 3, 12)
lola = Perro("Lola", 8, 1.5)
miko = Perro("Miko", 8, 3)

rantanplan = PerroAsistencia("Ran Tan Plan", 4, 8, "Lucky Luke")

#print(salchicho, lola, miko) #Muestra caracteristicas de los objetos
#print(rantanplan) #Imrpime mensaje del metodo estandar de la subclase
rantanplan.pasear()
        
        