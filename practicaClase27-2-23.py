# Lists
# La idea es la de agrupar variables, elementos

fruta1 = 'manzana'
fruta2 = 'pera'
fruta3 = 'banana'

# Este sería el agrupamiento, o en su defecto declarar
# el valor dentro de los corchetes
frutas = [fruta1, fruta2, fruta3]


# Supongamos importamos una fila de excel:
line = 'Manzana, 200, 390.10'
fila = line.split(', ') # Creamos un array del string
print(fila)
print(type(fila))

# Creamos un array vacío
cesta = []

# Puedo hacer uso del append como en un array:
cesta.append(fila)
cesta.append(['Pera', '200', '10'])

print(cesta)

# Chequear si un elemento está en una lista:
print('Pera' in cesta) # Esto devuelve falso porque no chequea dentro de los otros arrays

# Podemos hacer uso de f string:
for i in cesta:
    mostrar = f'El costo para {i[0]} es de {i[2]}. Total de stock: {i[1]}'
    print(mostrar)
    # El primero devuelve False
    print('Pera' in i)



# el poder de for
for x in range(-3, 3): # Esto devuelve -3 hasta 2. Porque considera a 0 como número
    print(x)


# el uso de while:
i = 0
# Bloquea el avance del código hasta que cierre el bucle
while i < 5:
    print(i)
    i = i+1
