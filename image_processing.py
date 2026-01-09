#Fonctions de traitement d'images

import cv2
import numpy as np


def filter_image(img):
    imgFlou = cv2.GaussianBlur(img, (5, 5), 0)
    contours = cv2.Canny(imgFlou, 50, 150, 3)
    elementStructurant = np.ones((3, 3), np.uint8)
    contoursDilates = cv2.dilate(contours, elementStructurant)
    _, imgResultat = cv2.threshold(contoursDilates, 100, 255, cv2.THRESH_BINARY)
    return imgResultat


def resize_image(img, largeur, hauteur):
    return cv2.resize(img, (largeur, hauteur))


def load_image(chemin, grayscale=True):
    mode = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    img = cv2.imread(str(chemin), mode)
    return img