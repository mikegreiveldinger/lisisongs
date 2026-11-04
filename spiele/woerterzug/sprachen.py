"""Erzeugt woerter-en.json (UK English) und woerter-fr.json (Français) für den Wörterzug.

Jede Sprache hat eigene Wörter zu den gemalten Bildern, mit passenden Silben und Schreibschwerpunkten.
Farben, Landschaften und Satzbilder kommen aus woerter.json (Deutsch). Aufruf: python3 sprachen.py
"""
import json, os, pathlib

hier = pathlib.Path(__file__).parent
NB = " "
de = json.loads((hier / "woerter.json").read_text(encoding="utf-8"))
L = {l["nr"]: l for l in de["level"]}


def S(wort, silben, id):
    assert "".join(silben) == wort, (wort, silben)
    return {"id": id, "wort": wort, "silben": silben}


def W(wort, fokus, id):
    assert not fokus or fokus in wort.lower(), (wort, fokus)
    return {"id": id, "wort": wort, "fokus": fokus}


def saetze(nr, texte):
    alt = L[nr]["eintraege"]
    assert len(alt) == len(texte), (nr, len(alt), len(texte))
    return [{"satz": t, "bild": a["bild"]} for t, a in zip(texte, alt)]


def lv(nr, station, intro, eintraege, frage=False):
    d = {k: v for k, v in L[nr].items() if k not in ("station", "intro", "eintraege", "emoji")}
    d.update(station=station, intro=intro, eintraege=eintraege)
    return d


