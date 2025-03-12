#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

#O menor valor de faturamento ocorrido em um dia do mês;
#O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:

#Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;






import json


with open('dados.json', 'r') as meu_json:
    dados = json.load(meu_json)






valores = [item['valor'] for item in dados]
valores_validos = [v for v in valores if v > 0]

menor_valor = min(valores_validos)
maior_valor = max(valores_validos)
media_mensal = sum(valores_validos) / len(valores_validos)
dias_acima_da_media = sum(1 for v in valores_validos if v > media_mensal)


print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal ( $$ {media_mensal:.2f} $$ ): {dias_acima_da_media}")

