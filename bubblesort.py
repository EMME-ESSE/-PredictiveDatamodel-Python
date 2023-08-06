def bubbleSort(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    return lista

lista = [20, 10, 5, 13, 6, 7]
print(lista)
print(bubbleSort(lista))