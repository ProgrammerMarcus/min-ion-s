# Intended to be used to update the semantics dictionary based on the context in which it applies.

def get_custom_lexicon(context: str):
    """
    Returns a custom sentiment lexicon based on the given context.
    :param: The context to adapt the custom lexicon to.
    :return: A dictionary of words with updated polarity scores.
    """
    if context == "horror":
        # return {
        #     "terrifying": 0.5,
        #     "scary": 0.5,
        #     "spooky": 0.5
        # }
        return [
            ("scary", "positive"),
            ("terrifying", "positive"),
            ("spooky", "positive"),
            ("never ghostly", "negative")
        ]
