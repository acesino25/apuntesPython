# Declaramos el inicio
# usando unpackage
a, b = 0, 1

# realizamos una acción por cada
# i en el rango 10
for i in range(10):
  print(a)  # Va a ser el valor previo siempre
  # b a la derecha en el primer ciclo vale 1
  # 1, 0+1
  # a, b a la izquierda se asignan esos resultados
  # en el segundo ciclo
  # b a la derecha vale 1 nuevamente
  # 1, 1+1
  # a, b a la izquierda son asignados los resultados
  # en el tercer ciclo
  # b a la derecha vale 2
  # 2, 2+1
  # a, b los resultados son asignados a los valores de la izquierda

  # Puede resultar confuso, pero lo que sucede
  # es que a la izquierda solicitamos los nuevos valores de a, b
  # a siempre va a ser el valor previo, que es B. Porque en el ciclo previo
  # tenemos a b como el resultado previo, entonces ahora que lo actualizaremos
  # necesitamos guardarlo para usarlo.
  a, b = b, a+b
