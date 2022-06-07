frase = "Eu amo comer amoras no café da manhã"

#   Resultado obitido utilizando o método count diretamente
print("Contagem direta: ", frase.count('amo'))

#   Resultado obitido utilizando a quebra da frase em palavras
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print("Contagem correta: ", contador)
