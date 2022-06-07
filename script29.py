import os

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido!")
except PermissionError as erro:
    print("Sem permissão para remover diretório")
    print("Descrição", erro)
except FileNotFoundError as erro:
    print("Diretorio inexistente")
    print("Descrição", erro)
except OSError as erro:
    print("Outro erro.")
    print("O diretorio está vazio")
    print("Descrição", erro)

print("Termino do programa.")