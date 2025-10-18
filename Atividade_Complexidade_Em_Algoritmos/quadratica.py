def contem_duplicatas(lista):
  """
  Verifica se existem elementos duplicados em uma lista usando laços aninhados.

  Complexidade: O(n^2) - Quadrática.
  Para cada elemento 'n' na lista (primeiro loop), o algoritmo
  percorre a lista novamente (segundo loop). Isso resulta em n*n
  comparações no pior caso.
  """
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] == lista[j]:
        return True
  return False

# --- Exemplo de Uso ---
lista_sem_duplicatas = [1, 2, 3, 4, 5]
lista_com_duplicatas = [1, 2, 3, 2, 5]

print(f"A lista [1, 2, 3, 4, 5] contém duplicatas? {contem_duplicatas(lista_sem_duplicatas)}")
print(f"A lista [1, 2, 3, 2, 5] contém duplicatas? {contem_duplicatas(lista_com_duplicatas)}")