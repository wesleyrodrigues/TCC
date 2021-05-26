from os import path, listdir
import pathlib
pasta = str(pathlib.Path().absolute())

caminhos = [path.join(pasta, nome) for nome in listdir(pasta)]
arquivos = [arq for arq in caminhos if path.isfile(
    arq) and arq.lower().endswith(".png")]
pngs = [arq for arq in arquivos if arq.lower().endswith(".png")]
arquivos_nomes = [arq[73:] for arq in arquivos]
print(len(arquivos_nomes))
print(arquivos_nomes)