
def contar_palabras(ruta_archivo):

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    palabras = texto.lower().split()
    total_palabras = len(palabras)
    total_caracteres = len(texto.replace("\n", ""))

    print(f"total palabras {total_palabras}")
    print(f"total caracteres {total_caracteres} \n")

    conteo = {}
    for palabra in palabras:
        
        if palabra in conteo:
            conteo[palabra] = conteo[palabra] + 1
        else:
            conteo[palabra] = 1

    # Ordenar con Merge Sort
    lista = []
    for palabra in conteo:
        lista.append((palabra, conteo[palabra]))

    ordenadas = merge_sort(lista)
    for palabra, cantidad in ordenadas:
        print(palabra + ": " + str(cantidad))

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2

    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][1] >= derecha[j][1]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado += izquierda[i:]
    resultado += derecha[j:]

    return resultado


if __name__ == "__main__":
    contar_palabras("texto_prueba.txt")