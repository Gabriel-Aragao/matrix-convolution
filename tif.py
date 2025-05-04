import numpy as np


def rgb_nir2tif(img_rgb, img_nir):
    altura, largura = len(img_rgb), len(img_rgb[0])
    img_tif = []
    
    for i in range(altura):
        row = []
        for j in range(largura):
            row.append([img_rgb[i][j][0], 
                        img_rgb[i][j][1], 
                        img_rgb[i][j][2], 
                        img_nir[i][j][0]])
        img_tif.append(row)

    img_tif = np.array(img_tif)
    return img_tif
