import cv2
import numpy as np
from config import ORB_FEATURES, SEUIL_DISTANCE, MIN_MATCHES


def extraire_features_orb(img, nfeatures=ORB_FEATURES):
    #on extrait les keypoints et descripteurs ORB d'une image
    orb = cv2.ORB_create(nfeatures=nfeatures)
    kp, des = orb.detectAndCompute(img, None)
    return kp, des


def matcher_logos(des_logo, des_image, ratio=0.75):
    if des_logo is None or des_image is None:
        return []
    #on utilise le matcher brut force comme vu en TD
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(des_logo, des_image, k=2)
    
    #on filtre les bons matches
    good_matches = []
    for match_pair in matches:
        if len(match_pair) == 2:
            m,n = match_pair
            #On garde seulement les matches qui passent le test du ratio
            if m.distance < ratio * n.distance:
                good_matches.append(m)
    #on retourne les matches triés par distance
    return sorted(good_matches, key=lambda x: x.distance)


def filtrer_bons_matches(matches, seuil=SEUIL_DISTANCE):
    #On filtre les matches selon la distance maximale autorisée
    return [m for m in matches if m.distance < seuil]


def valider_detection(matches, min_matches=MIN_MATCHES, seuil=SEUIL_DISTANCE):
    #on vérifie si la détection est considérée comme valide
    bons_matches = filtrer_bons_matches(matches, seuil)
    return len(bons_matches) >= min_matches


def dessiner_matches(img_logo, kp_logo, img_cible, kp_cible, matches, nb_matches=25):
    if kp_logo == [] or kp_cible == [] or matches == []:
        print("pas de keypoints ou pas de matches, aucun dessin possible")
        return None
    img_matches = cv2.drawMatches(
        img_logo, kp_logo, img_cible, kp_cible, matches[:nb_matches], None,
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
    )
    return img_matches



def valider_avec_homographie(kp_logo, kp_image, matches, min_inliers=10):
    if len(matches) < min_inliers:
        return False, 0
    
    #on extrait les points correspondants des keypoints
    points_logo = []
    points_image = []
    for m in matches:
        points_logo.append(kp_logo[m.queryIdx].pt)      #.pt donne les coordonnées (x,y), méthode trouver sur ce site :
        points_image.append(kp_image[m.trainIdx].pt)    #https://www.opencv.org.cn/opencvdoc/2.3.1/html/modules/features2d/doc/common_interfaces_of_feature_detectors.html
    src_pts = np.array(points_logo, dtype=np.float32).reshape(-1, 1, 2)
    dst_pts = np.array(points_image, dtype=np.float32).reshape(-1, 1, 2)
    #on met les points dans le bon format
    #https://numpy.org/doc/stable/reference/generated/numpy.reshape.html

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    if M is None:
        return False, 0
    #on compte les correspondances qui respectent la transformation trouvée

    inliers = mask.ravel().sum()
    ratio_inliers = inliers / len(matches)
    
    #On considère la détection valide si au moins 50% des matches sont cohérents
    return ratio_inliers > 0.5, inliers

#Lien wikipédia qui explique la méthode ci-dessus : https://fr.wikipedia.org/wiki/RANSAC
