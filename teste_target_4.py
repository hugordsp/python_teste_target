import os
os.system('cls')

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp+rj+mg+es+outros

print(f'Percentual de representação de SP é de {round(sp/total*100,2)}%')
print(f'Percentual de representação de RJ é de {round(rj/total*100,2)}%')
print(f'Percentual de representação de MG é de {round(mg/total*100,2)}%')
print(f'Percentual de representação de ES é de {round(es/total*100,2)}%')
print(f'Percentual de representação de Outros é de {round(outros/total*100,2)}%')
print()
print( "Fim do algoritmo.")