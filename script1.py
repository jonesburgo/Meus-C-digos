import os
#Para o arquivo dados1.txt
arquivo1 = open("dados1.txt") #caminho relativo
arquivo2 = open("C:\pythonProject\Projetão\dados1.txt")

# Para o arquivo dados2.txt
arquivo3 = open("documentos/dados2.txt") # caminho relativo
arquivo4 = open("C:\pythonProject\Projetão\documentos/dados2.txt") # caminho definitivo

print(os.path.relpath(arquivo1.name))
print(os.path.abspath(arquivo1.name))

print(arquivo1)