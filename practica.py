'''
    En python las divisiones y los módulos con un negativo y un positivo tienen una particularidad
    y es que en el caso de las divisiones con redondeo tienden a redondear hacia 0 en un sentido de
    recta, donde quieren llegar hacia el 0 absoluto de la recta infinita.

    Es decir, que si tenemos -3//2 redondeará hacia 2. Aunque no siempre es el caso
    y por eso existen librerías que omiten este comportamiento y lo convierten
    a unos mayormente esperado a lo que estamos acostumbrados en la matemática
    que nos han enseñado

'''
print(-3/2)     # devuelve -1.5
print(-3//2)    # devuelve -2.0

print(-19%3)    # devuelve -2 en lugar de resto 1 ¿Por qué?
                # porque en python siempre se debe de devolver un valor
                # positivo, y para eso se vuelve a tomar al divisor 3 y
                # se le resta el resto -1 + 3 = 2

print(-23%3)    # devuelve 1 ¿por qué? al resto: -2 se lo restamos al divisor
                # que es 3 y nos queda 1

''' EXPLICACIÓN

    Sí, si realizas la operación -23 % 3, el resultado sería 1.

    Al dividir -23 por 3, se obtiene un cociente de -7 con un resto de 2, ya que -7 x 3 = -21 y -21 + (-2) = -23. Sin embargo, el operador de módulo en Python devuelve el valor del resto como un número positivo, por lo que se le suma el divisor 3 al resto -2 para obtener un resultado final de 1.

    Por lo tanto, -23 % 3 es igual a 1 en Python.

 '''

# Para resolver este comportamiento modular en python podemos
# hacer uso de la librería 'math' y su modulo 'fmode'

import math
print(math.fmod(-10, 3)) # Devuelve -1.0

# Tenemos otras utilidades en la librería math

# podemos redondear hacia abajo:
print(math.floor(3/2))  # Devuelve 1

# podemos redondear hacia arriba:
print(math.ceil(3/2))  # Devuelve 2


# Raices:
# ingresamos el valor al que le queremos sacar raíz cuadrada
print(math.sqrt(2))


# Potencia:
# el valor, y segundo la potencia
print(math.pow(2,3))



# esto es extraño, pero puede obtener el infinito
# de un tipo de dato y de esa forma evitarte el overflow

print(float("inf"))     # No imprime, porque es infinito hasta el limite del tipo de dato
print(1<float("inf"))   # Esto devuelve true porque siempre será menor
print(float("-inf"))    # No imprime, porque es infinito hasta el limite del tipo de dato
print(1<float("-inf"))  # Esto devuelve false porque 1 es mayor a un infinito negativo del tipo de dato

# Aunque en python parece no existir el overflow, pero de todas formas hay
# que tenger cuidado





# ARRAYS : lists en python:
arr = [1, 2, 3]
# son dinámicos por default

# y puden ser usados como stacks, una pila
arr.append(4)
arr.append(5)

print(arr)

arr.pop()   # Esto debería quitar el último elemento
print(arr)


# Si bien podemos simular un stack con los array
# no quita que puedan ser usados con un array convencional
# y agregar elementos en una posición determinada con "insert"
arr.insert(1, 7)    # Hacemos inserción en la key '1' el valor '7'
print(arr)
# Pero esto es un big O en términos de tiempo de finalización de la operación
# al parecer su uso está desalentado

# Pero usar las keys nos brinda un tiempo constante de finalización:
arr[0] = 0
arr[3] = 0
print(arr)


# En javascript podemos crear un set de arrays con valores predeterminados
# haciendo uso de dos funciones arr = Array(5) y arr.fill(1)
# En python es parecido pero con una optimización en cantidad a escribir:
n = 5
arr = [1] *n
# con esto declaramos la cantidad de elementos que se repetirán en el array inicialmente
print(arr)

# Y claro, podemos saber el largo del array:
print(len(arr)) # Devuelve 5


# [-1] key
# no nos da un error, sino que parecido a golang nos devolvería 
# en reversa el último valor del array, la última key.
# Y si continuamos seguiría
print(arr[0])           # Devuelve 1
arr[len(arr)-1] = 4     # Asigna 4
print(arr[-1])          # Devuelve 4


# También puedes hacer uso de SLICE

arr = [1, 2, 3, 4]

# Para el SLICE puedes pasar 3 argumentos
# Inicio, Fin, cantidad de saltos (de cuanto en cuanto irá saltando)
# Por defecto los dos primeros valores son los máximos
# El de los saltos es 1

print(arr[1:3]) # Devuelve 2 y 3 (Es lo mismo que siempre que te genera dudas de por qué no toma el 4)


# También podemos hacer destructuración en python:

a, b = [1,2]
print(a)
print(b)

# Pero aparentemente no podemos hacerlo de la misma manera que Javascript
# en python esto se llama UNPACKAGING y debe coincidir la cantidad asignada
# con la cantidad a asignar
a, b, c, d = arr
print(c)
print(d)



#### LOOP ARRAY ###


# PODEMOS LOOPEAR en un array de la siguiente manera:
# Esta USA INDEX (con range)
for i in range(len(arr)):
    print(arr[i])

# Esta USA EL VALOR sin el index
for i in arr:
    print(n)


# Esta USA EL INDEX con (enumerate) y el valor:
# enumerate devuelve un valor a i y lo desempaqueta (UNPACKAGING)
for i, element in enumerate(arr):
    print('En el index: ',i, 'tengo el valor: ', element)


# Si tuviesemos dos arrays por los queremos iterar
# haríamos uso de la función zip():
# pero deben coincidir en cantidad
n1 = [4,5,6]
n2 = [1, 2, 3]

for i in zip(n1, n2):
    print(i)
    # Nos devuelve un par encerrado en paréntesis (una tupla)


# Revertir se hace con reverse()
arr = []
for i in zip(n1, n2):
    arr.append(i)
    # append de las tuplas al array

# Hacemos reverse sobre el orden de las TUPLAS
# NO podes hacer print y al mismo tiempo reverse 
# o te da NONE
arr.reverse()
print(arr)



# SORTING, tenemos una función que nos permite hacerle sort
# en ascendente por defecto

arr = [5, 4, 7, 10]
print(arr)
arr.sort()
print(arr)

# En orden de mayor a menor solo activamos reverse=True:
arr.sort(reverse=True)
print(arr)


# ¿Qué pasa con las letras?
# tabién podemos ordenarlas alfabéticamente con esta función
arr = ['las palabras', 'desordenadas', 'se unirán']
arr.sort()
print(arr)

# Para personalizar el sort lo podemos hacer
# de dos maneras, con una función lambda
# que es una función en una línea
# o una función personalizada más extensa

# Comencemos con una función fuera de la línea del sort:
def my_custom_function(x):  # Recibimos como argumento el elemento completo
    return x[0]             # devolvemos a sort lo que queremos que tenga en cuenta
                            # En este caso, que tenga en cuenta cada primer elemento del string

# Obtendríamos el orden alfabético, que lo tiene por default
arr.sort(key=my_custom_function)
print(arr)

# Podríamos hacer un reverse del resultado:
arr.sort(key=my_custom_function, reverse=True)
print(arr)



# EN UNA SOLA LÍNEA:
# usamos lambda que es semejante a declarar una función anónima = () => {}

arr.sort(key=lambda x: x[0])
print(arr)

# un ejemplo más con lambda, digamos que ordenamos por cantidad de caracteres:
arr.sort(key=lambda x: len(x))
print(arr)


# ADVANCE LIST CREATION
# involucra List Comprenhension
# es para cuando deseas crear columnas únicas
# en arrays multidimensionales que no conseguirías
# haciendo un arr = [[0]*4]*4
# porque no serían únicas

# De esta manera indicamos que el valor
# será el de i por cada i en un rango de 5
arr = [i for i in range(5)]
print(arr)

# así mismo podemos decirle que queremos
# que valga de la misma manera por cada 
# i en el rango de 5
arr = [0 for i in range(5)]
print(arr)


# ARRAYS MULTI DIMENSIONALES
# de esta forma repetimos el valor 
# creando un array de 4
arr = [0] * 4
print(arr)

# para el multi dimensional aplicamos
# el mismo principio pero le agregamos el
# list comprenhension

# Creamos un array de dos dimensiones
# el primer key accede a su respectivo
# conjunto de 4 ceros
# y el segundo key indica qué cero tocar
arr = [[0]*4 for i in range(4)]
print(arr)


# Strings
# Se manipulan de la misma manera, pero
# NO podemos mutar los chars de cada elemento de un string
'''
ESTO TIRARÁ ERROR
arr = "Inmutable"
arr[0] = "1"
print(arr)'''

# Podemos convertir los strings a int
# y viceversa
print(int("123") + int("123"))  # Sumas
print(str(123) + str(123))      # Concatenas


# ASCII
# si necesitamos obtener el valor ascii de un elemento
# podemos hacer uso de la función ord()
print(ord("a"))     # Devolverá el valor ascii de "a"
print(ord("b"))     # Devolverá el valor ascii de "b"


# JOIN
# Podemos hacer join de elementos en un array
# al revés de javascript
# hacemos uso de join, pero declaramos
# primero qué lo va a separar
# y entre paréntesis el arr:

arr = ["a", "b", "c"]
print("".join(arr))








# COLA
# En python podemos tener una cola
# de doblemente terminada

# hacemos uso de la librería deque
from collections import deque

queue = deque()
queue.append(1) # Agrega por derecha por default
queue.append(2)
print(queue)

queue.popleft() # Quitamos a la izquierda
print(queue)

queue.appendleft(0) # Podemos agregar hacia la izquierda
print(queue)

queue.pop()         # Por defecto saca de la derecha
print(queue)




# SETS

# HashSets, la ventaja es que podemos
# buscar dentro de ellos en un tiempo constante
# así como insertar en ellos en un tiempo constante
# usamos la función set()
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
# No puede haber duplicados 
# por lo que se fuciona con el existente
mySet.add(2)
print(mySet)    # Retorna {1,2}

# Podemos chequear con un True False
# si un elemento existe en el HashSet
print(1 in mySet)   #True
print(3 in mySet)   #False

# Para ELIMINAR usamos el remove()
mySet.remove(2)
print(mySet)

# Inicialización multiple
# podemos iniciar un set con múltiples valores
mySet = set([1,2,3])
print(mySet)

# Podemos hacer uso de SET Comprenhension
# para lo mismo
# similar a lo que usamos
# para los arrays multidimensionales
# solo que en lugar de envolver todo entre []
# envolvemos entre llaves
mySet = {i for i in range(5)}
print(mySet)

# eso fue HASHSET

# Ahora veremos HASHMAP
# son diccionarios, parecido a como
# declaras los objetos, pero diferente
# parece un híbrido entre array y objeto de javascript
# donde en un array pondrías la key entre comillas y corchetes
# aquí lo hacen como si fuese un objeto
myMap = {}
myMap["nuevaKey"] = 8
myMap["siguienteKey"] = 9
print(myMap)
# Al igual que el HashSet NO puede haber duplicados
myMap["nuevaKey"] = 10 # Sobreescribe el valor de la key
print(myMap)


# Ejemplo de uso para usuarios:
from datetime import datetime
userList = {}
userList["randomKeyGenerated"] ={
    "Usuario": "Nombre de usuario",
    "Fecha": datetime.now()
}

print(userList)

# Al igual que con HashSet, podemos controlar
# si un elemento existe en el hash y obtener
# True o False
print("randomKeyGenerated" in userList)

# en lugar de REMOVE usamos pop()
userList.pop("randomKeyGenerated")
print(userList)


# el comprenhension aquí se llama Dict Comprenhension
# debido a que en esencia es un diccionario.
# Si quisieramos declarar varios elementos en un objeto
# lo haríamos siguiendo el principio de la comprenhension
# del array: "se hará" mientras que por cada X en range(Y)
myDict = {i: i*2 for i in range(5)}
print(myDict)


# Loopear en un HashMap
# hay dos maneras
# la primera poniendo énfasis en la key
# la segunda poniendo énfasis en el valor

userList = {i: {"nombre": "", "puntos": i*2} for i in range(5)}
print(userList)

# énfasis en la key:
for i in userList:
    print(userList[i])


# énfasis en el valor:
# haciendo uso de values()
for value in userList.values():
    print(value)

# énfasis en ambos:
# haciendo usode items() y de unpackaging sobre lo que devuelve items()
for key, value in userList.items():
    print("el key: ", key, "posee los siguientes valores: ", value)




# TUPLAS...
# Son inmutables y las inicializamos con ()
# son como arrays
# se las usa como keys para hashmaps o hashsets

# La función tuple() puede recibir una lista
# y convertirla en tupla
# y para acceder a los elementos de una tupla usas
# su respectiva key[0]

myTuple = (1,2)
print(myTuple)

myMap = {
    (1,2): 3
}

print(myMap[(1,2)])

# Lo mismo para hashset:
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)   # Esto devuelve true

