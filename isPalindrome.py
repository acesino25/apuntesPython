from typing import Any
def isPalindrome(element: Any)-> bool:
  # Reverseamos: start : end : step
  # omit start, omit end, start 1 at time in reverse
  return element == element[::-1]

def getList(lista:list)->None:
  for i, value in enumerate(lista):
    if(isPalindrome(value)):
      print(value)

lista1 = ["racecar", "element"]

getList(lista1)