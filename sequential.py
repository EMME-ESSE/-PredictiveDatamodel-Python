# This function performs sequential search in a list to find all occurrences of a given value.
# lista is the list of numbers to search in.
# z is the value to be searched for.
# Returns a list of positions where the value z is found in the lista.
def sequential_search(lista, z):
    posiciones = []
    for i, n in enumerate(lista):
        if n == z:
            posiciones.append(i)
    return posiciones

lista = [10, 4, 23, 12, 40, 31 ,112, 5, 67, 5, 5, 4, 2]
z = int(input("Ingrese un número: "))
posiciones = sequential_search(lista, z)

print("El número {} se ingresó {} veces y está en las posiciones {}".format(z, len(posiciones), posiciones))
