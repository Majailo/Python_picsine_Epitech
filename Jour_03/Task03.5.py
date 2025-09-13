# task 3.5

LANGUAGE_PROFILES = {
    "english": {
        "e": 12.7,
        "t": 9.1,
        "a": 8.2,
        "o": 7.5,
        "i": 7.0,
        "n": 6.7,
        "s": 6.3,
        "h": 6.1,
        "r": 6.0,
        "d": 4.3,
        "l": 4.0,
        "c": 2.8,
        "u": 2.8,
        "m": 2.4,
        "w": 2.4,
        "f": 2.2,
        "g": 2.0,
        "y": 2.0,
        "p": 1.9,
        "b": 1.5,
        "v": 1.0,
        "k": 0.8,
        "j": 0.2,
        "x": 0.2,
        "q": 0.1,
        "z": 0.1,
    },
    "french": {
        "e": 14.7,
        "a": 7.6,
        "i": 7.5,
        "s": 7.9,
        "n": 7.2,
        "r": 6.6,
        "t": 7.0,
        "o": 5.8,
        "l": 5.5,
        "u": 6.3,
        "d": 3.7,
        "c": 3.3,
        "m": 2.7,
        "p": 3.0,
        "v": 1.8,
        "q": 1.4,
        "f": 1.1,
        "b": 0.9,
        "g": 1.0,
        "h": 1.1,
        "j": 0.3,
        "x": 0.4,
        "y": 0.3,
        "z": 0.1,
        "é": 1.5,
        "è": 0.8,
        "ê": 0.6,
        "ë": 0.1,
        "à": 0.5,
        "ù": 0.1,
        "ç": 0.3,
    },
    "spanish": {
        "e": 13.7,
        "a": 12.5,
        "o": 8.7,
        "s": 7.9,
        "n": 7.0,
        "r": 6.9,
        "l": 5.2,
        "d": 5.0,
        "c": 4.7,
        "t": 4.6,
        "u": 3.9,
        "m": 3.2,
        "p": 2.5,
        "b": 1.4,
        "g": 1.0,
        "v": 0.9,
        "y": 1.0,
        "q": 1.0,
        "h": 0.7,
        "f": 0.5,
        "z": 0.4,
        "j": 0.5,
        "ñ": 0.3,
        "á": 0.4,
        "é": 0.4,
        "í": 0.4,
        "ó": 0.4,
        "ú": 0.4,
    },
    "portuguese": {
        "a": 14.6,
        "e": 12.6,
        "o": 10.7,
        "s": 7.8,
        "r": 6.7,
        "i": 6.2,
        "n": 5.0,
        "d": 4.9,
        "m": 4.7,
        "u": 4.6,
        "t": 4.3,
        "c": 3.9,
        "l": 2.8,
        "p": 2.5,
        "v": 1.6,
        "g": 1.3,
        "h": 1.2,
        "q": 1.2,
        "b": 1.0,
        "f": 1.0,
        "z": 0.5,
        "j": 0.4,
        "x": 0.2,
        "á": 0.5,
        "â": 0.3,
        "ã": 0.5,
        "é": 0.4,
        "ê": 0.2,
        "í": 0.2,
        "ó": 0.4,
        "ô": 0.2,
        "õ": 0.3,
        "ú": 0.2,
        "ç": 0.3,
    },
    "italian": {
        "e": 11.8,
        "a": 11.7,
        "i": 10.7,
        "o": 9.8,
        "n": 6.9,
        "l": 6.5,
        "r": 6.4,
        "t": 5.6,
        "s": 4.9,
        "c": 4.5,
        "d": 3.7,
        "u": 3.2,
        "m": 2.9,
        "p": 3.0,
        "v": 2.1,
        "g": 1.6,
        "h": 0.6,
        "b": 1.0,
        "f": 1.1,
        "z": 1.0,
        "à": 0.2,
        "è": 0.2,
        "é": 0.2,
        "ì": 0.2,
        "ò": 0.2,
        "ù": 0.2,
    },
    "german": {
        "e": 17.4,
        "n": 9.8,
        "i": 7.6,
        "s": 7.3,
        "r": 7.0,
        "a": 6.5,
        "t": 6.2,
        "d": 5.1,
        "h": 4.8,
        "u": 4.3,
        "l": 3.4,
        "c": 3.1,
        "g": 3.0,
        "m": 2.5,
        "o": 2.5,
        "b": 1.9,
        "w": 1.9,
        "f": 1.7,
        "k": 1.2,
        "z": 1.1,
        "ä": 0.6,
        "ö": 0.4,
        "ü": 0.7,
        "ß": 0.3,
        "j": 0.3,
        "v": 0.8,
    },
    "dutch": {
        "e": 18.9,
        "n": 10.0,
        "a": 7.5,
        "t": 6.8,
        "i": 6.5,
        "r": 6.4,
        "o": 6.1,
        "d": 5.6,
        "s": 3.7,
        "l": 3.6,
        "g": 3.4,
        "v": 2.8,
        "h": 2.4,
        "k": 2.3,
        "m": 2.2,
        "u": 1.9,
        "b": 1.6,
        "p": 1.6,
        "w": 1.5,
        "j": 1.5,
        "z": 1.4,
        "f": 0.8,
        "c": 0.6,
        "x": 0.1,
        "y": 0.1,
        "é": 0.2,
        "è": 0.1,
        "ë": 0.1,
    },
    "swedish": {
        "e": 10.2,
        "a": 9.4,
        "n": 8.6,
        "t": 7.7,
        "r": 8.4,
        "s": 6.6,
        "l": 5.3,
        "d": 4.7,
        "o": 4.5,
        "i": 4.8,
        "m": 3.5,
        "g": 2.9,
        "k": 3.1,
        "v": 2.4,
        "h": 2.1,
        "u": 1.9,
        "f": 2.0,
        "b": 1.3,
        "p": 1.8,
        "å": 1.3,
        "ä": 1.8,
        "ö": 1.3,
        "y": 0.6,
        "j": 0.6,
    },
    "polish": {
        "a": 8.9,
        "i": 8.2,
        "e": 7.7,
        "o": 7.6,
        "z": 6.2,
        "n": 5.5,
        "r": 4.7,
        "w": 4.7,
        "y": 4.0,
        "c": 3.9,
        "l": 3.7,
        "t": 3.3,
        "s": 3.2,
        "d": 2.5,
        "k": 2.5,
        "p": 2.4,
        "m": 2.4,
        "u": 2.4,
        "j": 2.3,
        "b": 1.5,
        "g": 1.5,
        "ę": 1.1,
        "ł": 2.1,
        "ś": 0.8,
        "ń": 0.8,
        "ć": 0.8,
        "ó": 0.7,
        "ź": 0.3,
        "ż": 0.4,
    },
    "turkish": {
        "a": 12.9,
        "e": 8.6,
        "i": 8.3,
        "n": 7.9,
        "r": 6.7,
        "l": 6.0,
        "d": 5.2,
        "k": 4.7,
        "t": 3.6,
        "u": 3.2,
        "m": 3.0,
        "o": 2.9,
        "b": 2.8,
        "s": 2.7,
        "y": 2.7,
        "v": 2.4,
        "z": 1.5,
        "g": 1.3,
        "ç": 1.2,
        "ş": 1.2,
        "ğ": 1.1,
        "ı": 5.1,
        "ö": 0.8,
        "ü": 0.9,
        "c": 0.7,
        "h": 0.6,
        "f": 0.5,
        "j": 0.4,
        "p": 0.3,
    },
    "esperanto": {
        "a": 12.0,
        "e": 8.9,
        "i": 10.0,
        "o": 9.8,
        "u": 9.4,
        "n": 8.5,
        "l": 6.1,
        "s": 5.7,
        "r": 5.6,
        "t": 4.8,
        "k": 4.5,
        "m": 3.7,
        "d": 3.5,
        "p": 3.1,
        "v": 2.1,
        "g": 2.0,
        "b": 1.8,
        "f": 1.4,
        "h": 1.2,
        "ĉ": 1.0,
        "ĝ": 0.8,
        "ĵ": 0.5,
        "ŝ": 0.6,
        "ŭ": 0.3,
        "ĥ": 0.2,
        "z": 0.3,
        "c": 0.3,
        "j": 0.6,
    },
}


