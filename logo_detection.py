"""Détection de logos avec ORB et matching."""

import cv2
from config import ORB_FEATURES, SEUIL_DISTANCE, MIN_MATCHES


def extraire_features_orb(img, nfeatures=ORB_FEATURES):
    """
    Extrait les keypoints et descripteurs ORB d'une image.
    
    Args:
        img: image en niveaux de gris
        nfeatures: nombre de features à extraire
        
    Returns:
        (keypoints, descripteurs) ou (None, None) si erreur
    """
    orb = cv2.ORB_create(nfeatures=nfeatures)
    kp, des = orb.detectAndCompute(img, None)
    return kp, des


def matcher_logos_avec_ratio(des_logo, des_image, ratio=0.75):
    """
    Matching avec ratio test pour éliminer les faux positifs.
    
    Args:
        des_logo: descripteurs du logo
        des_image: descripteurs de l'image
        ratio: seuil du ratio test (0.75 recommandé)
        
    Returns:
        Liste de bons matches
    """
    if des_logo is None or des_image is None:
        return []
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(des_logo, des_image, k=2)
    
    # Ratio test de Lowe
    good_matches = []
    for match_pair in matches:
        if len(match_pair) == 2:
            m, n = match_pair
            if m.distance < ratio * n.distance:
                good_matches.append(m)
    
    return sorted(good_matches, key=lambda x: x.distance)


def filtrer_bons_matches(matches, seuil=SEUIL_DISTANCE):
    """
    Filtre les matches ayant une distance inférieure au seuil.
    
    Args:
        matches: liste de matches
        seuil: distance maximale
        
    Returns:
        Liste de bons matches
    """
    return [m for m in matches if m.distance < seuil]


def valider_detection(matches, min_matches=MIN_MATCHES, seuil=SEUIL_DISTANCE):
    """
    Valide si une détection est positive.
    
    Args:
        matches: liste de matches
        min_matches: nombre minimum de bons matches
        seuil: seuil de distance
        
    Returns:
        True si détection valide, False sinon
    """
    bons_matches = filtrer_bons_matches(matches, seuil)
    return len(bons_matches) >= min_matches


def dessiner_matches(img_logo, kp_logo, img_cible, kp_cible, matches, nb_matches=25):
    """
    Dessine les matches entre logo et image.
    
    Args:
        img_logo: image du logo
        kp_logo: keypoints du logo
        img_cible: image cible
        kp_cible: keypoints de l'image cible
        matches: liste de matches
        nb_matches: nombre de matches à afficher
        
    Returns:
        Image avec les matches dessinés
    """
    img_matches = cv2.drawMatches(
        img_logo, kp_logo, img_cible, kp_cible, matches[:nb_matches], None,
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
    )
    return img_matches
