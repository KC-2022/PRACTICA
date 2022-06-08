from FUNCIONES.genrnd import genrnd

def sumgenr():
    lista= genrnd()
    total= 0
    for i in range(0,len(lista)):
        for j in range(i,len(lista)+1):
            total= lista[i] + lista[j]
            print(total)
    return total
