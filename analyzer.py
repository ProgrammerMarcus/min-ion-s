import pattern.text.en
import spacy
from spacytextblob.spacytextblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
# from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import PatternAnalyzer
from textblob import Blobber

import context
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

    # TODO: For temporary test, remove later and set context somewhere else
    # Set context and update semantics lexicon
    # custom_lexicon = context.get_custom_lexicon("horror")
    # custom_analyzer = NaiveBayesAnalyzer(custom_lexicon)

    for r in reviews:
        # doc = nlp(r)
        opinions = extract.extract(r)
        # blob = TextBlob(r, analyzer=custom_analyzer)
        # Getting the polarity score of every opinion extracted from a review
        polarity_scores = [TextBlob(o).sentiment.polarity for o in opinions]
        # The sum of the polarity score of each opinion from a review
        polarity_score = sum(polarity_scores) / len(polarity_scores) if len(polarity_scores) else 0

        sentiment_score = {
            "review": r,
            "polarity": polarity_score
        }
        opinion_sentiments.append(sentiment_score)

    return opinion_sentiments


sources = source.get_sources()
print(analyze(sources))
