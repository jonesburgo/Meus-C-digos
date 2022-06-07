import  os

try:
    os.rename("teste_alfa.txt", "teste_beta.txt")
    print("Arquivo renomeado!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição", erro)
except FileExistsError as erro:
    print("Arquivo destino ja exístente")
    print("Descrição", erro)

print("Término do programa")


for i in range(10):

    if (i%2==0):

        print(i)
