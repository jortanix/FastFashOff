#Chemins et configuration du projet

from pathlib import Path

#Chemins permettant d'accéder aux dossiers de logos et d'images en jupiter notebook
#méthode trouver sur internet : https://docs.python.org/fr/3.13/library/pathlib.html#pathlib.Path.resolve

BASE_DIR = Path(__file__).resolve().parent
LOGO_DIR = BASE_DIR / "data" / "logo"
IMAGE_DIR = BASE_DIR / "data" / "dataset"

#Listes des fichiers des logos pour les tests
LOGOS = [
    "Bershka-logo.png",
    "primark-logo.png",
    "zara_logo.png",
    "hm-logo.png",
    "Shein-logo.png",
    "uniqlo-logo.png",
    "Pull_Bear-logo.png"
]


#Listes des fichiers des images a tester
IMAGES = [
    "BERSHKA.jpg",
    "PRIMARK.jpg",
    "ZARA.jpeg",
    "H&M.jpg",
    "SHEIN.jpeg"
]

#Paramètres de détection pour les méthodes utiliser dans le main
SEUIL_DISTANCE = 50      #distance maximale pour un bon match
MIN_MATCHES = 10         #nombre minimum de matches pour valider une détection
ORB_FEATURES = 1000      #nombre de features ORB à extraire
