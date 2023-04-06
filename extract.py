import spacy
from spacy.tokenizer import Tokenizer
from spacy.util import compile_infix_regex
from spacy import displacy
from spacy.matcher import Matcher
from spacy.lang.en import English


def extract(source: str):
    # lg performs best so far
    nlp = spacy.load("en_core_web_lg")
    nlp.disable_pipes("ner")

    # prevent splitting of hyphens by removing rule
    infix = compile_infix_regex([x for x in nlp.Defaults.infixes if '-|–|—|--|---|——|~' not in x])
    nlp.tokenizer = Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
                              suffix_search=nlp.tokenizer.suffix_search,
                              infix_finditer=infix.finditer,
                              token_match=nlp.tokenizer.token_match,
                              rules=nlp.Defaults.tokenizer_exceptions)

    ruler = nlp.add_pipe("entity_ruler")

    # add pattern tour interesting

    # add pattern wasn't fun

    # add pattern would not recommend

    # add pattern funny with a big knowledge

    # add pattern absolutely love it

    # add pattern better with friends

    # add pattern cute, narrowed streets and spots

    # add pattern voice was loud and clear

    # add pattern Callum was amazing

    # add pattern intresting Tour

    # add pattern not very ghostly

    # fix 's gruesome history
    # add optional and
    dependency1 = [
        {"POS": {"IN": ["AUX", "PART", "VERB"]}, "OP": "{0,3}", "DEP": {"NOT_IN": ["auxpass", "conj"]}},
        {"DEP": "det", "LOWER": {"NOT_IN": ["the", "all", "a"]}, "OP": "?"},
        {"POS": {"IN": ["ADJ", "ADV"]}, "DEP": {"NOT_IN": ["npadvmod", "advmod"]}, "OP": "{1,5}"},
        {"POS": {"IN": ["NNP", "NOUN"]}, "OP": "{1,}"}
    ]

    # prevent CCONJ for last word (fixed?)
    dependency2 = [
        {"POS": {"IN": ["NNP", "NOUN"]}, "OP": "{1,2}"},
        {"POS": "AUX"},
        {"DEP": "det", "LOWER": {"NOT_IN": ["the", "all"]}, "OP": "?"},
        {"POS": {"IN": ["ADJ", "ADV"]}, "OP": "{1,}"},
        {"POS": {"IN": ["ADJ", "ADV", "CCONJ"]}, "OP": "{0,}"},
    ]

    dependency3 = [
        {"POS": {"IN": ["NNP", "NOUN"]}, "OP": "{1,}"},
        {"POS": "VERB"},
        {"POS": {"IN": ["VERB", "ADV"]}},
        {"POS": {"IN": ["NNP", "NOUN"]}, "OP": "{1,2}"},
        {"POS": {"IN": ["VERB", "ADP", "PART"]}, "OP": "{0,4}"},
    ]

    constituency1 = [
        {"POS": "DET", "OP": "?"},
        {"POS": {"IN": ["NOUN", "NNP"]}, "OP": "{1,}", "DEP": {"NOT_IN": ["pobj"]}},
        {"POS": {"IN": ["NOUN", "NNP", "CCONJ"]}, "OP": "{,3}"},
        {"POS": "AUX"},
        {"POS": {"IN": ["VERB", "ADP", "NOUN", "ADP"]}, "OP": "{1,3}"},
        {"POS": {"IN": ["VERB", "CCONJ", "ADJ"]}, "OP": "{0,2}"},
    ]

    constituency2 = [
        {"POS": {"IN": ["PRON"]}, "OP": "{1,}"},
        {"POS": {"IN": ["AUX", "PART"]}, "OP": "{1,2}"},
        {"POS": {"IN": ["ADP", "ADJ", "NOUN", "NNP", "VERB"]}, "OP": "{1,4}"},
        {"POS": {"IN": ["NOUN", "NNP"]}, "OP": "{1,2}"},
    ]

    # The shrimp tacos and house fries are my standbys
    constituency3 = [
        {"POS": "DET", "OP": "?"},
        {"POS": "ADJ", "OP": "{0,2}"},
        {"POS": {"IN": ["NOUN", "NNP"]}, "OP": "{1,4}", "DEP": {"NOT_IN": ["pobj"]}},
        {"POS": {"IN": ["NOUN", "NNP", "CCONJ"]}, "OP": "{0,4}"},
        {"POS": {"IN": ["AUX"]}},
        {"POS": "PRON", "OP": "?"},
        {"POS": {"IN": ["ADJ", "VERB", "NOUN"]}, "OP": "{1,2}"},
    ]

    constituency4 = [
        {"POS": "DET", "OP": "?"},
        {"POS": "ADJ", "OP": "{0,2}"},
        {"POS": {"IN": ["NOUN", "NNP"]}, "OP": "{1,4}"},
        {"POS": {"IN": ["NOUN", "NNP", "CCONJ"]}, "OP": "{0,4}"},
        {"POS": "PRON"},
        {"POS": {"IN": ["ADP", "VERB"]}, "OP": "{1,2}"},
        {"POS": "AUX"},
        {"POS": {"IN": ["PART", "ADP", "VERB"]}, "OP": "{1,4}"},
    ]

    constituency5 = [
        {"POS": {"IN": ["PRON"]}},
        {"POS": {"IN": ["AUX", "PART"]}, "OP": "{1,2}"},
        {"POS": {"IN": ["ADV"]}, "DEP": "advmod"},
        {"POS": {"IN": ["ADJ"]}, "DEP": "acomp"},
    ]

    patterns = [
        {"label": "DEPENDENCY_1", "pattern": dependency1},
        {"label": "DEPENDENCY_2", "pattern": dependency2},
        {"label": "DEPENDENCY_3", "pattern": dependency3},
        {"label": "CONSTITUENCY_1", "pattern": constituency1},
        {"label": "CONSTITUENCY_2", "pattern": constituency2},
        {"label": "CONSTITUENCY_3", "pattern": constituency3},
        {"label": "CONSTITUENCY_4", "pattern": constituency4},
        {"label": "CONSTITUENCY_5", "pattern": constituency5},

    ]

    ruler.add_patterns(patterns)

    doc = nlp(source)

    opinions = set()
    for ent in doc.ents:
        print(ent.label_, "|", ent.text)
        opinions.add(ent.text)
    print(opinions)
    # http://localhost:5000/
    # displacy.serve(doc, style="dep")

    return opinions


