import numpy as np


def get_red_band(imagem):
    nova_imagem= []
    for i in range(len(imagem)):
        nova_imagem.append([])
        for j in range(len(imagem[0])):
            nova_imagem[i].append(int(imagem[i][j][2]))
    return nova_imagem


def get_nir_band(imagem):
    nova_imagem= []
    for i in range(len(imagem)):
        nova_imagem.append([])
        for j in range(len(imagem[0])):
            nova_imagem[i].append(int(imagem[i][j][3]))
    return nova_imagem


def ndvi_calc(nir, red):
    ndvi = []
    for i in range(len(red)):
        ndvi.append([])
        for j in range(len(red[i])):
            pixel_ndvi = (nir[i][j] - red[i][j]) / (nir[i][j] + red[i][j])
            ndvi[i].append(pixel_ndvi)
    return ndvi

def ndvi2gray(ndvi):
    image = []

    x_min = -1.0
    x_max = 1.0
    y_min = 0.0
    y_max = 255.0

    scale = (y_max - y_min) / (x_max - x_min)

    for i in range(len(ndvi)):
        image.append([])
        for j in range(len(ndvi[0])):
            ndvi_value = ndvi[i][j]
            
            gray_value_float = y_min + (ndvi_value - x_min) * scale
            gray_value_int = int(round(gray_value_float))
            
            image[i].append(gray_value_int)
    return np.array(image, dtype=np.uint8)
