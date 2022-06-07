import os

try:
    entradas = os.scandir("meu_diretorio")

    for obj in entradas:
        print(obj)
        print("Nome:", obj.name)
        print("Caminho:", obj.path)
        print("É diretorio:", obj.is_dir())
        print("É arquivo:", obj.is_file())
        if obj.is_file():
            print("tamanho:", obj.stat().st_size, "B")
        print("=====================================")

except FileNotFoundError:
    print("O caminho não existe.")
except NotADirectoryError:
    print("O caminho não é um diretorio.")