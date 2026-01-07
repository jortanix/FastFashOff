"""Fonctions utilitaires pour FastFashOff."""

from pathlib import Path


def verifier_fichier_existe(chemin):
    """
    Vérifie si un fichier existe.
    
    Args:
        chemin: chemin du fichier (Path ou str)
        
    Returns:
        True si existe, False sinon
    """
    return Path(chemin).exists()


def lister_fichiers(dossier, extensions=None):
    """
    Liste les fichiers d'un dossier avec extensions spécifiques.
    
    Args:
        dossier: chemin du dossier (Path ou str)
        extensions: liste d'extensions (ex: ['.png', '.jpg']) ou None pour tout
        
    Returns:
        Liste de chemins (Path)
    """
    dossier = Path(dossier)
    
    if not dossier.exists():
        return []
    
    if extensions is None:
        return list(dossier.iterdir())
    
    fichiers = []
    for ext in extensions:
        fichiers.extend(dossier.glob(f"*{ext}"))
    
    return sorted(fichiers)


def creer_dossier_si_absent(chemin):
    """
    Crée un dossier s'il n'existe pas.
    
    Args:
        chemin: chemin du dossier (Path ou str)
        
    Returns:
        Path du dossier créé
    """
    dossier = Path(chemin)
    dossier.mkdir(parents=True, exist_ok=True)
    return dossier


def obtenir_nom_sans_extension(chemin):
    """
    Récupère le nom d'un fichier sans son extension.
    
    Args:
        chemin: chemin du fichier (Path ou str)
        
    Returns:
        Nom du fichier sans extension (str)
    """
    return Path(chemin).stem


def valider_structure_projet():
    """
    Vérifie que la structure du projet est correcte.
    
    Returns:
        (bool, str): (valide, message d'erreur si invalide)
    """
    from config import BASE_DIR, LOGO_DIR, IMAGE_DIR, LOGOS, IMAGES
    
    # Vérifier l'existence des dossiers
    if not LOGO_DIR.exists():
        return False, f"Dossier des logos introuvable : {LOGO_DIR}"
    
    if not IMAGE_DIR.exists():
        return False, f"Dossier des images introuvable : {IMAGE_DIR}"
    
    # Vérifier l'existence des fichiers logos
    for logo in LOGOS:
        chemin = LOGO_DIR / logo
        if not chemin.exists():
            return False, f"Logo introuvable : {chemin}"
    
    # Vérifier l'existence des fichiers images
    for image in IMAGES:
        chemin = IMAGE_DIR / image
        if not chemin.exists():
            return False, f"Image introuvable : {chemin}"
    
    return True, "Structure du projet valide"


def afficher_statistiques_detection(resultats):
    """
    Calcule et affiche des statistiques de détection.
    
    Args:
        resultats: liste de dictionnaires avec clés 'logo', 'matches', 'distance_min'
    """
    if not resultats:
        print("Aucune détection à analyser.")
        return
    
    total_matches = sum(r['matches'] for r in resultats)
    moyenne_matches = total_matches / len(resultats)
    
    distances = [r['distance_min'] for r in resultats]
    distance_moyenne = sum(distances) / len(distances)
    distance_min = min(distances)
    distance_max = max(distances)
    
    print("\n📈 Statistiques de détection:")
    print(f"   Nombre de détections : {len(resultats)}")
    print(f"   Matches total : {total_matches}")
    print(f"   Moyenne matches/détection : {moyenne_matches:.1f}")
    print(f"   Distance minimale : {distance_min:.1f}")
    print(f"   Distance maximale : {distance_max:.1f}")
    print(f"   Distance moyenne : {distance_moyenne:.1f}")


def formater_temps(secondes):
    """
    Formate un temps en secondes en format lisible.
    
    Args:
        secondes: temps en secondes (float)
        
    Returns:
        Chaîne formatée (str)
    """
    if secondes < 1:
        return f"{secondes*1000:.0f}ms"
    elif secondes < 60:
        return f"{secondes:.2f}s"
    else:
        minutes = int(secondes // 60)
        secs = secondes % 60
        return f"{minutes}min {secs:.0f}s"


def sauvegarder_resultat(chemin_sortie, img, nom_fichier):
    """
    Sauvegarde une image de résultat.
    
    Args:
        chemin_sortie: dossier de sortie (Path ou str)
        img: image à sauvegarder (numpy array)
        nom_fichier: nom du fichier de sortie
        
    Returns:
        True si succès, False sinon
    """
    import cv2
    
    chemin_sortie = Path(chemin_sortie)
    creer_dossier_si_absent(chemin_sortie)
    
    chemin_complet = chemin_sortie / nom_fichier
    
    try:
        cv2.imwrite(str(chemin_complet), img)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False


def charger_image_depuis_url(url):
    """
    Charge une image depuis une URL (pour extension future).
    
    Args:
        url: URL de l'image
        
    Returns:
        Image (numpy array) ou None si erreur
    """
    try:
        import urllib.request
        import cv2
        import numpy as np
        
        with urllib.request.urlopen(url) as response:
            data = response.read()
        
        arr = np.asarray(bytearray(data), dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
        return img
    except Exception as e:
        print(f"Erreur lors du chargement depuis URL : {e}")
        return None


def generer_rapport_markdown(marques_detectees, fichier_sortie="rapport_detection.md"):
    """
    Génère un rapport Markdown des détections.
    
    Args:
        marques_detectees: liste de détections
        fichier_sortie: nom du fichier de sortie
    """
    from data_marques import LOGO_TO_MARQUE, MARQUES_INFO
    from datetime import datetime
    
    contenu = f"# Rapport FastFashOff\n\n"
    contenu += f"**Date**: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
    contenu += f"## Résumé\n\n"
    contenu += f"Nombre de marques détectées : **{len(marques_detectees)}**\n\n"
    
    if marques_detectees:
        contenu += "## Marques détectées\n\n"
        
        for detection in marques_detectees:
            marque_key = LOGO_TO_MARQUE.get(detection['logo'])
            if marque_key and marque_key in MARQUES_INFO:
                info = MARQUES_INFO[marque_key]
                contenu += f"### {info['nom_complet']}\n\n"
                contenu += f"- **Correspondances** : {detection['matches']}\n"
                contenu += f"- **Distance minimale** : {detection['distance_min']:.1f}\n\n"
                contenu += f"**Contexte** : {info['faits']}\n\n"
                contenu += "**Raisons de boycotter** :\n"
                for raison in info['raisons']:
                    contenu += f"- {raison}\n"
                contenu += f"\n**Alternatives** : {info['alternatives']}\n\n"
                contenu += "---\n\n"
    else:
        contenu += "Aucune marque de fast fashion détectée.\n"
    
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        f.write(contenu)
    
    print(f"✓ Rapport généré : {fichier_sortie}")