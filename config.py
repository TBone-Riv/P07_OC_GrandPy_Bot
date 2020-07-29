SECRET_KEY = '7a36bc4a5382f20b75199da707a79b86'

PARSE_REGEX = [
    ".*adresse (de |d'|du )(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*adresse (de |d'|du )(.*)",
    ".*parle moi (de |d'|du )(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*parle moi (de |d'|du )(.*)",
    ".*parler (de |d'|du )(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*parler (de |d'|du )(.*)",
    ".*dire sur ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*dire sur ()(.*)",
    ".*histoire sur ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*histoire sur ()(.*)",
    ".*où est ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*où est ()(.*)",
    ".*sais sur ()(.*)(\ss'il.*$|\s\?.*$|\sstp)",
    ".*sais sur ()(.*)"

]

ADDRESS_REGEX = [
    ".*Allée( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Avenue( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Boulevard( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Carrefour( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Chemin( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Chaussée( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Cité( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Corniche( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Cours( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Domaine( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Descente( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Ecart( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Esplanade( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Faubourg( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Grande Rue( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Hameau( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Halle( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Impasse( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Lieu-dit( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Lotissement( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Marché( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Montée( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Passage( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Place( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Plaine( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Plateau( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Promenade( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Parvis( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Quartier( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Quai( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Résidence( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Ruelle( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Rocade( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Rond-point( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Route( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Rue( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Sente( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Sentier( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Square( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Terre-plein( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Traverse( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Villa( de la | de l'| de | d'| du l'| du |\s)(.*)",
    ".*Village( de la | de l'| de | d'| du l'| du |\s)(.*)"
]

STRING_ERROR_PARSE = "Bot n'a pas comprit"
STRING_ERROR_ADDRESS = "Bot n'a trouvé d'address"
STRING_ERROR_WIKI = "Le wiki n'existe pas"
