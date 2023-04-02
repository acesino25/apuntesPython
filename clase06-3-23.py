# iterar key y valor de un diccionario

diccionario = {
    'Valor': 1,
    'ELemento': 2
}

# Podemos iterar sobre el diccionario, un objeto
# y obtener el key y los datos con
# el method items()
for item in diccionario.items():
    # Imprimimos lo que devuelve .items
    print(item)
    # el tipo de dato devuelto es una tupla, lo que significa que 
    print(type(item))
    # Y yo de la tupla puedo hacer uso de unpackage:
    a, b = item
    print(a)
    print(b)