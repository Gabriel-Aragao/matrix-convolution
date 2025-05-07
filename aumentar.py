import numpy as np

def aumentar_com_repeticao(imagem):
    nova_imagem = []
    for i in range(len(imagem)*2):
        nova_imagem.append([])
        for j in range(len(imagem[0])*2):
            nova_imagem[i].append(imagem[i//2][j//2])

    print(f'\nTamanho da imagem antiga: {len(imagem[0])} X {len(imagem)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)


def aumentar_com_media(imagem):
    nova_imagem = []
    for i in range(len(imagem)*2):
        nova_imagem.append([])
        for j in range(len(imagem[0])*2):
            
            if(j%2!=0 and j//2 < len(imagem[0])-1):
                azul = (int(imagem[i//2][j//2][0]) + 
                         int(imagem[i//2][j//2+1][0])) // 2
                verde = (int(imagem[i//2][j//2][1]) + 
                         int(imagem[i//2][j//2+1][1])) // 2
                vermelho = (int(imagem[i//2][j//2][2]) + 
                            int(imagem[i//2][j//2+1][2])) // 2
                nova_imagem[i].append([azul,verde,vermelho])
            
            elif(i%2!=0 and i//2 < len(imagem)-1):
                azul = (int(imagem[i//2][j//2][0]) + 
                        int(imagem[i//2+1][j//2][0])) // 2
                verde = (int(imagem[i//2][j//2][1]) + 
                         int(imagem[i//2+1][j//2][1])) // 2
                vermelho = (int(imagem[i//2][j//2][2]) + 
                            int(imagem[i//2+1][j//2][2])) // 2
                nova_imagem[i].append([azul,verde,vermelho])
            
            elif(j%2!=0 and i%2!=0 and j//2 < len(imagem[0])-1 and i//2 < len(imagem_lista)-1):
                azul = (int(imagem[i//2+1][j//2][0]) +
                        int(imagem[i//2][j//2+1][0])) // 2
                verde = (int(imagem[i//2+1][j//2][1]) +
                         int(imagem[i//2][j//2+1][1])) // 2
                vermelho = (int(imagem[i//2+1][j//2][2]) +
                            int(imagem[i//2][j//2+1][2])) // 2
                nova_imagem[i].append([azul,verde,vermelho])
            
            else:
                nova_imagem[i].append(imagem[i//2][j//2])

    print(f'\nTamanho da imagem antiga: {len(imagem[0])} X {len(imagem)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)







