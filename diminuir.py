import numpy as np

def diminuir_com_media(imagem):
    imagem_lista = list(imagem)
    nova_imagem = []
    for i in range(0, len(imagem_lista)-2, 2):
        nova_imagem.append([])
        for j in range(0, len(imagem_lista)-2, 2):
            azul = (float(imagem_lista[i][j][0]) + 
                    float(imagem_lista[i][j+1][0]) + 
                    float(imagem_lista[i+1][j][0]) + 
                    float(imagem_lista[i+1][j+1][0]))//4
            
            verde = (float(imagem_lista[i][j][1]) + 
                    float(imagem_lista[i][j+1][1]) + 
                    float(imagem_lista[i+1][j][1]) + 
                    float(imagem_lista[i+1][j+1][1]))//4
            
            vermelho = (float(imagem_lista[i][j][2]) + 
                    float(imagem_lista[i][j+1][2]) + 
                    float(imagem_lista[i+1][j][2]) + 
                    float(imagem_lista[i+1][j+1][2]))//4
            nova_imagem[i//2].append([azul, verde, vermelho])

    print(f'\nTamanho da imagem antiga: {len(imagem_lista[0])} X {len(imagem_lista)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)

def diminuir_com_perda(imagem):
    imagem_lista = list(imagem)
    nova_imagem = []
    for i in range(0, len(imagem_lista)-2, 2):
        nova_imagem.append([])
        for j in range(0, len(imagem_lista)-2, 2):
            nova_imagem[i//2].append(imagem_lista[i][j])
            
    print(f'\nTamanho da imagem antiga: {len(imagem_lista[0])} X {len(imagem_lista)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)
