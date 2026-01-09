import cv2
from data_marques import MARQUES_INFO, LOGO_TO_MARQUE


def afficher_info_boycott(nom_logo):
    marque_key = LOGO_TO_MARQUE.get(nom_logo)

    if not marque_key or marque_key not in MARQUES_INFO:
        print("Marque non reconnue: " + nom_logo)
        return
    
    info = MARQUES_INFO[marque_key]
    
    print("\nMARQUE DÉTECTÉE: " + info['nom_complet'])
    print("\nContexte:")
    print("   "+info['faits'])
    print("\nRaisons de boycotter:")
    for i, raison in enumerate(info['raisons'], 1):
        print("   " + str(i) + ". " + raison)
    print("\nAlternatives recommandées:")
    print("   "+info['alternatives'])



def afficher_image_opencv(img, titre="Image", largeur=None, hauteur=None):
    if largeur != None and hauteur != None: #on vérifie la taille
        img = cv2.resize(img, (largeur, hauteur)) #on redimensionne si jamais
    
    cv2.imshow(titre, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def afficher_resume(marques_detectees):
    print("\nRÉSUMÉ DE L'ANALYSE")
    if marques_detectees:
        print(str(len(marques_detectees)) + " marque de fast fashion détectée:")
        for detection in marques_detectees:
            marque_nom = LOGO_TO_MARQUE.get(detection['logo'], "Inconnue")
            print("   - " + marque_nom + " (" + str(detection['matches']) + " correspondances)")
        print("\nCes marques sont associées à:")
        print("   - Exploitation des travailleurs")
        print("   - Impact environnemental élevé")
        print("   - Modèle de surconsommation")
        print("\nPrivilégiez les alternatives durables et éthiques!")
    else:
        print("Aucune marque de fast fashion détectée dans ces images.")