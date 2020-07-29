SECRET_KEY = '7a36bc4a5382f20b75199da707a79b86'

PARSE_REGEX = [
    r".*adresse (de |d'|du )(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*adresse (de |d'|du )(.*)",
    r".*parle moi (de |d'|du )(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*parle moi (de |d'|du )(.*)",
    r".*parler (de |d'|du )(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*parler (de |d'|du )(.*)",
    r".*dire sur ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*dire sur ()(.*)",
    r".*histoire sur ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*histoire sur ()(.*)",
    r".*où est ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*où est ()(.*)",
    r".*sais sur ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    r".*sais sur ()(.*)"

]

ADDRESS_REGEX = [
    r".*Allée( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Avenue( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Boulevard( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Carrefour( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Chemin( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Chaussée( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Cité( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Corniche( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Cours( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Domaine( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Descente( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Ecart( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Esplanade( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Faubourg( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Grande Rue( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Hameau( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Halle( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Impasse( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Lieu-dit( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Lotissement( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Marché( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Montée( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Passage( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Place( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Plaine( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Plateau( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Promenade( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Parvis( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Quartier( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Quai( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Résidence( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Ruelle( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Rocade( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Rond-point( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Route( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Rue( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Sente( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Sentier( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Square( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Terre-plein( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Traverse( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Villa( de la | de l'| de | d'| du l'| du |\s)(.*)",
    r".*Village( de la | de l'| de | d'| du l'| du |\s)(.*)"
]

STRING_ERROR_PARSE = "Bot n'a pas comprit"
STRING_ERROR_ADDRESS = "Bot n'a trouvé d'address"
STRING_ERROR_WIKI = "Le wiki n'existe pas"