# ¿Por qué usar tuplas?
#  porque las listas NO pueden ser usadas como keys
#  no pueden ser HASHEABLES
#  myMap[[3,4]] = 5 NO funcionará, por ejemplo







# Heaps
# usado para encontrar el min y el max
# por defecto trabajamos con el minimo
# son en esencia arrays
# la particularidad es que siempre que tomen los
# valores asignará el valor mínimo a 0
# y el resto en orden

import heapq
#inicializamos el array con el que trabajaremos
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 2)

while len(minHeap):
    # Nos devuelve lo que popeamos
    print(heapq.heappop(minHeap))


# ¿Cómo trabajar con max?
# no hay funciones por defecto para
# trabajar con max, pero existe
# una manera usando negativos:

maxHeap = []
# Asignamos los valores en negativo
# cuando los invoquemos los multiplicaremos
# por negativo y de esa manera anulamos
# el signo original.
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -2)
# Devuelve el máximo
print(-1*maxHeap[0])
print("Máximos")
while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))


# Podemos construir el heap desde un array pre existente
# haciendo uso de heapify
arr = [4,5,6,10,8]
heapq.heapify(arr)
print("Mínimos con heapify")
while len(arr):
    print(heapq.heappop(arr))



# Funciones
# usan def para ser declaradas
# una particularidad es que en casos de
# funciones anidades es que la función
# superior tiene acceso a las variables
# de la inferior, y la inferior a los de la
# superior

