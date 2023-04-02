def countVowels(cadena):
  vowels = "aeiouAEIOU"
  count = 0

  for char in cadena:
    if char in vowels:
      count += 1

  return count

print(countVowels("mis vocales"))