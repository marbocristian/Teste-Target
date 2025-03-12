#Escreva um programa que inverta os caracteres de um string.

#Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; Evite usar funções prontas, como, por exemplo, reverse;


texto = input("Digite a string que você deseja inverter: ")
texto_invertido = ""

for i in range(len(texto) - 1, -1, -1):
  texto_invertido += texto[i]

print(f"String invertida: {texto_invertido}")
