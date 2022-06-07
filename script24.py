print("Abrindo um arquivo")

try:
    open("teste.pdf", 'w')
    print("Arquivo aberto!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição", erro)

print("Término do programa")
