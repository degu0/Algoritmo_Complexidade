def obter_primeiro_elemento(lista):
  """
  Retorna o primeiro elemento de uma lista.

  Complexidade: O(1) - Constante.
  O tempo de execução não depende do tamanho da lista, pois
  acessar um elemento pelo índice é uma operação de tempo constante.
  """
  if lista:
    return lista[0]
  return None

# --- Exemplo de Uso ---
lista_pequena = [3, 1, 4]
lista_grande = list(range(1000000))

print(f"Primeiro elemento da lista pequena: {obter_primeiro_elemento(lista_pequena)}")
print(f"Primeiro elemento da lista grande: {obter_primeiro_elemento(lista_grande)}")