class Solution:
    # En el caso de una lista o diccionario
    # podemos convertir la lista a un set y
    # comparar sus tamaños. Si se redujo, es porque había duplicados
    def containsDuplicate(self, nums: list[int]) -> bool:
        if(len(nums) != len(set(nums))):
            return True