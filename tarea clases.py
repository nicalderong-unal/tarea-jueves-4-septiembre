#Autor: Nicolás Alexander Calderón García

## Guía:
# Definición de la clase (repetir para contexto)
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

# Creando objetos
mi_coche = Coche("Ford", "Azul")
otro_coche = Coche("Toyota", "Rojo")

def acelerar(self):
        print(f"El {self.color} {self.marca} está acelerando... ¡Vroom!")

## Tarea:
#Clases
class Perro:
    def __init__(self,nombre,edad,raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    def ladrar(self):
        print(f"{self.nombre}, el perro {self.raza}, está ladrando: ¡Guau!")

class Gato:
    def __init__(self,nombre,edad,raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
    def maullar(self):
        print(f"{self.nombre}, el gato {self.raza}, está maullando: ¡Miau!")

#Asignación de datos
print("\nIngresa los datos del perro:")
nombre_perro=input("Ingrese el nombre del perro: ")
edad_perro=int(input("Ingrese la edad del perro: "))
raza_perro=input("Ingrese la raza del perro: ")
perro=Perro(nombre_perro,edad_perro,raza_perro)

print("\nIngresa los datos del gato:")
nombre_gato=input("Ingrese el nombre del gato: ")
edad_gato=int(input("Ingrese la edad del gato: "))
raza_gato=input("Ingrese la raza del gato: ")
gato=Gato(nombre_gato,edad_gato,raza_gato)

#Acciones animales
print("---------------------")
perro.ladrar()
gato.maullar()