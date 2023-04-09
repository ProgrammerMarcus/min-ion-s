import spacy
from spacy.tokens.doc import Doc
import compare
import extract
from spacytextblob.spacytextblob import SpacyTextBlob  # DO NOT REMOVE, IGNORE THE LIES OF THE IDE!

def check_sentiment(v1: Doc, v2: Doc):
    v1 = v1._.blob.polarity
    v2 = v2._.blob.polarity
    if v1 > 0 and v2 > 0:
        return True
    elif v1 < 0 and v2 < 0:
        return True
    elif v1 == 0 and v2 == 0:
        return True
    return False


def check_category(v1: Doc, v2: Doc):
    labels1 = set([x.label_ for x in v1.ents])
    labels2 = set([x.label_ for x in v2.ents])
    if len(labels1) == 0 and len(labels2) == 0:
        return True
    elif labels1.issuperset(labels2) or labels1.issubset(labels2):
        return True
    return False


def preparation(reviews: list):
    """
    Extracts opinions, and then adds necessary data to opinions.
    :param reviews: The reviews to process.
    :return: The processed opinions.
    """
    opinions = extract.extract(" ".join(reviews))
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("spacytextblob")
    docs = [nlp(opinion) for opinion in opinions]
    return docs


def group_dsc(reviews: list):
    docs = preparation(reviews)
    grouped = list()
    for doc in docs:
        # a value of 0.0 means that any similarity means that it similar
        filtered = list(filter(lambda entry: compare.compare(doc, entry) > 0.0
                             and check_sentiment(doc, entry)
                             and check_category(doc, entry), docs))

        grouped += [filtered]
        for r in filtered:
            docs.remove(r)
    return grouped

def group_d(reviews: list):
    docs = preparation(reviews)
    grouped = list()
    for doc in docs:
        # a value of 0.0 means that any similarity means that it similar
        filtered = list(filter(lambda entry: compare.compare(doc, entry) > 0.0, docs))
        grouped += [filtered]
        for r in filtered:
            docs.remove(r)
    return grouped

def group_fsc(reviews: list):
    docs = preparation(reviews)
    grouped = list()
    for doc in docs:
        # around 0.6 seems to work
        filtered = list(filter(lambda entry: compare.fuzzy(doc, entry) > 0.6
                             and check_sentiment(doc, entry)
                             and check_category(doc, entry), docs))

        grouped += [filtered]
        for r in filtered:
            docs.remove(r)
    return grouped

def group_f(reviews: list):
    docs = preparation(reviews)
    grouped = list()
    for doc in docs:
        # around 0.6 seems to work
        filtered = list(filter(lambda entry: compare.fuzzy(doc, entry) > 0.6, docs))
        grouped += [filtered]
        for r in filtered:
            docs.remove(r)
    return grouped


def experiment(reviews: list):
    grouped = group_d(reviews)
    minorities = list()
    majorities = list()
    for g in grouped:
        if len(g) / sum(
                [len(n) for n in grouped]) <= 0.03:  # at a sample size of 30, 3% seems to select minority opinions
            minorities += [g]
        else:
            majorities += [g]

    print("DIFFERENCE (NOVEL) ONLY", "\n###MINORITY###\n", minorities, "\n###MAJORITY###\n", majorities)