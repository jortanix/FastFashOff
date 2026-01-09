"""Détection de logos avec ORB et matching."""

import cv2
from config import ORB_FEATURES, SEUIL_DISTANCE, MIN_MATCHES


def extraire_features_orb(img, nfeatures=ORB_FEATURES):
    """Extrait les keypoints et descripteurs ORB d'une image."""
    orb = cv2.ORB_create(nfeatures=nfeatures)
    kp, des = orb.detectAndCompute(img, None)
    return kp, des


def matcher_logos(des_logo, des_image, ratio=0.75):
    """Matching avec ratio test de Lowe pour éliminer les faux positifs."""
    if des_logo is None or des_image is None:
        return []
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(des_logo, des_image, k=2)
    
    good_matches = []
    for match_pair in matches:
        if len(match_pair) == 2:
            m, n = match_pair
            if m.distance < ratio * n.distance:
                good_matches.append(m)
    
    return sorted(good_matches, key=lambda x: x.distance)


def filtrer_bons_matches(matches, seuil=SEUIL_DISTANCE):
    """Filtre les matches ayant une distance inférieure au seuil."""
    return [m for m in matches if m.distance < seuil]


def valider_detection(matches, min_matches=MIN_MATCHES, seuil=SEUIL_DISTANCE):
    """Valide si une détection est positive."""
    bons_matches = filtrer_bons_matches(matches, seuil)
    return len(bons_matches) >= min_matches


def dessiner_matches(img_logo, kp_logo, img_cible, kp_cible, matches, nb_matches=25):
    """Dessine les matches entre logo et image."""
    img_matches = cv2.drawMatches(
        img_logo, kp_logo, img_cible, kp_cible, matches[:nb_matches], None,
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
    )
    return img_matches

def valider_avec_homographie(kp_logo, kp_image, matches, min_inliers=10):
    """
    Valide les matches avec une transformation homographique (RANSAC).
    Retourne (valide, nb_inliers).
    """
    if len(matches) < min_inliers:
        return False, 0
    
    import numpy as np
    
    # Extraire les points correspondants
    src_pts = np.float32([kp_logo[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp_image[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    
    # Trouver l'homographie avec RANSAC
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    
    if M is None:
        return False, 0
    
    # Compter les inliers
    inliers = mask.ravel().sum()
    ratio_inliers = inliers / len(matches)
    
    # Au moins 50% des matches doivent être géométriquement cohérents
    return ratio_inliers > 0.5, inliers