from FUNCIONES.genrnd import genrnd

def media():
    lista= genrnd()
    return sum(lista) / len(lista)