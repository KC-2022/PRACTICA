from FUNCIONES.genrnd import genrnd

def median():
    lista= genrnd()
    lista.sort()
    # Obtener longitud
    longitud = len(lista)
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (lista[mitad - 1]+lista[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = lista[mitad]
    return mediana