txt = "Footage taken from a helicopter shows large swathes of snow falling down the side of a mountain during a controlled avalanche conducted by authorities in Milford Sound in New Zealand.Specialist teams from New Zealand's Transport Agency used explosives to trigger an avalanche to clear the risk for visitors driving on the road to the popular tourist destination in the South Island."
txt_portuguese = "Já vim muitas vezes aqui, mas antes nunca me aconteceu nada! Vou te contar uma história. Imagina por um segundo que você tem muito medo de falar com outras pessoas. Imaginou? Então, eu sou assim. Desde que eu era muito pequeno eu morria de medo de falar com os outros. Eu falava com meus pais e minha irmã mais nova. Depois, na escola, entre muitos alunos eu consegui encontrar, com muita dificuldade, um amigo. Quando eu percebi que tinha um problema muito sério, comecei a pensar em estratégias para vencer meu medo. Uma delas foi usar a tecnologia a meu favor e tentar conversar muito pela Internet com as poucas pessoas que eu conseguia falar. Uma outra ideia foi ir muitas vezes aos mesmos lugares para me acostumar ao ambiente e às pessoas. Às vezes até pedia aos meus pais para ir aos meus lugares preferidos para colocar minha ideia em prática. Reconheço que foi uma ideia muito boa até hoje à tarde."
txt_alle = "Die jährliche Studie enthält eine umfassende Datensammlung zu den Bildungssystemen der Mitgliedsstaaten und weiterer Partnerländer. Dargestellt wird etwa, wie viel Geld jeweils für Bildung ausgeben wird, wie der Betreuungsschlüssel in Bildungseinrichtungen aussieht, wie groß Schulklassen und wie hoch die Kosten für ein Studium sind."


