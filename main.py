"""
FastFashOff - Application de détection de logos de fast fashion
Point d'entrée principal en ligne de commande
"""

import argparse
import time
from pathlib import Path

from config import LOGOS, IMAGES, LOGO_DIR, IMAGE_DIR, MIN_MATCHES, SEUIL_DISTANCE
from image_processing import load_image, filter_image, resize_image
from logo_detection import (
    extraire_features_orb,
    matcher_logos_avec_ratio,
    filtrer_bons_matches,
    valider_detection,
    dessiner_matches
)
from display import afficher_info_boycott, afficher_image_opencv, afficher_resume
from utils import valider_structure_projet, afficher_statistiques_detection, generer_rapport_markdown


def analyser_dataset_complet(afficher_images=True, generer_rapport=False):
    print("\n FASTFASHOFF - Analyse en cours...".center(70))
    print("="*70 + "\n")
    
    debut = time.time()
    marques_detectees = []
    
    for i in range(len(IMAGES)):
        logo_path = LOGO_DIR / LOGOS[i]
        img_path = IMAGE_DIR / IMAGES[i]

        # Chargement
        imgLogo = load_image(logo_path, grayscale=True)
        img = load_image(img_path, grayscale=True)

        if imgLogo is None or img is None:
            print(f"Impossible de lire : {LOGOS[i]} ou {IMAGES[i]}")
            continue

        # Filtrage
        imgLogo_filtered = filter_image(imgLogo)
        img_filtered = filter_image(img)

        # Extraction ORB
        kp0, des0 = extraire_features_orb(imgLogo_filtered)
        kp1, des1 = extraire_features_orb(img_filtered)

        if des0 is None or des1 is None:
            print(f"Pas de descripteurs pour : {LOGOS[i]} ou {IMAGES[i]}")
            continue

        # Matching
        matches = matcher_logos_avec_ratio(des0, des1)
        good_matches = filtrer_bons_matches(matches, SEUIL_DISTANCE)
        
        # Validation de la détection
        if valider_detection(matches, MIN_MATCHES, SEUIL_DISTANCE):
            detection = {
                "logo": LOGOS[i],
                "image": IMAGES[i],
                "matches": len(good_matches),
                "distance_min": matches[0].distance if matches else 0
            }
            marques_detectees.append(detection)
            
            print(f"Logo détecté: {LOGOS[i]}")
            print(f"  - Bons matches: {len(good_matches)}")
            print(f"  - Distance minimale: {matches[0].distance:.1f}\n")

            # Affichage visuel
            if afficher_images:
                img_matches = dessiner_matches(imgLogo_filtered, kp0, img_filtered, kp1, matches, 25)
                afficher_image_opencv(img_matches, f"Détection - {LOGOS[i]}", 1200, 400)
            
            # Affichage des infos de boycott
            afficher_info_boycott(LOGOS[i])
        else:
            print(f"Pas de détection pour: {LOGOS[i]} vs {IMAGES[i]}")
            print(f"  - Matches trouvés: {len(good_matches)} (minimum requis: {MIN_MATCHES})\n")
    
    # Résumé et statistiques
    temps_ecoule = time.time() - debut
    afficher_resume(marques_detectees)
    afficher_statistiques_detection(marques_detectees)
    print(f"\nTemps d'exécution : {temps_ecoule:.2f}s\n")
    
    # Génération du rapport
    if generer_rapport and marques_detectees:
        generer_rapport_markdown(marques_detectees)


def analyser_image_specifique(nom_image, afficher_image=True):
    img_path = IMAGE_DIR / nom_image
    img = load_image(img_path, grayscale=True)
    
    if img is None:
        print(f"Impossible de lire l'image: {nom_image}")
        return
    
    print(f"\nAnalyse de: {nom_image}\n")
    img_filtered = filter_image(img)
    
    marques_trouvees = []
    
    for logo_name in LOGOS:
        logo_path = LOGO_DIR / logo_name
        imgLogo = load_image(logo_path, grayscale=True)
        
        if imgLogo is None:
            continue
        
        imgLogo_filtered = filter_image(imgLogo)
        
        kp0, des0 = extraire_features_orb(imgLogo_filtered)
        kp1, des1 = extraire_features_orb(img_filtered)
        
        if des0 is None or des1 is None:
            continue
        
        matches = matcher_logos_avec_ratio(des0, des1)
        good_matches = filtrer_bons_matches(matches, SEUIL_DISTANCE)
        
        if valider_detection(matches, MIN_MATCHES, SEUIL_DISTANCE):
            marques_trouvees.append({
                "logo": logo_name,
                "matches": len(good_matches),
                "distance_min": matches[0].distance
            })
            print(f"{logo_name} détecté ({len(good_matches)} matches)")
            
            if afficher_image:
                img_matches = dessiner_matches(imgLogo_filtered, kp0, img_filtered, kp1, matches, 25)
                afficher_image_opencv(img_matches, f"Détection - {logo_name}", 1200, 400)
    
    if marques_trouvees:
        print(f"\n{len(marques_trouvees)} marque(s) de fast fashion trouvée(s) dans cette image:\n")
        for detection in marques_trouvees:
            afficher_info_boycott(detection['logo'])
    else:
        print("\nAucune marque de fast fashion détectée!")


def main():
    #Fonction principale avec gestion des arguments en ligne de commande
    parser = argparse.ArgumentParser(
        description="FastFashOff - Détection de logos de fast fashion et sensibilisation au boycott"
    )
    
    parser.add_argument(
        "--mode",
        choices=["complet", "image"],
        default="complet",
        help="Mode d'analyse : 'complet' (tout le dataset) ou 'image' (une seule image)"
    )
    
    parser.add_argument(
        "--image",
        type=str,
        help="Nom de l'image à analyser (mode 'image' uniquement)"
    )
    
    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Ne pas afficher les images de matching (mode console uniquement)"
    )
    
    parser.add_argument(
        "--rapport",
        action="store_true",
        help="Générer un rapport Markdown des détections"
    )
    
    parser.add_argument(
        "--valider",
        action="store_true",
        help="Valider la structure du projet avant l'analyse"
    )
    
    args = parser.parse_args()
    
    # Validation de la structure du projet
    if args.valider:
        valide, message = valider_structure_projet()
        print(f"\n{'✓' if valide else '✗'} {message}\n")
        if not valide:
            return
    
    # Exécution selon le mode
    if args.mode == "complet":
        analyser_dataset_complet(
            afficher_images=not args.no_display,
            generer_rapport=args.rapport
        )
    elif args.mode == "image":
        if not args.image:
            print("Erreur : spécifiez une image avec --image <nom_fichier>")
            return
        analyser_image_specifique(args.image, afficher_image=not args.no_display)


if __name__ == "__main__":
    main()