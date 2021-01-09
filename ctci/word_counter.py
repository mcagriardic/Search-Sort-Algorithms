"""
Cracking the Coding Interview
Write a function which counts how many times each word appears in a paragraph
"""


paragraph = """
                The Cecil B. DeMille Award is an honorary Golden Globe Award bestowed by the Hollywood 
                Foreign Press Association for outstanding contributions to the world of 
                entertainment. The HFPA board of directors selects the honorees from a variety 
                of actors, directors, writers and producers who have made a significant mark in 
                the film industry. It was first presented at the 9th Golden Globe Awards ceremony 
                in February 1952 and is named in honor of its first recipient, director Cecil B. 
                DeMille. The award has been presented annually since 1952, with exceptions 
                being 1976 and 2008.
            """

from collections import defaultdict

def count_words(paragraph):
    word_count = defaultdict(lambda: 0)
    paragraph = paragraph.split(" ")
    for w in paragraph:
        w = w.replace("\n", "")
        if w[-1] in (",", "."):
            w = w[:-1]
        word_count[w] += 1
    return word_count

count_words(paragraph)

"""
>> defaultdict(<function __main__.count_words.<locals>.<lambda>()>,
            {'The': 3,
             'Cecil': 2,
             'B': 2,
             'DeMille': 2,
             'Award': 2,
             'is': 2,
             'an': 1,
             'honorary': 1,
             'Golden': 2,
             'Globe': 2,
             'bestowed': 1,
             'by': 1,
             'the': 5,
             'Hollywood': 1,
             'Foreign': 1,
             'Press': 1,
             'Association': 1,
             'for': 1,
             'outstanding': 1,
             'contributions': 1,
             'to': 1,
             'world': 1,
             'of': 4,
             'entertainment': 1,
             'HFPA': 1,
             'board': 1,
             'directors': 2,
             'selects': 1,
             'honorees': 1,
             'from': 1,
             'a': 2,
             'variety': 1,
             'actors': 1,
             'writers': 1,
             'and': 3,
             'producers': 1,
             'who': 1,
             'have': 1,
             'made': 1,
             'significant': 1,
             'mark': 1,
             'in': 3,
             'film': 1,
             'industry': 1,
             'It': 1,
             'was': 1,
             'first': 2,
             'presented': 2,
             'at': 1,
             '9th': 1,
             'Awards': 1,
             'ceremony': 1,
             'February': 1,
             '1952': 2,
             'named': 1,
             'honor': 1,
             'its': 1,
             'recipient': 1,
             'director': 1,
             'award': 1,
             'has': 1,
             'been': 1,
             'annually': 1,
             'since': 1,
             'with': 1,
             'exceptions': 1,
             'being': 1,
             '1976': 1,
             '2008': 1})
"""