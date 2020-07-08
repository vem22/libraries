import config as init
import re

def clean_text(testo, lang):
    testo = testo.lower()

    # si rimuovono gli indirizzi email
    testo = re.sub(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", "", testo)

    # si rimuovono le parole con meno di 3 lettere
    testo = re.sub(r'\b[a-zA-Z]{1,2}\b', '', testo)

    # si sostituiscono \r e \n con spazio
    testo = re.sub(r'\r\n', ' ', testo)

    # si sostituisce la fine e l'inizio della frase con uno spazio
    testo = re.sub(r'$', ' ', testo)
    testo = re.sub(r'^', ' ', testo)

    # si rimuove la punteggiatura tranne che per punteggiatura seguita da
    # un altro carattere o numero
    # si salva ad esempio: "azienda 4.0"
    testo = re.sub(r'[^\w\s](?!\d)(?!\w)', ' ', testo)

    # si rimuovono i numeri che sono preceduti e seguiti da
    # uno spazio
    testo = re.sub(r'(?<=\s)[\d]+(?=\s)', ' ', testo)

    # si rimuovono gli spazi maggiori di 2
    testo = re.sub(r' {2,100} ', ' ', testo).strip()

    if lang == 'it':
        testo = it_stopwords_lemma(testo)
    elif lang == 'en':
        testo = en_stopwords_lemma(testo)

    testo = re.sub(r'[^\w\s](?!\d)(?!\w)', ' ', testo)
    testo = re.sub(r' {2,100} ', ' ', testo).strip()

    return testo

def it_stopwords_lemma(testo):
    testo = ' '.join([w for w in testo.split() if not w in init.ITA_STOPWORDS])
    testo = init.NLP_ITA(testo)
    testo = ' '.join([w.lemma_.strip() for w in testo])

    return testo

def en_stopwords_lemma(testo):
    testo = ' '.join([w for w in testo.split() if not w in init.EN_STOPWORDS])
    testo = init.NLP_EN(testo)
    testo = ' '.join([w.lemma_.strip() for w in testo])

    return testo
