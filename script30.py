import os
import errno

try:
    os.rmdir("meu_diretorio")
    print("diretorio removido!")
except OSError as erro:
    print("erro.errno")
    if erro.errno == errno.ENOTEMPTY:
        print("O diretorio não está vazio")
    else:
        print("Erro inesperado!")
    print("Descrição", erro)
print("Termino do programa")