def outer(a, b):
    c= 'c'
    # Es accesible por fuera y por dentro
    print(b)
    def inner():
        return a + b + c
    return inner()

print(outer('a','b'))


# En funciones anidadas podemos modificar un objeto
# pero no podemos reasigar salvo que declaremos
# 'nonlocal' antes de la variable
def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            # Esto altera el array original
            # para evitarlo debes crear una copia
            arr[i] *= 2

        '''
        esto no es posible. Por alguna razón
        dice que estás reasignando la variable
        contrario al array que almacena una franja
        de memoria y la memoria guarda el valor
        eso es lo que entiendo
        val *=2
        print(val)'''

        # Esto permite reasignar
        nonlocal val
        val *= 2
    helper()
    print('Valores modificados')
    print(arr, val)

nums = [1,2]
print("Antes de modificar")
print(nums)
val = 3
double(nums, val)
print("Luego de modificar con double")
print(nums)


# CLASES
# son más limitadas que en otros lenguages
# el constructor lleva doble guión bajo al principio
# y doble al final __init__(self,nums)

class MyClass:
    #Constructor
    def __init__(self, nums):
        # self es pasado en cada método de una clase
        # es como el 'this'

        # En esencia esta parte es la creación de variables
        # con un scope a toda la clase
        # Crear miembros variables
        self.nums = nums
        self.size = len(nums)

    # Crear un método:
    def getLength(self):
        # retornamos el tamaño
        return self.size
    
    # Creamos otro método:
    def getDoubleLength(self):
        return 2*self.getLength()
        