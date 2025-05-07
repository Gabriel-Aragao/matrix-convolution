import numpy as np

def rotacionar_imgdir (imagem):
    nova_imagem = []
    for i in range(len(imagem[0])):
        nova_imagem.append([])
        for j in range(len(imagem)):
                nova_imagem[i].append(imagem[len(imagem)-1-j][i])

    return np.array(nova_imagem,dtype=np.uint8)

def rotacionar_imgesq (imagem):
    nova_imagem = []
    for i in range(len(imagem[0])):
        nova_imagem.append([])
        for j in range(len(imagem)):
                nova_imagem[i].append(imagem[j][len(imagem[0])-1-i])
    return np.array(nova_imagem,dtype=np.uint8)