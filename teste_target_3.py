lista=[22174.1664,24537.6698,26139.6134,0,0,26742.6612,0,42889.2258,46251.174,11191.4722,0,0,3847.4823,373.7838,2659.7563,48924.2448,18419.2614,0,0,35240.1826,43829.1667,18235.6852,4355.0662,13327.1025,0,0,25681.8318,1718.1221,13220.495,8414.61]

for i in lista:
    if 0 in lista:
        lista.remove(0)

media = sum(lista)/len(lista)

j=0
for x in lista:
    if x> media:
        j= j+ 1
        
print(f'A média de faturamento foi de {media}')
print(f'O menor valor de faturamento ocorrido em um dia do mês é {min(lista)}')
print(f'O maior valor de faturamento ocorrido em um dia do mês é {max(lista)}')
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é de {j} dias') 
print()
print( "Fim do algoritmo.")