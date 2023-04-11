sources = [
    "Absolutely wonderful! Perfect mix of gore and humour with the opportunity to see Gamla Stan in a new light. Corey was a fantastic guide and I thoroughly enjoyed this tour, especially the crypt at the end. Highly recommend this!",
    "Our guide was very good and made the tour interesting. This was more of a gory history tour than a ghost tour. That being said it was interesting and the guide was very good.",
    "What a fantastic experience it was! Our guide Callum is an amazing story teller, funny with a big knowledge of Swedish history! It was 1,5 hour best spend! We saw Stockholm from the different perspective! Absolutely love it- every minute of it!",
    "Excellent and funny commentary. Callan was great guide. Learnt heaps.Great value for money. Would recommend for ages",
    """A great way to spend our first evening in Stockholm!
Our guide was Callum who led us round the beautiful old streets of Gamla Stan....and enlightened us about Stockholm's gruesome history. Callum was a great storyteller who brought the spooky in spades.
Very atmospheric, spooky and funny!
A word of caution; the stories are not for the faint hearted !
Highly recommend.""",
    """Very entertaining but not very ghostly!

The guide Cody was very entertaining it was more of a history lesson but was still throughly enjoyable and we got to explore the old town""",
    """Callum was our guide. He was extremely theatrical which made everything less believable. And he was low-key racist - which wasn’t fun. The tour was never ghostly at all or even gory to be honest. I would not recommend.""",
    """About an hour and a half of we’ll done storytelling, attention retaining, and joke cracking. Callum was a great guide and storyteller and felt like he genuinely enjoyed performing.

I went solo and enjoyed it thoroughly, and I can safely say that it would be just as good, if not better with friends.""",
    """Wonderful tour with Chris, excellent storytelling and humour throughout and made an excellent start to our Stockholm city break. """,
    """Corey’s storytelling was captivating and the visit to the crypt was excellent! We got to see parts of the city we might have missed and the historical aspect was fascinating.""",
    "Very entertaining and intresting Tour. Kallem is very enthusiastic and knows how to tell a story. He combines historical facts and scary storys with his scottish humor. ",
    'Great entertainment on a cold evening. The "guide" Callam was spookly great :-) You will see some cute, narrowed streets and spots. ',
    "Attended to English version. Recommended for a brief history lesson, and a nice tour! Nice date idea",
    """The tour guide was a good laugh, and the tour was filled with interesting landmarks and gory tales! The only downside was the lack of ghost stories. I think it should be renamed to 'dark history of Stockholm' or something similar. It was still worth the money, however, as you are acquainted with the area of Gamla Stan while being entertained at the same time!""",
    "A fun way to explore Gamla Stan at night! Our host was fun and charismatic. My my wife and I enjoyed and I think it would be fun for families as well.",
    """Our family doesn't really do tours. We like to get lost on our own and see what we see but Callum may have finally changed all of that going forward. He gave us a true understanding of what it might have been like back when Stockholm was a small brutal city. He is a wonderful storyteller and raconteur! The last story he shared of an experience he had in the vault of the old German church is still raising hairs on the backs our necks. Thank you, Callum for a wonderful experience!""",
    """Great tour overall, the guide - Callum was amazing and made the whole experience a hundred times better!""",
    """We really enjoyed The Gamla Stan ghost walk. Chris our guide was excellent. He voice was loud and clear for all to hear. He was a great story teller, he made us laugh and shocked us at the horrors he told, he was a true entertainer.
Wish all walking guides were as good.""",
    """Very funny guide Chris. Great way to learn about history in a spooky spirit. 8/10 would recommend. But bring warm clothes if in winter. """,
    """It was very nice to explore the city with the guide. The trip was interactive and very exciting and the guide had great charisma"""

]


def get_sources():
    processed = list()
    for source in sources:
        processed.append(source.replace("\n", " "))
    return processed
