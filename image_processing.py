"""Fonctions de traitement d'images pour FastFashOff."""

import cv2
import numpy as np


def filter_image(img):
    """
    Filtre optimisé pour la détection de logos géométriques.
    Applique : blur + Canny + dilatation + seuillage.
    
    Args:
        img: image en niveaux de gris (numpy array)
        
    Returns:
        Image filtrée (numpy array)
    """
    imgFlou = cv2.GaussianBlur(img, (5, 5), 0)
    contours = cv2.Canny(imgFlou, 50, 150, 3)
    elementStructurant = np.ones((3, 3), np.uint8)
    contoursDilates = cv2.dilate(contours, elementStructurant)
    _, imgResultat = cv2.threshold(contoursDilates, 100, 255, cv2.THRESH_BINARY)
    return imgResultat


def resize_image(img, largeur, hauteur):
    """
    Redimensionne une image.
    
    Args:
        img: image (numpy array)
        largeur: nouvelle largeur
        hauteur: nouvelle hauteur
        
    Returns:
        Image redimensionnée
    """
    return cv2.resize(img, (largeur, hauteur))


def load_image(chemin, grayscale=True):
    """
    Charge une image depuis un chemin.
    
    Args:
        chemin: chemin du fichier (Path ou str)
        grayscale: si True, charge en niveaux de gris
        
    Returns:
        Image (numpy array) ou None si erreur
    """
    mode = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    img = cv2.imread(str(chemin), mode)
    return img
