# FastFashOff

FastFashOff est une application de **recherche d’image par contenu** qui analyse une image donnée pour détecter la présence de logos de grandes marques de fast fashion (Zara, H&M, Shein, Primark, Bershka) et informer l’utilisateur des raisons pour lesquelles ces marques sont régulièrement appelées au boycott. [file:2]

## Contexte et objectifs

Dans un contexte de surconsommation textile, FastFashOff vise à sensibiliser les consommateurs à l’envers du décor de l’industrie de la mode, en rendant visibles les impacts sociaux et environnementaux associés à certaines marques. [file:2]

Objectifs principaux : [file:1][file:2]  
- Reconnaitre automatiquement les logos des marques ciblées dans une image.  
- Associer à chaque marque détectée un court descriptif expliquant pourquoi elle est controversée.  
- Proposer une interface simple permettant de tester facilement différentes images et jeux de données.

## Fonctionnalités

- Détection de logos dans une image (photos de vêtements, produits, affiches, etc.). [file:2]  
- Utilisation d’un algorithme de description locale (SIFT, SURF ou ORB) pour comparer une imagette de logo à un jeu d’images plus grandes. [file:1]  
- Interface utilisateur simple (console / notebook) permettant :  
  - de choisir l’image à analyser,  
  - de sélectionner le jeu de données,  
  - d’afficher les correspondances entre logos et images. [file:1]

## Technologies

- Langage : **Python**. [file:1]  
- Bibliothèques principales :  
  - **OpenCV** (détection, description et matching de caractéristiques locales).  
  - **NumPy** pour la manipulation des matrices d’images.  
  - **Matplotlib** pour l’affichage optionnel des résultats dans le notebook.  

## Jeu de données

Le jeu de données est composé d’images de logos et d’images de contexte liées aux marques : Zara, H&M, Shein, Primark, Bershka. [file:2]  

Structure du dossier :

```text
data/
  logo/
    Bershka-logo.png
    hm-logo.png
    primark-logo.png
    Shein-logo.png
    zara_logo.jpg
    ...
  dataset/
    BERSHKA.jpg
    H&M.jpg
    PRIMARK.jpg
    SHEIN.jpeg
    ZARA.jpeg
    ...
```

Les imagettes utilisées pour la recherche ne doivent pas appartenir directement à la collection des grandes images, conformément aux consignes du projet. [file:1]

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/jortanix/FastFashOff.git
cd FastFashOff
```

Créer un environnement virtuel (optionnel mais recommandé), puis installer les dépendances de base :

```bash
pip install opencv-python opencv-contrib-python numpy matplotlib
```

Adapte cette section si tu ajoutes un `requirements.txt`.

## Utilisation

### Notebook `main.ipynb`

Le notebook `main.ipynb` contient :

- Les fonctions utilitaires :  
  - affichage des images du dataset et des logos,  
  - redimensionnement et filtrage (blur, Canny, dilatation, seuillage).  
- L’algorithme de test `main_for_test()` :  
  - applique un filtre aux logos et aux images,  
  - extrait les descripteurs ORB,  
  - effectue un matching par brute force,  
  - affiche les meilleurs matches pour visualiser la détection. [file:96][file:1]

Pour lancer le notebook :

```bash
jupyter notebook main.ipynb
```

ou via VS Code (Jupyter intégré).

### Exécution utilisateur

Une fonction `main_for_user()` permet de saisir le nom d’une image à analyser et d’afficher le résultat, à partir du jeu de données présent dans `data/dataset`. [file:96]

## Contexte pédagogique

Ce projet est réalisé dans le cadre de l’UE **35LIAC04 – Informatique graphique et vision** (Université Lyon 2), et a pour objectif la mise en œuvre d’une application de recherche d’image par contenu utilisant Python et OpenCV. [file:1]  

Le rapport associé doit notamment : [file:1]  
1. Présenter le but et l’intérêt de FastFashOff.  
2. Décrire les choix techniques (algorithmes, implémentation).  
3. Montrer les cas de succès/échec sur le jeu de données.  
4. Discuter les difficultés rencontrées et les perspectives d’amélioration.