en = {"level": [
    lv(1, "Farm", "Welcome to the farm! Put the syllables together.", [
        S("donkey", ["don", "key"], "zug-esel"), S("piglet", ["pig", "let"], "zug-ferkel"), S("turkey", ["tur", "key"], "zug-truthahn"),
        S("rabbit", ["rab", "bit"], "zug-kaninchen"), S("pony", ["po", "ny"], "zug-pony"), S("hedgehog", ["hedge", "hog"], "zug-igel"),
        S("wheelbarrow", ["wheel", "bar", "row"], "zug-schubkarre"), S("farmer", ["far", "mer"], "zug-bauer")]),
    lv(2, "Market", "Fruit and vegetables at the market. Which syllables fit?", [
        S("cherry", ["cher", "ry"], "zug-kirsche"), S("melon", ["mel", "on"], "zug-melone"), S("lemon", ["lem", "on"], "zug-zitrone"),
        S("pineapple", ["pine", "ap", "ple"], "zug-ananas"), S("cucumber", ["cu", "cum", "ber"], "zug-gurke"), S("pepper", ["pep", "per"], "zug-paprika"),
        S("onion", ["on", "ion"], "zug-zwiebel"), S("potato", ["po", "ta", "to"], "zug-kartoffel"), S("radish", ["rad", "ish"], "zug-radieschen"),
        S("honey", ["hon", "ey"], "zug-honig")]),
    lv(3, "Wardrobe", "Lisi is packing her suitcase. Which clothes does she take?", [
        S("jumper", ["jum", "per"], "zug-pullover"), S("pyjamas", ["py", "ja", "mas"], "zug-schlafanzug"), S("wellies", ["wel", "lies"], "zug-gummistiefel"),
        S("handbag", ["hand", "bag"], "zug-handtasche"), S("sandals", ["san", "dals"], "zug-sandalen"), S("trainers", ["train", "ers"], "zug-turnschuhe"),
        S("neckerchief", ["neck", "er", "chief"], "zug-halstuch"), S("necktie", ["neck", "tie"], "zug-krawatte")]),
    lv(4, "In the Woods", "It is quiet in the woods. Build the words letter by letter.", [
        W("wolf", "", "zug-wolf"), W("fox", "", "zug-fuchs"), W("badger", "", "zug-dachs"), W("deer", "ee", "zug-hirsch"), W("raven", "", "zug-rabe"),
        W("tent", "", "zug-zelt"), W("moss", "ss", "zug-moos"), W("fern", "", "zug-farn"), W("lantern", "", "zug-laterne"), W("nut", "", "zug-nuss"),
        W("berry", "rr", "zug-beere")]),
    lv(5, "At the Station", "The train stops at the station. Look out for double letters!", [
        W("carriage", "rr", "zug-waggon"), W("tunnel", "nn", "zug-tunnel"), W("balloon", "ll", "zug-ballon"), W("doll", "ll", "zug-puppe"),
        W("teddy", "dd", "zug-teddy"), W("hammer", "mm", "zug-hammer"), W("suitcase", "", "zug-koffer"), W("whistle", "", "zug-pfiff"),
        W("kettle", "tt", "zug-kanne")]),
    lv(6, "In the Meadow", "A long ee sound is often spelled ee or ea.", [
        W("knee", "ee", "zug-knie"), W("bee", "ee", "natur-biene"), W("sheep", "ee", "tiere-schaf"), W("tree", "ee", "pflanzen-baum"),
        W("meadow", "ea", "zug-wiese"), W("leaf", "ea", "pflanzen-blatt"), W("wheat", "ea", "pflanzen-aehre"), W("cheese", "ee", "essen-kaese")]),
    lv(7, "In Town", "In town we practise ck and sh.", [
        W("clock", "ck", "zug-wecker"), W("duck", "ck", "tiere-ente"), W("chick", "ck", "zug-kueken"), W("jacket", "ck", "kleidung-jacke"),
        W("shoe", "sh", "kleidung-schuh"), W("fish", "sh", "tiere-fisch"), W("shell", "sh", "natur-muschel"), W("puddle", "dd", "zug-pfuetze")]),
    lv(8, "By the Sea", "Listen for ai, oa, ow and igh!", [
        W("snail", "ai", "natur-schnecke"), W("rain", "ai", "wetter-regen"), W("rainbow", "ai", "wetter-regenbogen"), W("goat", "oa", "zug-ziege"),
        W("coat", "oa", "zug-mantel"), W("snow", "ow", "wetter-schnee"), W("lighthouse", "igh", "zug-leuchtturm"), W("rope", "", "zug-seil")]),
    lv(9, "At Home", "Short sentences from home. A capital letter at the start and a full stop at the end!", saetze(9, [
        "Lisi reads a book.", "Nora paints a picture.", "Malik plays football.", "Tian cooks pasta.", "The cat is sleeping.", "Dad bakes bread.",
        "Mum waters the flowers.", "The dog barks loudly.", "We eat together.", "Gran knits a scarf.", "I brush my teeth.", "The baby laughs."])),
    lv(10, "Autumn Woods", "The leaves are falling. Put the autumn sentences in order.", saetze(10, [
        "The fox runs through the woods.", "Lisi travels by train.", "The leaves fall from the tree.", "Nora collects shiny conkers.",
        "The hedgehog sleeps in the leaves.", "In autumn the wind often blows.", "Malik flies a kite.", "Tian drinks a warm cup of tea.",
        "The sun is shining in the sky.", "The squirrel looks for nuts.", "The rain drips on the roof.", "The children jump in the puddle.",
        "The train goes over the bridge.", "We are baking a pumpkin cake.", "The hare hops across the field."])),
    lv(11, "On a Journey", "Long sentences for a long journey. Read carefully!", saetze(11, [
        "Lisi packs her suitcase for the trip.", "The train goes through a long tunnel.", "Malik waits at the station with his gran.",
        "Nora looks out of the window.", "Tian has the tickets in his pocket.", "The guard blows his whistle very loudly.",
        "We are going to the seaside by train.", "We build a sandcastle on the beach.", "The plane flies high above the clouds.",
        "It is warm and cosy in the tent.", "In the evening Grandad tells a story.", "Tomorrow we are going home again."])),
    lv(12, "Last Stop", "Last stop! Here are questions. A question ends with a question mark.", saetze(12, [
        "Where is the train going?", "When will we get there?", "Who has got my suitcase?", "Where is the ticket?", "Are you coming to the seaside?",
        "Are you hungry?", "What can you see out of the window?", "What is the station called?", "Can I sit by the window?",
        "Why is the train stopping here?", "Will you play with me?", "Do you like hot chocolate?"]), True)],
    "ueberraschungen": [
        {"von": "Nora", "bild": "pflanzen-kastanie", "text": "Nora has brought you a shiny conker!"},
        {"von": "Malik", "bild": "🪁", "text": "Malik gives you a colourful kite!"},
        {"von": "Tian", "bild": "🏮", "text": "Tian has a glowing lantern for you!"},
        {"von": "Nora", "bild": "pflanzen-blatt", "text": "Nora found the prettiest autumn leaf for you!"},
        {"von": "Malik", "bild": "essen-kuerbis", "text": "Malik brings you a big pumpkin!"},
        {"von": "Tian", "bild": "🦔", "text": "Tian found a little hedgehog. It says hello!"},
        {"von": "Nora", "bild": "natur-feder", "text": "Nora gives you a soft feather!"},
        {"von": "Malik", "bild": "tiere-eichhoernchen", "text": "A squirrel comes to visit you with Malik!"},
        {"von": "Tian", "bild": "pflanzen-sonnenblume", "text": "Tian brings you a big sunflower!"}]}

