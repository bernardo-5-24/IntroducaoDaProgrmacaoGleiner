#bernardo irie Rochas
a= int(input ("'quantos arquivos o senhor precisa carregar?"))
b= int (input ("em tempo médio, quantos segundos demora para carregar um arquivo"))
print (f"o tempo total te carregar os arquivos {a*b}, ou seja {a*b / 60} minutos e {a*b % 60}, cada 10 arquivos vai demorar aprocimadamente {10 * b}")