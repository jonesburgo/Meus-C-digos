import os

try:
    os.mkdir("meu_diretorio")
    print("Diretório criado!")
except PermissionError as erro:
    print("Sem permissão para criar o diretório")
    print("Descrição", erro)
except FileExistsError as erro:
    print("Diretório já existe")
    print("Descrição", erro)

print("Término do programa")
