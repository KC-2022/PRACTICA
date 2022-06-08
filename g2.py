from FUNCIONES.cartel import cartel
from FUNCIONES.ing2i import ing2i
from FUNCIONES.ing2s import ing2s
from FUNCIONES.suma import suma
from FUNCIONES.resta import resta
from FUNCIONES.producto import producto
from FUNCIONES.cociente import cociente
from FUNCIONES.modulo import modulo
from FUNCIONES.potencia import potencia
from FUNCIONES.radicacion import radicacion
from FUNCIONES.p1suma import p1sum
from FUNCIONES.p1produc import p1produc
from FUNCIONES.p1rest import p1rest
from FUNCIONES.genrnd import genrnd
from FUNCIONES.media import media
from FUNCIONES.mediana import median
from FUNCIONES.sumgenrnd import sumgenr
print(cartel())

enteros= ing2i()
print("Enteros ingresados: ", enteros[0], "y", enteros[1])
print("Suma de Enteros: ", suma(enteros[0],enteros[1]))
print("Resta de Enteros: ", resta(enteros[0],enteros[1]))
print("Producto de Enteros: ", producto(enteros[0],enteros[1]))
print("Cociente de Enteros: ", cociente(enteros[0],enteros[1]))
print("Modulo de Enteros: ", modulo(enteros[0],enteros[1]))
print("Potencia de Enteros: ", potencia(enteros[0],enteros[1]))
print("Radicacion de Enteros: ", radicacion(enteros[0],enteros[1]))
print("El producto de los 2 parametros mas el tercero es: ", p1produc(enteros[0],enteros[1],int(input("Ingrese Tercer parametro: "))))
print("La suma de los 2 parametros más el tercero es: ", p1sum(enteros[0],enteros[1],int(input("Ingrese Tercer parametro: "))))
print("La resta de los parametros por el tercero es:  ", p1rest(enteros[0],enteros[1],int(input("Ingrese Tercer parametro: "))))

print("Numeros aleatorios: ", genrnd())

print("suma aleatorios: ", sumgenr())

print("Media de Los Numeros aleatorios: ", media())
print("Mediana de Los Numeros aleatorios: ", median())
cadenas = ing2s()
print('Los strings intresados son: ', cadenas[0], "y", cadenas[1])