def test():
    opinion1 = """A warm-hearted waiter
greets us. The restaurant has
excellent Mexican cuisine,
but the slow service...""".replace("\n", " ")
    opinion2 = """We went there last night. No allergic reactions. The
shrimp tacos and house fries are my standbys. The fries
are sometimes good and sometimes great, and the spicy
dipping sauce they come with is to die for. Full beer
menu and long cocktail lists, all reasonable prices.""".replace("\n", " ")
    opinion3 = """This hotel is meant for weddings, there isn’t much service and the staff are like wedding planners. We had arrived early and was promised early check in but was told they had no information about this and asked us to come back later, when we did the same staff attended to us could not recognize us and forgot who we were when it was barely 2 hours ago that we spoke to her. They don’t help with bigger bags and you have to take them up to the rooms yourself. Rooms are really really tiny, toilet had barely space to turn around. Carpets were stained and dirty. They called us the moment we got to the room and instead of a welcome was told everything at the mini bar area is chargeable except the coffee and tea. They are so welcoming !!!! Noticed the sink was choked and called them but no one answered, when someone finally answered but with an unhappy voice and said loudly YES!!! When I told her about the sink she says she will send someone to check but the person never did. We did not bother anymore and left it as it was. When ever we used the sink we had to be careful not to flood the sink because of the choke. Staff are generally unfriendly and cold. You can see they are very fake even when they try to smile at you. Not worth the money we payed. A night costs around 500."""

    assert {'warm-hearted waiter', 'has excellent Mexican cuisine', 'slow service'} \
        .issubset(extract(opinion1))

    assert {'last night', 'Full beer menu', 'reasonable prices', 'fries are sometimes good and sometimes great',
            'No allergic reactions', 'The shrimp tacos and house fries are my standbys', 'long cocktail lists',
            'the spicy dipping sauce they come with is to die for'} \
        .issubset(extract(opinion2))

    # can't detect sarcasm
    assert {{'the sink was choked and called', 'the mini bar area is chargeable', 'They are so welcoming', 'This hotel is meant for weddings', 'same staff', 'They don’t help with bigger bags', 'Carpets were stained and dirty', 'an unhappy voice', 'they are very fake', 'isn’t much service', 'Rooms are really really tiny', 'Staff are generally unfriendly and cold', 'the staff are like wedding planners', 'toilet had barely space to turn around'}} \
        .issubset(extract(opinion3))
