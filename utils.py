import cv2
from pathlib import Path
import urllib.request
import numpy as np
from datetime import datetime

from data_marques import LOGO_TO_MARQUE, MARQUES_INFO

def verifier_fichier_existe(chemin):
    return Path(chemin).exists()

def lister_fichiers(dossier, extensions=None):
    dossier = Path(dossier)
    if dossier.exists() == False:
        return []
    fichiers = []

    for fichier in dossier.iterdir(): #renvoie tous les éléments (fichiers et sous-dossiers) sans les parcourir
        if fichier.is_file():
            if extensions == None or fichier.suffix in extensions:
                fichiers.append(fichier)
    return sorted(fichiers)

def creer_dossier_si_absent(chemin):
    dossier = Path(chemin)
    dossier.mkdir(parents=True, exist_ok=True)
    return dossier

def obtenir_nom_sans_extension(chemin):
    return Path(chemin).stem 
    #renvoie le nom du fichier sans l'extension, propriété de Pathlib

def valider_structure_projet():
    from config import BASE_DIR, LOGO_DIR, IMAGE_DIR, LOGOS, IMAGES

    #On vérifie l'existence des dossiers
    if LOGO_DIR.exists() == False:
        return False, "Dossier des logos introuvable :" + str(LOGO_DIR)
    if IMAGE_DIR.exists() == False:
        return False, "Dossier des images introuvable :" + str(IMAGE_DIR)
    
    #On vérifie l'existence des fichiers logos
    for logo in LOGOS:
        chemin = LOGO_DIR / logo
        if chemin.exists() == False:
            return False, "Logo introuvable :" + str(chemin)
    
    #On vérifie l'existence des fichiers images
    for image in IMAGES:
        chemin = IMAGE_DIR / image
        if chemin.exists() == False:
            return False, "Image introuvable :" + str(chemin)

    return True, "Structure du projet valide"


def afficher_statistiques_detection(resultats):
    if not resultats:
        print("Aucune détection à analyser.")
        return
    
    total_matches = 0 
    for res in resultats:
        total_matches += res['matches']
    moyenne_matches = total_matches/len(resultats)

    distances = []
    for resultat in resultats:
        distances.append(resultat['distance_min'])

    distance_moyenne = sum(distances) / len(distances)
    distance_min = min(distances)
    distance_max = max(distances)
    
    print("Statistiques de détection:")
    print("  Nombre de détections : " + str(len(resultats)))
    print("  Matches total : " + str(total_matches))
    print("  Moyenne matches/détection : " + str(round(moyenne_matches, 1)))
    print("  Distance minimale : " + str(round(distance_min, 1)))
    print("  Distance maximale : " + str(round(distance_max, 1)))
    print("  Distance moyenne : " + str(round(distance_moyenne, 1)))

def formater_temps(secondes):
    if secondes < 1:
        millisecondes = round(secondes * 1000)
        return str(millisecondes) + "ms"
    elif secondes < 60:
        return str(round(secondes, 2)) + "s"
    else:
        minutes = int(secondes // 60)
        secondes_restantes = round(secondes % 60)
        return str(minutes) + "min " + str(secondes_restantes) + "s"
    
def sauvegarder_resultat(chemin_sortie, img, nom_fichier):
    chemin_sortie = Path(chemin_sortie)
    creer_dossier_si_absent(chemin_sortie)
    chemin_complet = chemin_sortie / nom_fichier
    try:
        cv2.imwrite(str(chemin_complet), img)
        return True
    except Exception as e:
        print("Erreur lors de la sauvegarde : " + str(e))
        return False

def charger_image_depuis_url(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        arr = np.asarray(bytearray(data), dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
        return img
    except Exception as e:
        print("Erreur lors du chargement depuis URL : " + str(e))
        return None



def generer_rapport_markdown(marques_detectees, fichier_sortie="rapport_detection.md"):
    contenu = "# Rapport FastFashOff\n\n"
    contenu += "**Date**: " + datetime.now().strftime('%d/%m/%Y %H:%M') + "\n\n"
    contenu += "## Résumé\n\n"
    contenu += "Nombre de marques détectées : **" + str(len(marques_detectees)) + "**\n\n"
    
    if marques_detectees:
        contenu += "## Marques détectées\n\n"
        
        for detection in marques_detectees:
            marque_key = LOGO_TO_MARQUE.get(detection['logo'])
            if marque_key and marque_key in MARQUES_INFO:
                info = MARQUES_INFO[marque_key]
                contenu += "### " + info['nom_complet'] + "\n\n"
                contenu += "- **Correspondances** : " + str(detection['matches']) + "\n"
                contenu += "- **Distance minimale** : " + str(round(detection['distance_min'], 1)) + "\n\n"
                contenu += "**Contexte** : " + info['faits'] + "\n\n"
                contenu += "**Raisons de boycotter** :\n"
                for raison in info['raisons']:
                    contenu += "- " + raison + "\n"
                contenu += "\n**Alternatives** : " + info['alternatives'] + "\n\n"
                contenu += "---\n\n"
    else:
        contenu += "Aucune marque de fast fashion détectée.\n"
    
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        f.write(contenu)
    
    print("Rapport généré : " + fichier_sortie)