# FastFashOff

FastFashOff est une application de **recherche d’image par contenu** qui analyse une image donnée pour détecter la présence de logos de grandes marques de fast fashion (Zara, H&M, Shein, Primark, Bershka) et informer l’utilisateur des raisons pour lesquelles ces marques sont régulièrement appelées au boycott. [file:2]

## Contexte et objectifs

Dans un contexte de surconsommation textile, FastFashOff vise à sensibiliser les consommateurs à l’envers du décor de l’industrie de la mode, en rendant visibles les impacts sociaux et environnementaux associés à certaines marques. [file:2]

Objectifs principaux : [file:1][file:2]  
- Reconnaitre automatiquement les logos des marques ciblées dans une image.  
- Associer à chaque marque détectée un court descriptif expliquant pourquoi elle est controversée.  
- Proposer une interface simple permettant de tester facilement différentes images et jeux de données.

## Fonctionnalités

- Détection de logos dans une image (photos de vêtements, produits, affiches, etc.). [file:1][file:2]  
- Utilisation d’un algorithme de description locale (SIFT, SURF ou ORB) pour comparer une imagette de logo à un jeu d’images plus grandes. [file:1]  
- Interface utilisateur simple (console ou notebook) permettant :  
  - de choisir l’image à analyser,  
  - de sélectionner le jeu de données,  
  - d’afficher les logos détectés et les explications associées. [file:1]

## Technologies

- Langage : **Python**. [file:1]  
- Bibliothèque principale : **OpenCV** (détection, description et comparaison de caractéristiques locales). [file:1]  
- Algorithmes possibles : **SIFT**, **SURF** ou **ORB** (au moins un utilisé dans le projet). [file:1]

## Jeu de données

Le jeu de données est composé d’images de logos et d’images de contexte liées aux marques : Zara, H&M, Shein, Primark, Bershka. [file:2]  

Structure possible du dossier `data/` :  
- `data/logos/` : imagettes de logos (une ou plusieurs par marque).  
- `data/images/` : images plus grandes sur lesquelles rechercher les logos. [file:1]

Les imagettes utilisées pour la recherche ne doivent pas appartenir directement à la collection des grandes images, conformément aux consignes du projet. [file:1]
