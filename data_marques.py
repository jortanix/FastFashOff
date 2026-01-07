"""Base de données des marques de fast fashion et raisons de boycott."""

# Informations complètes sur chaque marque
MARQUES_INFO = {
    "Bershka": {
        "nom_complet": "Bershka (groupe Inditex)",
        "raisons": [
            "Conditions de travail précaires dans les usines sous-traitantes",
            "Salaires en dessous du seuil de subsistance dans plusieurs pays",
            "Production de masse encourageant la surconsommation",
            "Impact environnemental élevé (eau, produits chimiques, déchets textiles)"
        ],
        "faits": "Fait partie du groupe Inditex. Plusieurs scandales liés aux conditions de travail en Asie et en Amérique latine.",
        "alternatives": "Vêtements de seconde main, marques éthiques certifiées (Fair Wear, GOTS)"
    },
    "Primark": {
        "nom_complet": "Primark",
        "raisons": [
            "Salaires très bas et horaires excessifs pour les ouvriers",
            "Absence de transparence sur la chaîne d'approvisionnement",
            "Modèle économique basé sur l'ultra fast-fashion",
            "Utilisation massive de matières polluantes (polyester)"
        ],
        "faits": "Impliqué dans l'effondrement du Rana Plaza (Bangladesh, 2013) qui a tué plus de 1100 personnes.",
        "alternatives": "Friperies, location de vêtements, marques responsables"
    },
    "Zara": {
        "nom_complet": "Zara (groupe Inditex)",
        "raisons": [
            "Rythme de production effréné (nouvelles collections toutes les 2 semaines)",
            "Exploitation des travailleurs dans les pays en développement",
            "Gaspillage textile massif (invendus détruits)",
            "Empreinte carbone élevée due à la logistique mondiale"
        ],
        "faits": "Leader mondial de la fast fashion. Inditex est régulièrement pointé du doigt pour ses pratiques sociales et environnementales.",
        "alternatives": "Mode durable, upcycling, marques locales et transparentes"
    },
    "H&M": {
        "nom_complet": "H&M (Hennes & Mauritz)",
        "raisons": [
            "Pratiques de greenwashing (communication trompeuse sur l'écologie)",
            "Salaires insuffisants pour les ouvriers du textile",
            "Tonnes de vêtements invendus brûlés chaque année",
            "Conditions de travail dangereuses dans les usines partenaires"
        ],
        "faits": "Malgré ses initiatives 'Conscious', H&M reste un acteur majeur de la fast fashion avec un impact environnemental considérable.",
        "alternatives": "Achats responsables, réparation de vêtements, marques éthiques"
    },
    "Shein": {
        "nom_complet": "Shein",
        "raisons": [
            "Modèle ultra fast-fashion le plus extrême (milliers de nouveaux produits par jour)",
            "Conditions de travail déplorables (journées de 18h, pas de jour de repos)",
            "Qualité très faible encourageant le jetable",
            "Empreinte carbone gigantesque (production en Chine, livraison mondiale)",
            "Produits chimiques dangereux détectés dans les vêtements"
        ],
        "faits": "Enquêtes récentes révèlent des conditions proches de l'esclavage moderne. Aucune transparence sur la chaîne de production.",
        "alternatives": "Boycott total recommandé, privilégier qualité et durabilité"
    }
}

# Mapping nom de fichier logo -> clé dans MARQUES_INFO
LOGO_TO_MARQUE = {
    "Bershka-logo.png": "Bershka",
    "primark-logo.png": "Primark",
    "zara_logo.jpg": "Zara",
    "hm-logo.png": "H&M",
    "Shein-logo.png": "Shein"
}
