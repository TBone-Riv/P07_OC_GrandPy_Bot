parse_sample = [
    ("""Que peut tu me dire sur l'école de Nante ?""",
     """l'école de Nante"""),
    ("""parle moi du puy du fou""",
     """puy du fou"""),
    ("""Done moi l'adresse d'Openclassrooms stp""",
     """Openclassrooms"""),
    ("""raconte moi une histoire sur la gare de Lyon s'il te plait""",
     """la gare de Lyon""")]

address_sample = [
    ("""la maire d'artas""",
     {'candidates': [{
         'formatted_address': 'Place du 8 mai 1945, 38440 Artas, France',
         'geometry': {'location': {'lat': 45.5363785,
                                   'lng': 5.1675587}},
         'name': 'Mairie'}], 'status': 'OK'},
     ("Mairie", "Place du 8 mai 1945, 38440 Artas, France",
      {'lat': 45.5363785, 'lng': 5.1675587})
     ),
    ("""j'aime le code""",
     {'candidates': [], 'status': 'ZERO_RESULTS'},
     (None, None, {"lat": 0, "lng": 0}))
]

parse_address = [
    ("Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
     ['', 'Champ de Mars', 'Anatole France', 'Paris', 'France'])
]

info_sample = [
    ('Champ de Mars',
     {'query': {'pages': [
         {'extract': "Champ de Mars o" +
                     "u Champ-de-Mars est un nom de lieu, généralement" +
                     " urbain, faisant à la fois référence au dieu Mar" +
                     "s et au mois de mars (qui lui était autrefois dé" +
                     "dié). La fonction du « champ de Mars » a évolué " +
                     "au cours du temps.\n\n\n== Antiquité ==\nLe Cham" +
                     "p de Mars est dans la Rome antique une plaine si" +
                     "tuée entre la ville républicaine et la rive gauc" +
                     "he du Tibre.\n\n\n== Moyen Âge ==\nAu Moyen Âge," +
                     " le champ de mars, puis champ de mai, est un nom" +
                     " générique que l'on a donné aux grandes assemblé" +
                     "es de guerriers francs en Gaule aux époques méro" +
                     "vingienne et carolingienne. Le nom associe un li" +
                     "eu (un pré où tous les chevaux des différents gu" +
                     "erriers pouvaient se rassembler pour la première" +
                     " fois de l'année avant de partir pour une nouvel" +
                     "le campagne militaire) et la période de l'année " +
                     "la plus favorable à la pousse de l'herbe du cham" +
                     "p en question et qui peut être aussi bien choisi" +
                     "e en mars qu'en mai.\nPour le médiévaliste Mauli" +
                     "n, spécialiste de la chanson de geste en littéra" +
                     "ture médiévale :\n\n« Chaque année, dans les tem" +
                     "ps mérovingiens et sous les premiers Carolingien" +
                     "s, voyait les Francs préparer dans leur Champ de" +
                     " mars ou de mai la prochaine campagne, puis s'ab" +
                     "attre un mois plus tard sur une nouvelle proie »" +
                     "Maulin (en 1863) voyait là une des origines des " +
                     "cantilènes, qui ont ensuite - selon lui - évolué" +
                     " en chansons de geste ;\n\n« Chaque année voyait" +
                     " aussi les cantilénisles célébrer, le départ, le" +
                     " retour, l'heureux ou le mauvais succès de la gr" +
                     "ande chevauchée Être signalé honorablement dans " +
                     "un de ces récits populaires, c'était alors ce qu" +
                     "'aujourd'hui nous appelons être mis à l'ordre du " +
                     "jour de l'armée. La chanson était le bulletin des" +
                     " combats, bulletin vivement attendu, avidement " +
                     "écouté par ceux dont le nom pouvait s'y trouver" +
                     " prononcé et par la nation entière dont il fla" +
                     "ttait l'orgueil et le patriotisme », mais, est" +
                     "ime Maulin, « à côté de ces pièces, pour ainsi " +
                     "dire officielles, il y avait des chansons qui ré" +
                     "pondaient à des sentiments non moins enracinés, " +
                     "et portaient sur de pieuses traditions ravivées " +
                     "par la conquête, ou sur la translation de certai" +
                     "nes reliques, ou sur le bruit de certains miracl" +
                     "es (...) ».\n\n\n== Sens contemporain ==\n\nDepu" +
                     "is la Renaissance, et dans cette même acception " +
                     "guerrière, ce nom était donné aux places sur les" +
                     "quelles se déroulaient les exercices militaires." +
                     " Les villes de garnison avaient leur champ de Ma" +
                     "rs (dénommé aussi parfois « champ de bataille »)" +
                     " et l'expression sert à désigner de nombreuses p" +
                     "laces ou espaces verts modernes qui ont perdu cet" +
                     "te fonction première.\nEn Belgique, le terme de «" +
                     " plaine des manœuvres » (ou « plaine de manœuvres" +
                     " ») est en général préféré."}]}},
     ("Champ de Mars",
      "<p>Champ de Mars ou Champ-de-Mars est un nom de l" +
      "ieu, généralement urbain, faisant à la fois réfé" +
      "rence au dieu Mars et au mois de mars (qui lui é" +
      "tait autrefois dédié). La fonction du « champ de" +
      " Mars » a évolué au cours du temps.</p><p></p><p" +
      "></p><p>== Antiquité ==</p><p>Le Champ de Mars e" +
      "st dans la Rome antique une plaine située entre " +
      "la ville républicaine et la rive gauche du Tibre" +
      ".</p><p></p><p></p><p>== Moyen Âge ==</p><p>Au M" +
      "oyen Âge, le champ de mars, puis champ de mai, e" +
      "st un nom générique que l'on a donné aux grandes" +
      " assemblées de guerriers francs en Gaule aux épo" +
      "ques mérovingienne et carolingienne. Le nom asso" +
      "cie un lieu (un pré où tous les chevaux des diff" +
      "érents guerriers pouvaient se rassembler pour la" +
      " première fois de l'année avant de partir pour u" +
      "ne nouvelle campagne militaire) et la période de" +
      " l'année la plus favorable à la pousse de l'herb" +
      "e du champ en question et qui peut être aussi bi" +
      "en choisie en mars qu'en mai.</p><p>Pour le médi" +
      "évaliste Maulin, spécialiste de la chanson de ge" +
      "ste en littérature médiévale :</p><p></p><p>« Ch" +
      "aque année, dans les temps mérovingiens et sous " +
      "les premiers Carolingiens, voyait les Francs pré" +
      "parer dans leur Champ de mars ou de mai la proch" +
      "aine campagne, puis s'abattre un mois plus tard " +
      "sur une nouvelle proie »Maulin (en 1863) voyait " +
      "là une des origines des cantilènes, qui ont ensu" +
      "ite - selon lui - évolué en chansons de geste ;<" +
      "/p><p></p><p>« Chaque année voyait aussi les can" +
      "tilénisles célébrer, le départ, le retour, l'heu" +
      "reux ou le mauvais succès de la grande chevauché" +
      "e Être signalé honorablement dans un de ces réci" +
      "ts populaires, c'était alors ce qu'aujourd'hui n" +
      "ous appelons être mis à l'ordre du jour de l'arm" +
      "ée. La chanson était le bulletin des combats, bu" +
      "lletin vivement attendu, avidement écouté par ce" +
      "ux dont le nom pouvait s'y trouver prononcé et p" +
      "ar la nation entière dont il flattait l'orgueil " +
      "et le patriotisme », mais, estime Maulin, « à cô" +
      "té de ces pièces, pour ainsi dire officielles, i" +
      "l y avait des chansons qui répondaient à des sen" +
      "timents non moins enracinés, et portaient sur de" +
      " pieuses traditions ravivées par la conquête, ou" +
      " sur la translation de certaines reliques, ou su" +
      "r le bruit de certains miracles (...) ».</p><p><" +
      "/p><p></p><p>== Sens contemporain ==</p><p></p><" +
      "p>Depuis la Renaissance, et dans cette même acce" +
      "ption guerrière, ce nom était donné aux places s" +
      "ur lesquelles se déroulaient les exercices milit" +
      "aires. Les villes de garnison avaient leur champ" +
      " de Mars (dénommé aussi parfois « champ de batai" +
      "lle ») et l'expression sert à désigner de nombre" +
      "uses places ou espaces verts modernes qui ont pe" +
      "rdu cette fonction première.</p><p>En Belgique, " +
      "le terme de « plaine des manœuvres » (ou « plain" +
      "e de manœuvres ») est en général préféré.</p>",
      "https://fr.wikipedia.org/wiki/Champ_de_Mars"))
]
