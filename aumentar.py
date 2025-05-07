import numpy as np

def aumentar_com_repeticao(imagem):
    imagem_lista = list(imagem)
    nova_imagem = []
    for i in range(len(imagem_lista)*2):
        nova_imagem.append([])
        for j in range(len(imagem_lista[0])*2):
            nova_imagem[i].append(imagem_lista[i//2][j//2])

    print(f'\nTamanho da imagem antiga: {len(imagem_lista[0])} X {len(imagem_lista)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)


def aumentar_com_media(imagem):
    imagem_lista = list(imagem)
    nova_imagem = []
    for i in range(len(imagem_lista)*2):
        nova_imagem.append([])
        for j in range(len(imagem_lista[0])*2):
            if(j%2!=0 and j//2 < len(imagem_lista[0])-1):
                azul = (int(imagem_lista[i//2][j//2][0]) + 
                         int(imagem_lista[i//2][j//2+1][0])) // 2
                verde = (int(imagem_lista[i//2][j//2][1]) + 
                         int(imagem_lista[i//2][j//2+1][1])) // 2
                vermelho = (int(imagem_lista[i//2][j//2][2]) + 
                            int(imagem_lista[i//2][j//2+1][2])) // 2
                nova_imagem[i].append([azul,verde,vermelho])
            elif(i%2!=0 and i//2 < len(imagem_lista)-1):
                azul = (int(imagem_lista[i//2][j//2][0]) + 
                        int(imagem_lista[i//2+1][j//2][0])) // 2
                verde = (int(imagem_lista[i//2][j//2][1]) + 
                         int(imagem_lista[i//2+1][j//2][1])) // 2
                vermelho = (int(imagem_lista[i//2][j//2][2]) + 
                            int(imagem_lista[i//2+1][j//2][2])) // 2
                nova_imagem[i].append([azul,verde,vermelho])
            elif(j%2!=0 and i%2!=0 and j//2 < len(imagem_lista[0])-1 and i//2 < len(imagem_lista)-1):
                azul = (int(imagem_lista[i//2][j//2][0]) + 
                        int(imagem_lista[i//2+1][j//2+1][0])) // 2
                verde = (int(imagem_lista[i//2][j//2][1]) + 
                         int(imagem_lista[i//2+1][j//2+1][1])) // 2
                vermelho = (int(imagem_lista[i//2][j//2][2]) + 
                            int(imagem_lista[i//2+1][j//2+1][2])) // 2
                nova_imagem[i].append([azul,verde,vermelho])
            else:
                nova_imagem[i].append(imagem_lista[i//2][j//2])

    print(f'\nTamanho da imagem antiga: {len(imagem_lista[0])} X {len(imagem_lista)}')
    print(f'Tamanho da imagem nova: {len(nova_imagem[0])} X {len(nova_imagem)}')
    return np.array(nova_imagem, dtype=np.uint8)







