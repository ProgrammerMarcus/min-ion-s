import spacy

nlp = spacy.load("en_core_web_sm")


def categorize(opinions: list):
    categories = list()
    for o in opinions:
        doc = nlp(o)
        categories += [{"text": o, "ents": [x.label_ for x in doc.ents]}]
    return categories
