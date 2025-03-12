texto = input("Digite a string que você deseja inverter: ")
texto_invertido = ""

for i in range(len(texto) - 1, -1, -1):
  texto_invertido += texto[i]

print(f"String invertida: {texto_invertido}")
