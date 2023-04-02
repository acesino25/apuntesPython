'''
Estaba equivocado, esto es otra cosa
class Solution:
    # Controlar si t es un anagrama de s
    def isAnagram(self, s: str, t: str) -> bool:
        # no podemos aplicar reverse sobre un string
        # pero podemos hacer uso de slice
        # y el mismo slice te un array invertido para controlar
        # stringAinvertir[::-1] 
        return s[::-1] == t '''

# Creo que deberías intentar con un HEAP o un array e ir haciendo POPS 
class Solution:
    # Controlar si t tiene todas las letras de s
    def isAnagram(self, s: str, t: str) -> bool:
        # si uno es más grande que el otro
        # no son anagramas
        if(len(s) != len(t)):
            return False

        #convertimos a t en un array (una lista)
        arrT = list(t)
        # También podríamos haber puesto arrT = [char for char in t]
        
        #por cada caracter en s
        for chr in s:
            # el caracter está contenido en t?
            if(not chr in arrT):
                return False
            else:
                # si lo está hacemos remove() que se usa en lugar de pop cuando no sabes el índice
                arrT.remove(chr)
        return True
    
# Esta es la mejor solución:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorted
        '''
        sorted(s) -> ['R', 'a', 'a', 'z']
        sorted(t) -> ['R', 'a', 'a', 'z']
        '''
        # Nos devuelve una lista ordenada de letras, y
        # si fuesen anagramas sería la misma cadena
        return sorted(s)==sorted(t)
