# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2 as cv
import numpy as np
import mss
import mss.tools
from vision import Vision
import genes
from time import sleep

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
mss = mss.mss()


def empty(blah):
    pass


y_gene = Vision('img/y-gene.png')
g_gene = Vision('img/g-gene.png')
h_gene = Vision('img/h-gene.png')
w_gene = Vision('img/w-gene.png')
x_gene = Vision('img/x-gene.png')

mon_world = {"top": 286, "left": 1073, "width": 373, "height": 148}
mon_loot = {"top": 299, "left": 797, "width": 154, "height": 20}

gene_set = set()
gene_file = open('genes.txt', 'w')

# Loop until Q is pressed
while True:

    # Get Screenshot
    sct = mss.grab(mon_loot)
    img = np.array(sct)
    regions = genes.get_gene_roi(img)

    gene_output = []
    for region in regions:
        x, y, w, h = region
        img2 = img[y:y + h, x:x + w]
        match_y = y_gene.find_max(img2, threshold=0.7)
        match_g = g_gene.find_max(img2, threshold=0.7)
        match_h = h_gene.find_max(img2, threshold=0.7)
        match_x = x_gene.find_max(img2, threshold=0.55)
        match_w = w_gene.find_max(img2, threshold=0.55)

        # Compare Max Values
        gene_scores = {'Y': match_y['max_val'], 'G': match_g['max_val'], 'H': match_h['max_val'],
                       'X': match_x['max_val'], 'W': match_w['max_val']}

        max_gene = max(gene_scores, key=gene_scores.get)
        if gene_scores[max_gene] > 0:
            # print(max_gene)
            gene_output.append(max_gene)
        cv.imshow('test', img2)

    gene_output = ''.join(gene_output)
    if gene_output not in gene_set and len(gene_output) == 6:
        gene_set.add(gene_output)
        gene_file.write(gene_output)
        gene_file.write('\n')
        print(gene_output)
    # print(gene_output)
    cv.imshow('Result', img)
    # cv.imshow('Gene ROI', img2)
    # match = y_gene.find_max(img, threshold=0.80, debug_mode='points')


    # Close Image Preview when 'Q' Pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

gene_file.close()