import spacy
from spacytextblob.spacytextblob import TextBlob

import extract
import source


# def get_sentiment_score_from_list(reviews: list):
#     nlp = spacy.load("en_core_web_lg")
#     nlp.add_pipe("spacytextblob")
#
#     positive_threshold = 0.2
#     negative_threshold = -0.2
#
#     # analyze sentiment of each review and categorize it as positive, negative or neutral
#     for review in reviews:
#         doc = nlp(review)
#         polarity_score = doc._.blob.polarity
#         print(review)
#         print(polarity_score)
#         # aspects = {}
#         # for token in doc:
#         #     # print(token)
#         #     if token.pos_ == "NOUN":
#         #         # print("yes")
#         #         aspect = token.text.lower()
#         #         if aspect not in aspects:
#         #             aspects[aspect] = []
#         #         aspects[aspect].append(token)
#         # print(f"Review: {review}")
#         #
#         # for aspect, tokens, in aspects.items():
#         #     sentiment_scores = [t._.polarity for t in tokens]
#         #     aspect_sentiment = sum(sentiment_scores) / len(sentiment_scores)
#         #     print(f"{aspect.capitalize()}: {aspect_sentiment}")
#         # print()
#         # if polarity_score >= positive_threshold:
#         #     score = {
#         #
#         #     }


def analyze(reviews: list):
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe("spacytextblob")
    opinion_sentiments = list()

    # Should the reviews/opinions be categorized in positive, negative and neutral?
    positive_threshold = 0.1
    negative_threshold = -0.1

    # TODO: Find a way to "weight" some words?
    #  For example, the sentiment of 'scary' is negative, but it's mostly used in a positive way in the reviews.
    custom_weights = {"scary": 0.25, "spookly": 0.25}

    for r in reviews:
        # doc = nlp(r)
        opinions = extract.extract(r)
        # Getting the polarity score of every opinion extracted from a review
        polarity_scores = [TextBlob(o).sentiment.polarity for o in opinions]
        # The sum of the polarity score of each opinion from a review
        polarity_score = sum(polarity_scores) / len(polarity_scores) if len(polarity_scores) else 0

        sentiment = {
            "review": r,
            "polarity": polarity_score
        }
        opinion_sentiments.append(sentiment)

    return opinion_sentiments


# sources = source.get_sources()
# print(analyze(sources))
