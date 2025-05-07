import numpy as np

def diminuir_com_media(imagem):
    nova_imagem = []
    for i in range(0, len(imagem)-2, 2):
        nova_imagem.append([])
        for j in range(0, len(imagem)-2, 2):
            azul = (int(imagem[i][j][0]) + 
                    int(imagem[i][j+1][0]) + 
                    int(imagem[i+1][j][0]) + 
                    int(imagem[i+1][j+1][0]))//4
            
            verde = (int(imagem[i][j][1]) + 
                    int(imagem[i][j+1][1]) + 
                    int(imagem[i+1][j][1]) + 
                    int(imagem[i+1][j+1][1]))//4
            
            vermelho = (int(imagem[i][j][2]) + 
                    int(imagem[i][j+1][2]) + 
                    int(imagem[i+1][j][2]) + 
                    int(imagem[i+1][j+1][2]))//4
            nova_imagem[i//2].append([azul, verde, vermelho])

    print(f'\nTamanho da imagem antiga: {len(imagem[0])} X {len(imagem)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)

def diminuir_com_perda(imagem):
    nova_imagem = []
    for i in range(0, len(imagem)-2, 2):
        nova_imagem.append([])
        for j in range(0, len(imagem)-2, 2):
            nova_imagem[i//2].append(imagimagemem_lista[i][j])
            
    print(f'\nTamanho da imagem antiga: {len(imagem[0])} X {len(imagem)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)
