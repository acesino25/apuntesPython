# Endscape
#'\n'    # Salto de linea
#'\r'    # Retorno de carro, es una diferencia obsoleta. Habla de diferentes manejos del pasado
         # Windows xp entre otros sistemas operativos, que indican saltos de línea o acción de salto de línea con enter
#'\t'    # Tabulador
#'\''    # Comilla Simple literal
#'\"'    # Comilla doble literal
#'\\'    # Barra invertida Literal

s = '\U0001D120'    # Código unicode usa la barra invertida
print(s)            # Imprime la clave de sol 



# String como cadena de caracteres igual a C

a = 'Hola mundo'
print(a[0])     # Imprime H

# Pero son inmutables los valores de sus índices

'''
Esto daría error
a[0] = 'h'
print(a)'''

# Para acceder al último elemento recuerda que podemos usar el índice negativo:
print(a[-1])    # Imprime 'o'

# Puedes acceder a un grupo de caracteres por rango:

rango = a[0:4]  # Incluyendo el espacio
print(rango)

# Algo raro con valor negativo:
rango = a[-5:]  # Sobre entiende 0
print(rango)

# Usando positivos implica desde el final o desde el principio:
rango = a[:5]
print(rango)

rango = a[0:]
print(rango)



# Concatenación
# Usando +

a = 'Hola' + 'mundo'
print(a)

# Usamos len() para encontrar el tamaño de a SIN contar 0:
print(len(a))

# 'in' y 'not in' es una manera de chequear si algo se encuentra en algo
# y devuelve un true or false
t = 'e' in a        # Devuelve False porque no hay tal valor
print(t)
e = 'a' in a        # Devuelve True porque hay tal valor
print(e)
t = 'e' not in a    # Devuelve True porque no existe tal valor
print(t)


# Podemos repetir una serie de strings con el * y almacenarlos:
a = 'Multiplicame '*5
print(a)


# strip() un método para eliminar espacios
a = ' Espacios al final y al principio '
b = a + ' hola'
print(b)
a = a.strip()
print(a)
b = a + ' hola'
print(b)

# Si necesitamos mayúsculas o minúsculas podemos usar
# upper() o lower()
a = a.lower()
print(a)
b = b.upper()
print(b)

# No MUTAS el array original por lo que debes almacenar el resultado
# del método


# Podemos reemplazar con el método
# replace('reemplazar', 'por esto')
a = 'Hola mundo'
b = a.replace('Hola', 'Hello')
print(b)

'''
OTROS MÉTODOS:

endswith    Termina con x sufijo
startswith  Comienza con x sufijo
find        Primera aparición de x caracter que determinemos, devuelve -1 si no está
index       Primera aparición de x caracter, arroja error si no encuentra
isalpha     ¿Son alfabéticos?
isdigit     ¿Es un número?
islower     ¿Es minúscula?
isupper     ¿Es mayúscula?
delimitador. join        Uno una lista y uso delimitador como elemento que los separará
split       Destruyo y devuelvo un array(lista)


'''

# Ejemplo de uso de Join
a = [a]*5
print(a)
delimitador = '-'
b = delimitador.join(a)
print(b)

# Ejemplo de uso de split
# usando '-' como delimitador
a = b.split('-')
print(a)


# Podemos controlar el tipo de dato que es un elemento
# Y lo pasamos a otro tipo de dato
a = "42"
print(type(a))
print(a.isdigit())
a = int(a)
print(a)


# f-strings algo que solo existe en python
# se inicia con la letra f
# es similar a `${a} ${b}` en javascript
# devuelve una cadena de caracteres
a = 'Python'
b = 'UNSAM'
f'Estoy aprendiendo {a} en {b}'

# pero tiene otros usos:
b = 'Naranja'
a = 100
precio = 91

# Esto nos devuelve una columna formateada
# s es string 10 caracteres
# d es digit 10 digitos
# .2f es lo mismo que en c, la cantidad de decimales que queremos
c = f'{b:>10s} {a:10d} {precio:10.2f}'
print(c)

# pero tiene otros usos:
b = 'Mandarina'
a = 100
precio = 91

# Esto nos devuelve una columna formateada
c = f'{b:>10s} {a:10d} {precio:10.2f}'
print(c)