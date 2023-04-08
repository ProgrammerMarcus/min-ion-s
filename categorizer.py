import spacy

nlp = spacy.load("en_core_web_sm")

def categorize(opinions: list):
    """
    Categorizes a list of strings into a list of dictionaries containing the string and categories.
    Works better on longer strings, so accuracy of categorization of extracted opinions is low.
    :param opinions:
    :return:
    """
    categories = list()
    for o in opinions:
        print(o)
        doc = nlp(o)
        categories += [{"text": o, "ents": [x.label_ for x in doc.ents]}]
    return categories
