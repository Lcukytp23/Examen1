def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
resultado = suma_lista(lista)
print(f"La suma de los elementos de la lista {lista} es {resultado}")
