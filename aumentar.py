import numpy as np

def aumentar_imagem(imagem):
    imagem_lista = list(imagem)
    nova_imagem = []
    for i in range(len(imagem_lista)*2):
        nova_imagem.append([])
        for j in range(len(imagem_lista[0])*2):
            nova_imagem[i].append(imagem_lista[i//2][j//2])

    print(f'\nTamanho da imagem antiga: {len(imagem_lista[0])} X {len(imagem_lista)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)







