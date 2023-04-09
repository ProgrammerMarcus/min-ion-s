from fuzzywuzzy import fuzz
from spacy.tokens.doc import Doc

whitelist = {"ADJ": "adjective",
             "ADV": "adverb",
             "NOUN": "noun",
             "NUM": "numeral",
             "PRON": "pronoun",
             "PROPN": "proper noun",
             "SYM": "symbol",
             "VERB": "verb",
             "CD": "cardinal number",
             "FW": "foreign word",
             "JJ": "adjective (English), other noun-modifier (Chinese)",
             "JJR": "adjective, comparative",
             "JJS": "adjective, superlative",
             "NN": "noun, singular or mass",
             "NNP": "noun, proper singular",
             "NNPS": "noun, proper plural",
             "NNS": "noun, plural",
             "PRP": "pronoun, personal",
             "PRP$": "pronoun, possessive",
             "RB": "adverb",
             "RBR": "adverb, comparative",
             "RBS": "adverb, superlative",
             "RP": "adverb, particle",
             "VB": "verb, base form",
             "VBD": "verb, past tense",
             "VBG": "verb, gerund or present participle",
             "VBN": "verb, past participle",
             "VBP": "verb, non-3rd person singular present",
             "VBZ": "verb, 3rd person singular present",
             "WP": "wh-pronoun, personal",
             "WP$": "wh-pronoun, possessive",
             "WRB": "wh-adverb",
             "ADD": "email",
             "GW": "additional word in multi-word expression",
             }


def compare(a: Doc, b: Doc):
    """
    Compares a to b by comparing distance of lemma words.
    Compares distance of words, so that similar words are considered different.
    POS tagging is used to exclude certain common words such as "the".
    :return:
    :param a: An (opinion) as a Doc.
    :param b: An (opinion) as a Doc.
    """

    lemma_a = [token.lemma_ for token in filter(lambda t: t.tag_ in whitelist, [token for token in a])]
    lemma_b = [token.lemma_ for token in filter(lambda t: t.tag_ in whitelist, [token for token in b])]
    score = 0

    for position, value in enumerate(lemma_a):
        try:
            score += 1 / abs(position - lemma_b.index(value)) if position - lemma_b.index(value) else 1
        except ValueError:
            pass
    return score / len(lemma_a) if len(lemma_a) > 0 else 0


def fuzzy(a: Doc, b: Doc):
    """
    Compares a to b by comparing difference of lemma words.
    Note that this compares the characters in the words, so similar words will be considered similar.
    :return: The similarity as a percentage.
    :param a: An (opinion) as a Doc.
    :param b: An (opinion) as a Doc.
    """

    return fuzz.token_set_ratio(" ".join([token.lemma_ for token in a]),
                                " ".join([token.lemma_ for token in b])) / 100
