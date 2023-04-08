import compare
import categorizer
from collections import defaultdict
def group_by_sequence(opinions: list):
    """
    Groups a list of opinions by similarity in text sequence.
    :param opinions:
    :return:
    """
    merged = dict()
    for opinion in opinions:
        # a value of 0.0 means that any similarity means that it similar
        filtered = list(filter(lambda entry: compare.compare(opinion, entry) > 0.0, opinions))
        merged.update({opinion: filtered})
        for r in filtered:
            opinions.remove(r)
    return merged

def group_by_difference(opinions: list):
    """
    Groups a list of opinions with levenshtein distance (probably).
    :param opinions:
    :return:
    """
    merged = dict()
    for opinion in opinions:
        # 0.60 is how much the texts needs to be similar, around 0.50 is good.
        filtered = list(filter(lambda entry: compare.fuzzy(opinion, entry) > 0.60, opinions))
        merged.update({opinion: filtered})
        for r in filtered:
            opinions.remove(r)
    return merged

def group_by_category(opinions: list):
    """
    Groups a list of opinions by category.
    :param opinions:
    :return:
    """
    categorized = categorizer.categorize(opinions)
    names = defaultdict(list)
    for opinion in categorized:
        for ent in opinion["ents"]:
            names.update({ent: list()})
    names.update({"UNCATEGORIZED": list()})
    for name in names.keys():
        for entity in categorized:
            if name in entity["ents"]:
                names[name].append(entity["text"])
            else:
                names["UNCATEGORIZED"].append(entity["text"])
    return names