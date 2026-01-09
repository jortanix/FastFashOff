#Base de données des marques de fast fashion et raisons de boycott

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
    },
    "Uniqlo": {
        "nom_complet": "Uniqlo (groupe Fast Retailing)",
        "raisons": [
            "Marque de fast-fashion (production de masse, renouvellement rapide des collections)",
            "Enquêtes en Chine montrant des heures supplémentaires massives, salaires très bas et conditions proches du travail en atelier de misère",
            "Accusations de travail forcé dans la chaîne de coton (Xinjiang), manque de preuves solides d’absence de travail forcé",
            "Empreinte carbone élevée liée à un modèle de production globalisé, avec surproduction et déchets textiles",
            "Utilisation de matières animales (laine, cuir, soie) et absence de certification généralisée sur les textiles, accusations de greenwashing"
        ],
        "faits": "ONG documentent 17h/jour en usines chinoises, salaires bas, produits chimiques sans protection. Coton Xinjiang lié au travail forcé sans preuves suffisantes. Modèle fast-fashion impactant malgré efforts RSE.",
        "alternatives": "Réduire les achats chez Uniqlo, privilégier des marques plus transparentes et certifiées (label GOTS, Fair Wear, etc.) ou la seconde main."
  },
  "Pull & Bear": {
  "nom_complet": "Pull & Bear (Inditex Group)",
  "raisons": [
    "Modèle fast-fashion avec surproduction et tendances jetables",
    "Conditions de travail précaires : semaines de 60-70h, salaires inférieurs au minimum vital dans les usines (ex. Bangladesh)",
    "Empreinte carbone massive (Inditex parmi les plus gros émetteurs, pas sur la bonne trajectoire des objectifs)",
    "Utilisation limitée de matériaux éco-friendly, déchets textiles élevés",
    "Produits chimiques toxiques dans les vêtements, accusations de greenwashing"
  ],
  "faits": "Éthique faible : audits/salaires insuffisants, usines à risques. CO2 élevé, peu durable, surproduction/déchets [web:16][web:17][web:21].",
  "alternatives": "Boycott ou limitation, seconde main, marques certifiées (GOTS, Fair Wear) ou slow fashion."
}
}

# Mapping nom de fichier logo dans MARQUES_INFO
LOGO_TO_MARQUE = {
    "Bershka-logo.png": "Bershka",
    "primark-logo.png": "Primark",
    "zara_logo.png": "Zara",
    "hm-logo.png": "H&M",
    "Shein-logo.png": "Shein",
    "uniqlo-logo.png": "Uniqlo",
    "Pull_Bear-logo.png": "Pull&Bear"
}
