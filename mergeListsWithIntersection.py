list1 = [1,2,3,4,5,6,7,10,11]
list2 = [1,2,3,10]
# Quitamos los repetidos con set
set1 = set(list1)
set2 = set(list2)
# Creamos una nueva lista aplicando
# el método intersección que viene con los sets
commonElements = list(set1.intersection(set2))
print(commonElements)