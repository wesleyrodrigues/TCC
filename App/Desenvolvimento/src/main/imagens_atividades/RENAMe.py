import os 

pasta = "C:\\Users\\wesle\\Documents\\TCC\\App\\Desenvolvimento\\src\\main\\imagens_atividades"
nome = "imagens_atividades"
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
arquivos_nomes = [arq[77:] for arq in arquivos]
[os.rename(arq, arq[:-4].upper() + arq[-4:]) for arq in arquivos_nomes]

pngs = [arq for arq in arquivos if arq.lower().endswith(".png")]
print(pngs)