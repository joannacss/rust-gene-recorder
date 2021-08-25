import cv2 as cv
import numpy as np
from vision import Vision

mon_world = {"top": 286, "left": 1073, "width": 373, "height": 148}
mon_loot = {"top": 295, "left": 797, "width": 154, "height": 26}

GENE_LOOT_SIZE = 17
GENE_LOOT_SPACING = 10

y_gene = Vision('img/y-gene.png')
g_gene = Vision('img/g-gene.png')
h_gene = Vision('img/h-gene.png')
w_gene = Vision('img/w-gene.png')
x_gene = Vision('img/x-gene.png')

# def find_gene():
    # 1: 1, 17 (17 pixel width, 9 pixel spacing)
    # 2: 34,50
    # 3: 60,76
    # 4: 86,102
    # 5: 112,126

def get_gene_roi(image, size=GENE_LOOT_SIZE, spacing=GENE_LOOT_SPACING, debug=None):
    """
    Return the regions for loot Genes

    :param image:
    :param size:
    :param spacing:
    :param debug:
    :return: Regions for ROI (X, Y, W, H)
    """
    # For the 6 Genes, draw an ROI rectangle
    regions = []
    top_left = (1,1)
    bottom_right = (top_left[0] + GENE_LOOT_SIZE, top_left[1] + GENE_LOOT_SIZE)
    for i in range(6):
        if i > 0:
            top_left = (((GENE_LOOT_SIZE + GENE_LOOT_SPACING) * i), 1)
            bottom_right = (top_left[0] + GENE_LOOT_SIZE, top_left[1] + GENE_LOOT_SIZE)

        # Add ROI to regions (X, Y, W, H)
        regions.append((top_left[0], top_left[1], GENE_LOOT_SIZE, GENE_LOOT_SIZE))

        if debug:
            cv.rectangle(image, top_left, bottom_right, color=(0,255,0),
                         lineType=cv.LINE_8, thickness=1)

    return regions


def get_gene(image):
    regions = get_gene_roi(image)