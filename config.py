#Chemins et configuration du projet

from pathlib import Path

# Chemins
BASE_DIR = Path(__file__).resolve().parent
LOGO_DIR = BASE_DIR / "data" / "logo"
IMAGE_DIR = BASE_DIR / "data" / "dataset"

# Listes des fichiers
LOGOS = [
    "Bershka-logo.png",
    "primark-logo.png",
    "zara_logo.png",
    "hm-logo.png",
    "Shein-logo.png",
    "uniqlo-logo.png",
    "Pull_Bear-logo.png"
]

IMAGES = [
    "BERSHKA.jpg",
    "PRIMARK.jpg",
    "ZARA.jpeg",
    "H&M.jpg",
    "SHEIN.jpeg"
]

# Paramètres de détection
SEUIL_DISTANCE = 30      # distance maximale pour un bon match
MIN_MATCHES = 20          # nombre minimum de matches pour valider une détection
ORB_FEATURES = 1000        # nombre de features ORB à extraire