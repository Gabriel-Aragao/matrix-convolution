import os
import cv2
import cmapy
import datetime
import ndvi
import tif

IMAGEM_DIR = "imagens"

def exibir_menu():
    print("\nMenu Principal:")
    print("1. Combinar RGB e NIR para TIF")
    print("2. Transformar TIF(RGB+NIR) para NDVI")
    print("0. Encerrar")

def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def listar_imagens(extensoes):
    imagens = []
    try:
        for file in os.listdir(IMAGEM_DIR):
            if os.path.isfile(os.path.join(IMAGEM_DIR, file)):
                if file.split('.')[-1] in extensoes:
                    imagens.append(file)
        return imagens
    except:
        print(f"Ocorreu um erro ao listar os arquivos. Verifique a pasta e tente novamente. Erro: {e}")
        return None

def selecionar_imagem(imagens):
    print('\nMenu de imagens:')
    for i in range(len(imagens)):
        print(f"{i + 1}. {imagens[i]}")
    indice = -1
    while indice != 0:
        indice = int(input(f"Digite o número da imagem escolhida: "))
        if 1 <= indice <= len(imagens):
            nome_imagem = imagens[indice - 1]
            path_imagem = os.path.join(IMAGEM_DIR, nome_imagem) 

            print(f"Imagem selecionada: {path_imagem}")
            return path_imagem 
        else:
            print("Escolha inválida. Tente novamente.")

def carregar_imagem(extensoes):
    imagens = listar_imagens(extensoes)
    if not imagens:
        print("Não há imagens disponíveis para esta operação.")
        return None
    path_imagem = selecionar_imagem(imagens)
    try:
        return cv2.imread(path_imagem, cv2.IMREAD_UNCHANGED)
    except:
        print("Erro ao carregar a imagem.")
        return None

def salvar_imagem(imagem, nome_base, extensao):
    timestamp = get_timestamp()
    nome_arquivo = f"{nome_base}_{timestamp}.{extensao}"
    caminho_completo = os.path.join(IMAGEM_DIR, nome_arquivo)
    try:
        cv2.imwrite(caminho_completo, imagem)
        print(f"\nImagem salva em: {caminho_completo}")
    except Exception as e:
        print(f"\nErro ao salvar a imagem em {caminho_completo}")
    

print("====Matrix Convolution====")

opcao = -1
while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o número da opção escolhida: "))

    if opcao == 1:
        extensoes = ['png']
        
        print("\nEsta opção combina 2 imagens .PNG em uma imagem .TIF")
        
        print("Selecione a primeira imagem .PNG com os canais NIR:")
        img_nir = carregar_imagem(extensoes)
        if img_nir is None:
            continue

        print("Selecione a imagem .PNG correspondente com os canais RGB:")
        img_rgb = carregar_imagem(extensoes)
        if img_rgb is None:
            continue
        
        nova_imagem = tif.rgb_nir2tif(img_rgb, img_nir)
        salvar_imagem(nova_imagem, "RGB_NIR", "tif")
        
    
    elif opcao == 2:
        extensoes = ['tif']

        print("\nEsta opção aplica o cálculo do NDVI e transforma a imagem.")
        imagem = carregar_imagem(extensoes)
        if imagem is None:
            continue

        nir = ndvi.get_nir_band(imagem)
        red = ndvi.get_red_band(imagem)
        ndvi_result = ndvi.ndvi_calc(nir, red)
        
        gray = ndvi.ndvi2gray(ndvi_result)
        nova_imagem = cv2.applyColorMap(gray, cmapy.cmap('RdYlGn'))
        
        salvar_imagem(nova_imagem, "NDVI", "png")

    
    elif opcao != 0:
        print("\nOpção Inválida!")

print("\nPrograma encerrado.")