def conca():  # recupere tous les types de lettre possible dans les differentes langue proposé par le dictonnaire
    key_prim = [elm for elm in LANGUAGE_PROFILES]
    key_sec = []
    # key_sec = [elm for elm in LANGUAGE_PROFILES[key_prim]]
    for elm in key_prim:
        for i in LANGUAGE_PROFILES[elm]:
            key_sec.append(i)
            # print(i)

    key_sec = set(key_sec)
    key_sec = list(key_sec)
    return key_sec


# faire un disctionnaire inversé avec comme clef le score et la lettre
def find_recu(txt):
    l = conca()
    # dico = {txt.count(letter)/(len(txt))*100:letter for letter in l}
    # dico2 = {letter : format(txt.count(letter)/len(txt)*100, ".1F") for letter in l}
    dico2 = {letter: txt.count(letter) / len(txt) * 100 for letter in l}

    # print (dico2)
    return dico2


def find_lang(t):
    final = []
    key_prim = [elm for elm in LANGUAGE_PROFILES]
    dico = find_recu(
        t
    )  # retour de l'analyse du text avec les frequence en % par caractere
    for lang in key_prim:
        score = 0
        for lettre in LANGUAGE_PROFILES[lang]:
            i = LANGUAGE_PROFILES[lang][lettre]
            score += abs(
                i - dico[lettre]
            )  # on calcul de delta entre les difference de lettre pour obtenir un score global d'écart

        final.append([lang, score])
    print(final)
    match = ""
    old = final[0][1]  # valeur initialisé à la 1er itéraation du dico fourni
    for elm in final:

        if elm[1] <= old:
            match = [elm][0][0]
            old = elm[1]

    print(match)

    # calcul de delta sur chaque caracter par raport à chaque langue


# find_lang(txt_portuguese)


find_lang(txt_alle)
