verificador =int( input("Digite um número para saber se este encontra-se na sequência de fibonacci : "))

n1 = 0
n2 = 1
n3 = 0
lista=[]

for i in range(verificador+2):
    lista.append(n1)
    n3 = n1 + n2
    n2 = n1
    n1 = n3  
    

if verificador in lista:
    print('Esse número está na sequência de fibonacci!') 
else:
    print('Esse número não está na sequência de fibonacci!')     
      
print()
print( "Fim do algoritmo.")
