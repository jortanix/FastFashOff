"""Fonctions d'affichage et interface utilisateur."""

import cv2
from data_marques import MARQUES_INFO, LOGO_TO_MARQUE


def afficher_info_boycott(nom_logo):
    """
    Affiche les informations de boycott pour une marque détectée.
    
    Args:
        nom_logo: nom du fichier logo (ex: "Zara-logo.jpg")
    """
    marque_key = LOGO_TO_MARQUE.get(nom_logo)
    
    if not marque_key or marque_key not in MARQUES_INFO:
        print(f"⚠️  Marque non reconnue: {nom_logo}")
        return
    
    info = MARQUES_INFO[marque_key]
    
    print("\n" + "="*70)
    print(f"🚨 MARQUE DÉTECTÉE: {info['nom_complet']}")
    print("="*70)
    print(f"\n📌 Contexte:")
    print(f"   {info['faits']}")
    print(f"\n❌ Raisons de boycotter:")
    for i, raison in enumerate(info['raisons'], 1):
        print(f"   {i}. {raison}")
    print(f"\n✅ Alternatives recommandées:")
    print(f"   {info['alternatives']}")
    print("="*70 + "\n")


def afficher_image_opencv(img, titre="Image", largeur=None, hauteur=None):
    """
    Affiche une image avec OpenCV.
    
    Args:
        img: image à afficher
        titre: titre de la fenêtre
        largeur: largeur de redimensionnement (optionnel)
        hauteur: hauteur de redimensionnement (optionnel)
    """
    if largeur and hauteur:
        img = cv2.resize(img, (largeur, hauteur))
    
    cv2.imshow(titre, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def afficher_resume(marques_detectees):
    """
    Affiche un résumé des marques détectées.
    
    Args:
        marques_detectees: liste de dictionnaires avec infos de détection
    """
    print("\n" + "="*70)
    print(f"📊 RÉSUMÉ DE L'ANALYSE".center(70))
    print("="*70)
    
    if marques_detectees:
        print(f"\n🚨 {len(marques_detectees)} marque(s) de fast fashion détectée(s):\n")
        for detection in marques_detectees:
            marque_nom = LOGO_TO_MARQUE.get(detection['logo'], "Inconnue")
            print(f"   • {marque_nom} ({detection['matches']} correspondances)")
        print(f"\n💡 Ces marques sont associées à:")
        print(f"   - Exploitation des travailleurs")
        print(f"   - Impact environnemental élevé")
        print(f"   - Modèle de surconsommation")
        print(f"\n✅ Privilégiez les alternatives durables et éthiques!")
    else:
        print("\n✓ Aucune marque de fast fashion détectée dans ces images.")
    
    print("="*70 + "\n")