fr = {"level": [
    lv(1, "La ferme", f"Bienvenue à la ferme{NB}! Assemble les syllabes.", [
        S("chèvre", ["chè", "vre"], "zug-ziege"), S("porcelet", ["por", "ce", "let"], "zug-ferkel"), S("poussin", ["pous", "sin"], "zug-kueken"),
        S("dindon", ["din", "don"], "zug-truthahn"), S("lapin", ["la", "pin"], "zug-kaninchen"), S("poney", ["po", "ney"], "zug-pony"),
        S("poulain", ["pou", "lain"], "zug-fohlen"), S("hérisson", ["hé", "ris", "son"], "zug-igel"), S("arrosoir", ["ar", "ro", "soir"], "zug-giesskanne"),
        S("brouette", ["brou", "ette"], "zug-schubkarre"), S("fermier", ["fer", "mier"], "zug-bauer")]),
    lv(2, "Le marché", f"Des fruits et des légumes au marché. Quelles syllabes vont ensemble{NB}?", [
        S("cerise", ["ce", "rise"], "zug-kirsche"), S("melon", ["me", "lon"], "zug-melone"), S("citron", ["ci", "tron"], "zug-zitrone"),
        S("ananas", ["a", "na", "nas"], "zug-ananas"), S("concombre", ["con", "com", "bre"], "zug-gurke"), S("poivron", ["poi", "vron"], "zug-paprika"),
        S("oignon", ["oi", "gnon"], "zug-zwiebel"), S("patate", ["pa", "tate"], "zug-kartoffel"), S("raisin", ["rai", "sin"], "zug-trauben"),
        S("radis", ["ra", "dis"], "zug-radieschen")]),
    lv(3, "L’armoire", f"Lisi fait sa valise. Quels vêtements emporte-t-elle{NB}?", [
        S("collant", ["col", "lant"], "zug-strumpfhose"), S("manteau", ["man", "teau"], "zug-mantel"), S("chemisier", ["che", "mi", "sier"], "zug-bluse"),
        S("pyjama", ["py", "ja", "ma"], "zug-schlafanzug"), S("ceinture", ["cein", "ture"], "zug-guertel"), S("cravate", ["cra", "vate"], "zug-krawatte"),
        S("sandales", ["san", "dales"], "zug-sandalen"), S("baskets", ["bas", "kets"], "zug-turnschuhe"), S("barrette", ["bar", "rette"], "zug-haarspange"),
        S("foulard", ["fou", "lard"], "zug-halstuch")]),
    lv(4, "Dans la forêt", "Dans la forêt, on entend ou et eau. Écris les mots lettre par lettre.", [
        W("loup", "ou", "zug-wolf"), W("renard", "", "zug-fuchs"), W("blaireau", "eau", "zug-dachs"), W("cerf", "", "zug-hirsch"),
        W("corbeau", "eau", "zug-rabe"), W("tente", "", "zug-zelt"), W("mousse", "ou", "zug-moos"), W("fougère", "ou", "zug-farn"),
        W("ruisseau", "eau", "zug-bach"), W("lanterne", "", "zug-laterne"), W("noisette", "tt", "zug-nuss"), W("myrtille", "ill", "zug-beere")]),
    lv(5, "À la gare", f"Le train s’arrête à la gare. Attention aux lettres doubles{NB}!", [
        W("valise", "", "zug-koffer"), W("wagon", "", "zug-waggon"), W("tunnel", "nn", "zug-tunnel"), W("ballon", "ll", "zug-ballon"),
        W("poupée", "ou", "zug-puppe"), W("nounours", "ou", "zug-teddy"), W("marteau", "eau", "zug-hammer"), W("sifflet", "ff", "zug-pfiff"),
        W("fauteuil", "au", "zug-sessel"), W("ciel", "", "zug-himmel")]),
    lv(6, "Dans le pré", "Dans le pré, on entend oi, eau et an.", [
        W("mouche", "ou", "zug-fliege"), W("miroir", "oi", "zug-spiegel"), W("lettre", "tt", "zug-brief"), W("taureau", "eau", "zug-stier"),
        W("drapeau", "eau", "zug-ziel"), W("chanson", "an", "zug-lied"), W("genou", "ou", "zug-knie"), W("géant", "an", "zug-riese"),
        W("pin", "in", "zug-kiefer")]),
    lv(7, "En ville", "En ville, on entend eil, qu et gu.", [
        W("boulanger", "an", "zug-baecker"), W("sucre", "", "zug-zucker"), W("réveil", "eil", "zug-wecker"), W("couverture", "ou", "zug-decke"),
        W("moineau", "eau", "zug-spatz"), W("bonnet", "nn", "zug-muetze"), W("trésor", "", "zug-schatz"), W("flaque", "qu", "zug-pfuetze"),
        W("matelas", "", "zug-matratze"), W("seringue", "gu", "zug-spritze")]),
    lv(8, "À la mer", f"Au bord de la mer, écoute bien les sons{NB}!", [
        W("seau", "eau", "zug-eimer"), W("corde", "", "zug-seil"), W("pelle", "ll", "zug-schaufel"), W("chenille", "ill", "zug-raupe"),
        W("phare", "ph", "zug-leuchtturm"), W("foin", "oin", "zug-heu"), W("craie", "ai", "zug-kreide"), W("ventre", "en", "zug-bauch"),
        W("échelle", "ll", "zug-leiter")]),
    lv(9, "À la maison", f"Des phrases courtes de la maison. Une majuscule au début et un point à la fin{NB}!", saetze(9, [
        "Lisi lit un livre.", "Nora peint un tableau.", "Malik joue au football.", "Tian fait cuire des pâtes.", "Le chat dort.", "Papa fait du pain.",
        "Maman arrose les fleurs.", "Le chien aboie fort.", "Nous mangeons ensemble.", "Mamie tricote une écharpe.", "Je me brosse les dents.", "Le bébé rit."])),
    lv(10, "La forêt d’automne", "Les feuilles tombent. Range les phrases d’automne.", saetze(10, [
        "Le renard court dans la forêt.", "Lisi voyage en train.", "Les feuilles tombent de l’arbre.", "Nora ramasse des marrons brillants.",
        "Le hérisson dort dans les feuilles.", "En automne, le vent souffle souvent.", "Malik fait voler un cerf-volant.", "Tian boit un thé chaud.",
        "Le soleil brille dans le ciel.", "L’écureuil cherche des noisettes.", "La pluie tombe sur le toit.", "Les enfants sautent dans la flaque.",
        "Le train passe sur le pont.", "Nous faisons un gâteau à la citrouille.", "Le lièvre saute dans le champ."])),
    lv(11, "En voyage", f"Des phrases longues pour un long voyage. Lis bien{NB}!", saetze(11, [
        "Lisi prépare sa valise pour le voyage.", "Le train passe dans un long tunnel.", "Malik attend à la gare avec sa mamie.",
        "Nora regarde par la fenêtre.", "Tian a les billets dans sa poche.", "Le contrôleur siffle très fort.", "Nous allons à la mer en train.",
        "Sur la plage, nous faisons un château de sable.", "L’avion vole au-dessus des nuages.", "Dans la tente, il fait chaud et doux.",
        "Le soir, papi raconte une histoire.", "Demain, nous rentrons à la maison."])),
    lv(12, "Le terminus", f"Terminus{NB}! Ici, il y a des questions. À la fin, on met un point d’interrogation.", saetze(12, [
        "Où va le train ?", "Quand arrivons-nous ?", "Qui a ma valise ?", "Où est le billet ?", "Tu viens à la mer ?", "As-tu faim ?",
        "Que vois-tu par la fenêtre ?", "Comment s’appelle la gare ?", "Je peux m’asseoir à la fenêtre ?", "Pourquoi le train s’arrête ici ?",
        "Tu joues avec moi ?", "Tu aimes le chocolat chaud ?"]), True)],
    "ueberraschungen": [
        {"von": "Nora", "bild": "pflanzen-kastanie", "text": f"Nora t’a apporté un marron tout brillant{NB}!"},
        {"von": "Malik", "bild": "🪁", "text": f"Malik t’offre un cerf-volant coloré{NB}!"},
        {"von": "Tian", "bild": "🏮", "text": f"Tian a une lanterne lumineuse pour toi{NB}!"},
        {"von": "Nora", "bild": "pflanzen-blatt", "text": f"Nora a trouvé la plus belle feuille d’automne pour toi{NB}!"},
        {"von": "Malik", "bild": "essen-kuerbis", "text": f"Malik t’apporte une grosse citrouille{NB}!"},
        {"von": "Tian", "bild": "🦔", "text": f"Tian a trouvé un petit hérisson. Il te dit bonjour{NB}!"},
        {"von": "Nora", "bild": "natur-feder", "text": f"Nora t’offre une plume toute douce{NB}!"},
        {"von": "Malik", "bild": "tiere-eichhoernchen", "text": f"Un écureuil vient te voir avec Malik{NB}!"},
        {"von": "Tian", "bild": "pflanzen-sonnenblume", "text": f"Tian t’apporte un grand tournesol{NB}!"}]}

ids = {p.stem for p in (hier / "bilder-gemalt").glob("*.webp")} | {p.stem for p in (hier.parent / "lisis-woerterwelt" / "bilder-gemalt").glob("*.webp")}
for name, d in (("en", en), ("fr", fr)):
    fehlt = [e["id"] for l in d["level"] for e in l["eintraege"] if "id" in e and e["id"] not in ids]
    print(name, "Einträge:", {l["nr"]: len(l["eintraege"]) for l in d["level"]}, "| fehlende Bilder:", fehlt)
    d = {"hinweis": f"Wortliste ({name}) für den Wörterzug, erzeugt von sprachen.py. id = gemaltes Bild.", **d}
    (hier / f"woerter-{name}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
