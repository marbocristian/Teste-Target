def pertence_fibonacci(numero):
  """Verifica se um número pertence à sequência de Fibonacci.

  Args:
    numero: O número a ser verificado.

  Returns:
    True se o número pertence à sequência de Fibonacci, False caso contrário.
  """

  a = 0
  b = 1

  while b < numero:
    a, b = b, a + b

  return b == numero

numero = int(input("Digite um número: "))

if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
