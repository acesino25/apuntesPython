nombres = ['Laura', 'Juan', 'Tomás', 'Ana', 'Diego', 'Carla', 'Kim', 'Sofía']
apellidos = ['Pérez', 'Isla', 'Gómez', 'Castro', 'Roca', 'Romero', 'Díaz', 'López']
notas = [7, 4, 9, 5, 7, 8, 6, 10]


# Tu codigo
# Combine the data into a list of tuples
# hamos uzo de zip para crear una tupla de la lista
# a esas tuplas las encerramos en una lista para iterarlas
alumnos = list(zip(nombres, apellidos, notas))

# Sort the list of tuples by the apellido
# hacemos uso de sort(key=) en lugar de 'len'
# la key en este caso va a ser una función personalizada
# le decimos que de los elementos [0][1][2]
# tome aquel que corresponda a la columna uno, que son los
# apellidos y los ordene. 
# Por default los ordena por orden alfabético
# lambda es una manera de definir una función anónima
alumnos.sort(key=lambda x: x[1])

# Print the nombre and apellido of each alumno
print('Lista de alumnos ordenada por apellido:')
# por cada tupla en la lista alumnos:
for alumno in alumnos:
    print(f'{alumno[1]}, {alumno[0]}')
    # [1] apellido en la tupla
    # [0] nombre en la tupla

# Calculate the average, max, and min notas
# de la cursada obtendremos el total de notas y las promediaremos
# sum() el total, len() la cantidad de elementos en la lista
promedio = sum(notas) / len(notas)
# la función max(), min()
nota_maxima = max(notas)
nota_minima = min(notas)

print(f'Promedio de notas: {promedio:.2f}')
print(f'Nota máxima: {nota_maxima}')
print(f'Nota mínima: {nota_minima}')

# Generate a list of aprobados
# creamos una nueva lista, siendo alumno el resultado final
# que depositaremos en la lista por cada iteración
# alumno en alumnos se contará, solo si en la tupla en su valor
# de [2] notas, éste es mayor o igual a 7
aprobados = [alumno for alumno in alumnos if alumno[2] >= 7]

# Generate a list of boolean values indicating whether each alumno is aprobado
# ahora lo mismo pero para el total de la tupla
# guardando TRUE en caso de cumplirse la condición
# False en caso de que no
aprobado_bool = [alumno[2] >= 7 for alumno in alumnos]

# Imprimimos la lista de aprobados únicamente
print('Lista de aprobados:')
for alumno in aprobados:
    print(f'{alumno[1]}, {alumno[0]}')

# Imprimimos la lista de TRUE y FALSE que corresponda a cada alumno
# en la lista alumnos que creamos con tuplas
print('Lista de aprobados (True/False):')
print(aprobado_bool)