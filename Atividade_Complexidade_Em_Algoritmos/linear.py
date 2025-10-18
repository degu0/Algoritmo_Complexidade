def encontrar_maximo(lista):
  """
  Encontra o maior número em uma lista.

  Complexidade: O(n) - Linear.
  Onde 'n' é o número de elementos na lista. O algoritmo precisa
  percorrer cada elemento da lista uma vez para encontrar o máximo.
  """
  if not lista:
    return None

  maximo = lista[0]
  for numero in lista:
    if numero > maximo:
      maximo = numero
  return maximo

# --- Exemplo de Uso ---
numeros = [45, 23, 89, 12, 99, 5, 67]
print(f"O maior número na lista é: {encontrar_maximo(numeros)}")